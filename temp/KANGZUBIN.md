## 使用 HTTPDNS 服务后，HTTPS 请求的证书校验问题

我们知道，客户端向服务端发起一个请求时，在建立 TCP/IP 连接前，需要有一个步骤就是根据请求 URL 中的域名获取对应服务器的 IP 地址，即 `DNS 解析`。

但在移动互联网络中，我们经常会遭遇到运营商的 DNS 劫持（利益使然），导致页面出现弹窗、小广告、服务不稳定、不可用等。为了解决这种情况，很多云服务厂商都提供了 HTTPDNS 服务：[阿里云](https://www.aliyun.com/product/httpdns?spm=5176.10695662.765261.732.16cf5279THiIA4)、[腾讯云](https://cloud.tencent.com/product/hd?from=qcloudHpHeaderHd)

>HTTPDNS 使用 HTTP 协议进行域名解析，代替现有基于 UDP 的 DNS 协议，域名解析请求直接发送到 HTTPDNS 服务器，从而绕过运营商的 Local DNS，能够避免 Local DNS 造成的域名劫持、调度不精准、延迟、不稳定等问题。 —— 引自阿里云文档

HTTPDNS 的基本原理如下图所示：

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/03/2-1.png?raw=true)

当客户端使用 HTTPDNS 解析域名时，请求 URL 中的 host 会被替换成 HTTPDNS 解析出来的 IP，这种方案对于 HTTP 请求不会有任何影响，但是对于 HTTPS 来说，由于请求前多了一个 SSL/TLS 握手过程，涉及到证书校验，这时候问题就来了！

在 SSL/TLS 握手过程中，服务端下发的证书里的 CN 字段（即证书颁发的域名）仍然为域名，但是请求中的 host 在请求前已经被我们替换为 IP 了，这时在证书校验时，就会出现 domain 不匹配的情况，导致 SSL/TLS 握手不成功，请求会被 Canceled 掉。

因此，我们需要对证书校验的逻辑做一下小改动，在 NSURLSession 的证书校验代理方法（`URLSession:didReceiveChallenge:completionHandler:`）中，增加一个前置处理：把待验证的的 domian 由原本的 IP 转换为其对应的域名，然后再进行下一步操作。代码如下：

```objc
- (void)URLSession:(NSURLSession *)session
didReceiveChallenge:(NSURLAuthenticationChallenge *)challenge
 completionHandler:(void (^)(NSURLSessionAuthChallengeDisposition disposition, NSURLCredential *credential))completionHandler
{
    NSURLSessionAuthChallengeDisposition disposition = NSURLSessionAuthChallengePerformDefaultHandling;
    NSURLCredential *credential = nil;
    
    // 证书验证前置处理
    NSString *domain = challenge.protectionSpace.host; // 获取当前请求的 host（域名或者 IP），此时为：123.206.23.22
    NSString *testHostIP = self.tempDNS[self.testHost];
    // 此时服务端返回的证书里的 CN 字段（即证书颁发的域名）与上述 host 可能不一致，
    // 因为上述 host 在发请求前已经被我们替换为 IP，所以校验证书时会发现域名不一致而无法通过，导致请求被取消掉，
    // 所以，这里在校验证书前做一下替换处理。
    if ([domain isEqualToString:testHostIP]) {
        domain = self.testHost; // 替换为：kangzubin.com
    }
    
    // 以下逻辑与 AFNetworking -> AFURLSessionManager.m 里的代码一致
    if ([challenge.protectionSpace.authenticationMethod isEqualToString:NSURLAuthenticationMethodServerTrust]) {
        if ([self evaluateServerTrust:challenge.protectionSpace.serverTrust forDomain:domain]) {
            // 上述 `evaluateServerTrust:forDomain:` 方法用于验证 SSL 握手过程中服务端返回的证书是否可信任，
            // 以及请求的 URL 中的域名与证书里声明的的 CN 字段是否一致。
            credential = [NSURLCredential credentialForTrust:challenge.protectionSpace.serverTrust];
            if (credential) {
                disposition = NSURLSessionAuthChallengeUseCredential;
            } else {
                disposition = NSURLSessionAuthChallengePerformDefaultHandling;
            }
        } else {
            disposition = NSURLSessionAuthChallengeCancelAuthenticationChallenge;
        }
    } else {
        disposition = NSURLSessionAuthChallengePerformDefaultHandling;
    }
    
    if (completionHandler) {
        completionHandler(disposition, credential);
    }
}

// 以下逻辑取自 AFNetworking -> AFSecurityPolicy 的 `evaluateServerTrust:forDomain:`
// 方法中 SSLPinningMode 为 AFSSLPinningModeNone 的情况
- (BOOL)evaluateServerTrust:(SecTrustRef)serverTrust forDomain:(NSString *)domain {
    // 创建证书校验策略
    NSMutableArray *policies = [NSMutableArray array];
    if (domain) {
        // 需要验证请求的域名与证书中声明的 CN 字段是否一致
        [policies addObject:(__bridge_transfer id)SecPolicyCreateSSL(true, (__bridge CFStringRef)domain)];
    } else {
        [policies addObject:(__bridge_transfer id)SecPolicyCreateBasicX509()];
    }
    
    // 绑定校验策略到服务端返回的证书（serverTrust）上
    SecTrustSetPolicies(serverTrust, (__bridge CFArrayRef)policies);
    
    // 评估当前 serverTrust 是否可信任，
    // 根据苹果文档：https://developer.apple.com/library/ios/technotes/tn2232/_index.html
    // 当 result 为 kSecTrustResultUnspecified 或 kSecTrustResultProceed 的情况下，serverTrust 可以被验证通过。
    SecTrustResultType result;
    SecTrustEvaluate(serverTrust, &result);
    return (result == kSecTrustResultUnspecified || result == kSecTrustResultProceed);
}
```

