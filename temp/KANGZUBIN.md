iOS9 以后 openURL 和 canOpenURL 使用限制的小误区
----

**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

通常我们会用 `UIApplication` 的 `openURL:` 方法调起其他 App 来进行一些操作，如分享、第三方登录、支付等。但 `iOS9` 发布后，在看了很多适配总结的文章后，相信很多人可能跟我一样会有如下理解：

> `iOS9` 限制了 `openURL:` 和 `canOpenURL:` 方法的使用，如果我们要调起第三方 App，需要在 `Info.plist` 的 `LSApplicationQueriesSchemes` Key 中添加相应 App 的 `Scheme` 才行，且添加的 `Scheme` 个数不能超过 **50** 个。

**其实上面描述是有误的。**

举个例子，大部分 App 在接入微信的 `SDK` 后，会先在自己工程配置中的 `Info` -> `URL Types` 添加注册一个 `Scheme`，叫 “wx+appId” ，以便在调起微信进行登录或分享后，微信回调返回到我们自己的 App 中。但是试想一下，如果 `openURL:` 使用必须事先声明且有个数的限制，那么微信如何回调成千上万的 App 呢，难道微信要在其工程的 Info.plist 中把这些第三方 App 的 `Scheme` 都添加进去，而且每天都会有新增的 App 接入了微信 `SDK`，如何动态更新添加 Scheme 呢？微信是有什么黑科技或者苹果给微信等大厂的超级 App 开了特殊通道？

在查阅了苹果官方文档后，我们发现其实并不是这样的，如下图：

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/03/6-1.jpg)

>**！！！只有 `canOpenURL:` 方法的使用受 `Info.plist` 中声明的 `Scheme` 的限制，而 `openURL:` 方法是不受限制的，不需要事先声明，也没有个数限制。**（其实在 `iOS9` 的某 Beta 版上，`openURL:` 也受同样限制，但苹果后面确认是 Bug，在正式版中已更正过来）

另外关于 `canOpenURL:` 最多只能对 **50** 个 `Scheme` 做判断的说法也是错误的。苹果的正确描述是：**“如果你的 App 是使用 `Xcode 7 (iOS9 SDK)` 之前版本编译的，但是在 `iOS9` 及以后的系统中运行，那么你的 App 最多只能调用 50 次 `canOpenURL:` 方法，超过 50 次后，该方法都会返回 `NO`。”**

如果我们使用最新版的 `Xcode` 编译 App，`canOpenURL:` 能判断的 `Scheme` 个数应该是不受限制的。

我写了一个 `Demo` 验证了以上说法，如下图所示，在 `Info.plist` 中我先添加了超过 100 个 `Scheme` 后再添加 "weixin"，仍可以通过 `canOpenURL:` 判断是否安装了微信，另外即使没有添加微博的 `Scheme` "sinaweibo" 也可以通过 `openURL:` 正常打开。

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/03/6-2.jpg)

Demo 地址：[TestOpenURL](https://github.com/kangzubin/DevDemo/tree/master/TestOpenURL)

>虽然 `openURL:` 方法使用不受限制，但是苹果还是建议我们在使用它之前，先调 `canOpenURL:` 判断一下，再进行后续操作。

以上测试结果是在真机 **`iPhone 8 (iOS 11.2.6)`** 上进行的，如果其他设备或者系统版本有差异，欢迎留言讨论。

参考链接：

1、[Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiapplication/1622952-canopenurl?language=objc)
2、[Querying URL Schemes with canOpenURL](https://useyourloaf.com/blog/querying-url-schemes-with-canopenurl/)
