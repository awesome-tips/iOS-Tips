webview关闭时手动停止音频播放
--------
**作者**: [halohily](https://weibo.com/halohily)

当我们使用 webview 展示网页时，页面内若含有音频标签，点击播放，这时关闭带有 webview 的 VC，会发现即使 webview 已经被释放，音频还是没有停止。这时可以采用比较快捷的方法来做到 webview 被关闭时停止正在播放的音频：webview 重新 load 页面，或者执行停止音频播放的 JavaScript 语句。

这里以 UIWebview 举例，WKWebview 同理。

方法一：重新 load 一个空白页面

> [self.webView loadRequest:[NSURLRequest requestWithURL:[NSURL URLWithString:@"about:blank"]]];

方法二：手动执行停止音频的 JavaScript 语句

> [self.webView stringByEvaluatingJavaScriptFromString:@"audioPause()"];

当然，这两种方法都是比较简便但不优雅的实现方式，适合轻度使用 webview 的场景。如果你们对于 webview 做了比较多的加工，是可以监听 webview 中的音频、视频任务，来手动停止的。

