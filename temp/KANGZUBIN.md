TestFlight 内测邀请弹窗的实现
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

最近，我们在使用一些 App 时经常会遇到，在 App 刚启动不久后有时我们会看到一些内测弹窗，类似 “恭喜您获得内测资格，诚邀您体验新版本...”，然后点击下载按钮时就会跳转到 TestFlight 中安装测试版本，（注意不是跳转到 App Store 中更新最新版本哦），而且用户无需输入任何测试邀请码。

我们知道，TestFlight 是苹果官方提供的内测平台，在刚推出时，使用起来很繁琐，开发者需要先收集用户的邮箱，然后在提交测试版本苹果审核通过后，给他们发邀请码，最后需要用户手机安装 TestFlight App 并输入对应的邀请码才能开始安装内测。

于是国内也诞生了很多像蒲公英、fir.im、testflight.top 等内测应用分发平台，优化了体验流程。

终于，在去年苹果自己也简化了 TestFlight 的使用流程，支持通过同一公开链接邀请 TestFlight 测试员，无需再收集邮箱和发送邀请码了，如图所示。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/02/1-1.jpg)

因此我们大致可以使用如下步骤实现开头说的功能：

1、上传新的构建版本包到 App Store Connect 后台，并提交 Beta Test 申请，苹果审核通过后，我们可以创建一个 TestFlight Public Link，并把这个公开测试邀请链接保存到我们的服务端，通过某一接口灰度下发给 App；

2、App 在启动后特定的时机调用接口查询是否有新的内测邀请链接，如果有就弹窗提醒用户是否要参与内测；

3、如果用户点了确认，就通过 UIApplication 的 openURL 方法打开 TestFlight Public Link，此时就会自动跳转到 TestFlight App 中进行内测版的安装，用户无需输入邀请码，如用户未安装 TestFlight 会先提示安装。

但 TestFlight Public Link 有两个限制：最大测试人数上限为 1 万人，且测试版本仍然需要通过苹果的审核。更多细节可以参考这个 [WWDC 视频](https://developer.apple.com/videos/play/wwdc2018/301/)，大概从 10 分钟左右开始讲。

* 参考链接：[https://juejin.im/post/5bac3ba7e51d450e531c9d2c](https://juejin.im/post/5bac3ba7e51d450e531c9d2c)
