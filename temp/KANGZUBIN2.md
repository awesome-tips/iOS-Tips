Xcode 10.1 并没有修复由于 Assets 引起的在 iOS 9 上的崩溃问题
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

关于 Xcode 10.0 打的线上 Release 包会在 iOS 9.0 ~ 9.2.1 系统上出现随机的崩溃，相信大家已经不陌生了，网上已有不少关于[这个问题的讨论](https://blog.csdn.net/Hello_Hwc/article/details/82891405)。

之前 `@高老师很忙` 也写了一个小集[《解决 Xcode 10 打包 iOS 9.0 - iOS 9.2.1 Crash 的问题》](https://weibo.com/1608617333/GE8Glfzvi)，分析了这个问题产生的原因，以及如何解决这个问题。

我们的 App 上个月一开始用 Xcode 10.0 发了一个包，因为这个导致线上崩溃率直线上升（主要集中在 iOS 9），无奈之下，**只能用 Xcode 9.4.1 重新编译发了一版本**。

苹果号称在 Xcode 10.1 Beta 2 中解决了这个问题，然后在 2018 年 10 月 31 日，苹果发布了 Xcode 10.1 正式版，并在 Release Notes 中声称已经解决了这个问题，有如下截图为证：

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/11/3-1.jpg)

然而，当天立刻有人在苹果的开发者论坛（Apple Developer Forums）上发了帖子说这个问题仍然存在，

* [Xcode 10.1 did not fix the iOS 9 asset catalogs crash problem](https://forums.developer.apple.com/thread/110393)

如下图所示：

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/11/3-2.jpg)

国内也有很多开发者通过自身 App 的实践纷纷证实了这个问题。

我们 App 前几天发新版，打包人员疏忽忘记了这个问题，直接用 Xcode 10.1 发包上线，结果这两天果然在 iOS 9 上的崩溃率又上来了，惨痛教训！！！

另外，让人遗憾的是：苹果已经偷偷在 Xcode 10.1 的 [Release Notes](https://developer.apple.com/documentation/xcode_release_notes/xcode_10_1_release_notes?language=objc) 中，把这个问题从 Resolved Issues（已解决的问题）该为 Known Issues（已知问题）了，如下：

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/11/3-3.jpg)

临时解决方法：

* 参考之前高老师的小集介绍的几种方式

* 切回到 Xcode 9.4.1 打包

* 把 App 最低支持系统改为 iOS 10+ ...😅

* 等待 Xcode 10.2 解决 ...🤣
