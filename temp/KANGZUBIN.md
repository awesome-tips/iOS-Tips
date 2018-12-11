Xcode 10 / iOS 12 获取 WiFi 信息
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

在一些特定业务场景下，我们需要获取 iOS 设备所连接的 WiFi 的信息，比如 WiFi 的 `SSID`（即 WiFi 的名称），WiFi 的 `BSSID`（即 WiFi 的路由器的 Mac 地址）等，相应的代码也很简单，大致如下图所示：

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/12/1-1.jpg)

在 Xcode 10（iOS 12）之前，上述代码可以正常运行取到结果，但当升级到 Xcode 10 后编译工程在 iOS 12 上运行时，同样的代码却无法取得 WiFi 的信息。通过断点调试发现 `CNCopyCurrentNetworkInfo(...)` 函数总是返回 `nil`，查阅官方 API 文档，发现该函数的描述多了一条重要提示，如下图红框内容：

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/12/1-2.jpg)

大致意思是说：在 iOS 12 及以上系统调用该方法时，需要先在 Xcode 工程中授权获取 WiFi 信息的能力，开启路径为：Xcode -> [Project Name] -> Targets -> [Target Name] -> Capabilities -> Access WiFi Information -> ON，如下图：

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/12/1-3.jpg)

设置完毕后，我们可以发现在工程的 `.entitlements` 文件会多了一对键值：

`Access WiFi Information` => `YES`

至此，我们就可以正常在 iOS 12+ 中获取 WiFi 的信息了。

* 参考链接：[https://juejin.im/post/5ba20f4b6fb9a05ce469c027](https://juejin.im/post/5ba20f4b6fb9a05ce469c027)
