关于Xcode Simulator无法启动的原因
-------
**作者**: [这个汤圆没有馅](https://weibo.com/u/6603469503)

前几天为了清理Xcode缓存，误删了文件，编译时仍然有一堆模拟器可以选择，但是却无法启动模拟器。

先是`Command + R`后等待一段时间报出超时错误。
![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/04/1-1.jpg)

再在应用程序中找到Xcode，打开包内容，找到`Developer-->Applications-->Simulator`，双击后提示磁盘中并没有模拟器设备。
![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/04/1-2.jpg)

进入文件夹`~/Library/Developer/CoreSimulator/Devices`，发现目录下是空的，这就是导致模拟器无法启动的原因。

按顺序找到`Xcode-->Window-->Devices and Simulators`，点击左下角的【+】添加新的模拟器，完成后再次打开 `~/Library/Developer/CoreSimulator/Devices`，会发现目录下有内容，如下图。进入文件夹，打开`device.plist`，里面就是刚添加的模拟器的设备信息，然后就可以正常运行项目了
![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/04/1-3.jpg)

如有表述不当，欢迎指出~~
