iOS 如何调试 WebView （二）
--------
**作者**: [Lefe_x](https://weibo.com/u/5953150140)

上次的小集中，我主要讨论了如何调试 WebView ，小集发出后  @折腾范儿_味精 提供了另一种方法来调试 WebView。我觉得有必要再扩展一下，原话是这样的：

> 真说方便还是植入一个 webview console 在 debug 环境，可以在黑盒下不连电脑不连 safari 调 dom，调js，另外在开发期间 Xcode 断点 run 的时候，js hook console.log console.alert，接管window.onerror 全都改 bridge NSLog 输出，也会方便点。

短短几句话，信息量很大，私下向味精学习了下，这里总结一下。写完这个小集特意让味精看了下，觉得有必要再补充下第二种调试技巧，但中途踩了几个坑，一直到23:30左右才搞定。

第一，把 WebView 用来调试的 log、alert、error 显示到 NA ，在调试时会方便不少。做 WebView 与端交互的时候，主要用 `window.webkit.messageHandlers.xxx.postMessage(params);` 来给端发消息，也就是说 WebView 想给端发消息的时候直接调用这个方法即可，端会通过 `WKScriptMessageHandler` 的代理方法来接收消息，而此时端根据和 WebView 约定的规则进行通信即可。

```
- (void)userContentController:(WKUserContentController *)userContentController didReceiveScriptMessage:(WKScriptMessage *)message
```

而添加调试信息，无非就是给 WebView 添加了 log、alert、error 这些消息的 bridge，这样当 WebView 给端发送消息后，端根据和 WebView 约定的规则解析 log、alert、error 为端对应的事件，比如 log 直接调用端的 `NSLog`，alert 调用端的 `UIAlertController`。

第二，黑盒下调试 WebView，无需连接电脑和 safari 即可调试 DOM，这个可以参考小程序的 [vConsole](https://github.com/Tencent/vConsole) 或者 [eruda
](https://github.com/liriliri/eruda) 。可以直接在 WebView 中接入，或者在端中接入。这里以在端中接入 eruda 为例，这里踩到几个坑：

1.有些页面显示不出来，估计是故意屏蔽掉的，味精特意使用 JSBox 试了下其它页面，发现百度等都不可以显示调试按钮，而掘金是可以的；

2.使用本地的页面也显示不出来，这是 webview 跨域安全方面的考虑，file 协议下会禁止 js css html 以部分 file，部分网络的方式加载。

下面这段代码直接在 webview 加载完成后执行即可。

```
NSString *js = @"(function() {var script = document.createElement('script');script.type = 'text/javascript';script.src = 'https://xteko.blob.core.windows.net/neo/eruda-loader.js';document.body.appendChild(script);})();";
[self.webView evaluateJavaScript:js completionHandler: nil];
```


![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/05/14-1.jpg)