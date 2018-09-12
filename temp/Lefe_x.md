WKWebView给scrollView添加delegate crash
--------
**作者**: [Lefe_x](https://weibo.com/u/5953150140)

想监听 WKWebView 的滚动，我的做法是设置 WKWebView.scrollView.delegate，然而这种方法会导致在 iOS9 上 crash。使用全局断点并不能定位到 crash 的具体位置，当 crash 后，在打印控制台处输入 `bt`，发现有输出异常信息，大体意思是 WKWebView 已经释放，但在其它地方还在使用它的属性 scrollView。

关于这个 crash 的描述：

```
Possible crash when setting the WKWebViews's scroll view delegate, if the scroll view outlives the web view

Null out the internal delegate on the WKScrollView when the WKWebView goes away, since it's possible for a client to set its own scroll view delegate, forcing the creation of a WKScrollViewDelegateForwarder, and then retain the UIScrollView past the lifetime of the WKWebView. In this situation, the WKScrollViewDelegateForwarder's internalDelegate would point to a deleted WKWebView.
```

想解决这个问题需要在，dealloc 的位置把 delegate 设置为 nil：

```
self.webView.scrollView.delegate = nil;
```

参考：
[Webkit](https://trac.webkit.org/changeset/177329/webkit)