上述解决方法只适用于一台服务器的 IP 只配置了一个默认的域名和 SSL 证书的情况，而对于服务器配置了多个域名的证书的情况（即 SNI），比较复杂，我们下次再讲。

详细的 Demo 参见：https://github.com/kangzubin/DevDemo/tree/master/TestHTTPDNS

参考文档：
1、https://help.aliyun.com/document_detail/30143.html
2、[AFNetWorking Source Code](https://github.com/AFNetworking/AFNetworking)

## 解决 WKWebView 无法处理 URL Scheme 和 App Store 链接的问题

之前使用 UIWebView 时，当遇到 App Store 下载链接（例如：`https://itunes.apple.com/cn/app/id414478124?mt=8`），点击可以自动打开 iPhone 本地 App Store 并跳转到相应 App 的下载页面，

但是当换成 WKWebView 时，我们发现点击 App Store Links 时，有时候无反应，有时则会打开相应 App 的 App Store Web 页面，而不会直接调起本地 App Store。

另外，对于自定义的 URL Scheme 类型链接，在 WKWebView 里直接点击则会报错：`Error Domain=NSURLErrorDomain Code=-1002 "unsupported URL"`

所以我们需要在 WKWebView 即将加载某一 URL 时，对这两种情况做一下处理，修改 WKWebView 的 delegate 中的 `webView:decidePolicyForNavigationAction:decisionHandler:` 方法，当遇到上述两种链接时，我们交给系统的 `[[UIApplication sharedApplication] openURL:xxx]` 来处理即可，代码如图如下：

```objc
- (void)webView:(WKWebView *)webView decidePolicyForNavigationAction:(WKNavigationAction *)navigationAction decisionHandler:(void (^)(WKNavigationActionPolicy))decisionHandler {
    
    NSURL *url = navigationAction.request.URL;
    NSString *urlString = (url) ? url.absoluteString : @"";
    
    // iTunes: App Store link
    // 例如，微信的下载链接: https://itunes.apple.com/cn/app/id414478124?mt=8
    if ([urlString containsString:@"//itunes.apple.com/"]) {
        [[UIApplication sharedApplication] openURL:url];
        decisionHandler(WKNavigationActionPolicyCancel);
        return;
    }
    
    // Protocol/URL-Scheme without http(s)
    else if (url.scheme && ![url.scheme hasPrefix:@"http"]) {
        [[UIApplication sharedApplication] openURL:url];
        decisionHandler(WKNavigationActionPolicyCancel);
        return;
    }
    
    decisionHandler(WKNavigationActionPolicyAllow);
}
```

关于使用 WKWebView 的更多 Tips，可以参考：https://github.com/ShingoFukuyama/WKWebViewTips

