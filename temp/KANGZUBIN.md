iOS 判断设备是否锁屏
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

在某些特定的业务场景下，我们可能需要判断用户在使用 App 过程中是否锁屏了。那么，我们该如何监听 iOS 设备的锁屏事件呢？

在 AppDelegate 的回调事件中，当单击 Home 键进入后台时，会依次调用 `applicationWillResignActive:`（App 即将失去焦点）和 `applicationDidEnterBackground:`（App 已经进入后台），而当 App 在前台使用过程中进行锁屏操作时，也是依次执行这两个回调。

因此，我们无法通过 AppDelegate 的上述相应回调事件来直接判断设备是否锁屏了。

在网上搜了一下，目前主要有以下几种方式：

* 通过 Darwin 通知监听锁屏事件，代码大致如图 1 所示，**不过这种方式已被禁用，在提交 App Store 审核时会被拒。**

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/03/1-1.png)

* 通过 `<notify.h>` 中的 `notify_register_dispatch` 函数添加锁屏和解锁监听，代码如图 2 所示。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/03/1-2.png)

* 苹果官方其实也提供了另外两个回调：`applicationProtectedDataWillBecomeUnavailable:` 和 `applicationProtectedDataDidBecomeAvailable:` 可以分别用于判断锁屏和解锁事件，如图 3 所示，不过这两个方法只有在手机设置了密码、TouchID 或 FaceID 时才会调用。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/03/1-3.png)

* 通过屏幕亮度是否为 0 进行判断。如前面所述，在 App 打开状态下，对于点击 Home 键和锁屏操作，接收到的回调事件是一样的。因此，我们可以在 App 进入后台的 `applicationDidEnterBackground:` 回调中获取当前屏幕的亮度值，如果为 0，则认为是锁屏操作，否则认为是点击了 Home 键，代码如图 4 所示。不过这种方式存在不足，经验证，有时锁屏后获取到的屏幕亮度值并不为 0，且如果手机的亮度调到最低时，获取到的亮度值始终都为 0，就无法区分锁屏和 Home 键了。详细参考[这篇文章](https://a1049145827.github.io/2018/01/06/iOS%E5%BC%80%E5%8F%91-%E5%8C%BA%E5%88%86Home%E9%94%AE%E5%92%8C%E9%94%81%E5%B1%8F%E9%94%AE%E4%BA%8B%E4%BB%B6/)。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/03/4-1.png)

* 此外，[这篇文章](https://www.jianshu.com/p/4d6472735e42)中也提出一种通过是否能更改屏幕亮度进行判断。代码如图 5 所示，不过经验证，这种方式无效！

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/03/5-1.png)

更多其它的方式，详见[这篇文章](https://juejin.im/entry/5be54d816fb9a049ea387454)中的介绍。

PS1：上述方法仅适用于 App 在使用过程中进行锁屏操作的判断，如果先点击 Home 键进入后台再锁屏，就无法知道了。

PS2：上述代码在 iOS 12+，iPhone XS 上验证通过，对于其它版本系统或者设备，如有不同，欢迎指出~

扩展阅读：[iPhone Objective-C detect Screen Lock](https://stackoverflow.com/questions/37649808/iphone-objective-c-detect-screen-lock)、[Detecting iPhone lock and unlock when app is in the background](https://forums.developer.apple.com/thread/69333)
