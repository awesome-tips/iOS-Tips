解决 WKWebView 无法处理 URL Scheme 和 App Store 链接的问题
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

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

关于使用 WKWebView 的更多 Tips，可以[参考](https://github.com/ShingoFukuyama/WKWebViewTips)

