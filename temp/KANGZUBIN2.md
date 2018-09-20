检测设备是否为 iPhone X/XS/XR 的几种方式
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

在上一条小集[《iPhone 屏幕分辨率终极指南》](https://weibo.com/1645958062/GA26Ux6TR)中，我们整理介绍了目前已发布的所有 iPhone 设备的屏幕数据，包括了最新上市的 iPhone XS、iPhone XS Max 和 iPhone XR。

最后我们介绍了一种在代码中通过获取屏幕的高度判断是否等于 812.0 或 896.0 来检测设备是否为 iPhone X 的方法，但该方法存在小瑕疵，需要考虑一下两点：

* 当 App 支持横竖屏切换时，在横屏模式下也能够正确判断；

* 在模拟器中调试时，能够正确判断当前所选则的模拟器类型是不是 iPhone X；

因此，本条小集重新整理一下我们目前所了解到的几种检测设备是否为 iPhone X 的方式，供大家参考，不足之处欢迎补充。

备注：这里所说的 iPhone X 泛指屏幕大小为 5.8、6.1、6.5 英寸三种尺寸，且带有顶部刘海和底部操作条的 iPhone 设备。

方式一：通过获取设备的 device model 来判断

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/09/2-1.png)

方式二：通过获取屏幕的宽高来判断

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/09/2-2.png)

方式三：通过底部安全区域的高度来判断

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/09/2-3.png)

方式四：通过是否支持 FaceID 判断

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/09/2-4.png)

方式五：通过 UIStatusBar 的高度判断

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/09/2-5.png)

由于小集篇幅有限，这几种方式的实现和优缺点分析详见我写的这篇博文：

* https://kangzubin.com/iphonex-detect/ 

你是否有其他判断方式呢？欢迎补充~

参考链接：[Detect if the device is iPhone X](https://stackoverflow.com/questions/46192280/detect-if-the-device-is-iphone-x/)
