iOS 获取设备型号最新总结
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

在开发中，我们经常需要获取设备的型号（如 `iPhone X`，`iPhone 8 Plus` 等）以进行数据统计，或者做不同的适配。但苹果并没有提供相应的系统 API 让我们直接取得当前设备的型号。

其中，`UIDevice` 有一个属性 `model` 只是用于获取 iOS 设备的类型，如 `iPhone`，`iPod touch`，`iPad` 等；而其另一个属性 `name` 表示当前设备的名称，由用户在设置》通用》关于》名称中设定，如 `My iPhone`，`xxx 的 iPhone` 等。然而，我们无法根据这两个值获得具体的型号。

不过，每一种 iOS 设备型号都有对应的一个或多个硬件编码/标识符，称为 `device model` 或者叫 `machine name`，之前的小集介绍过，我们可以通过如图 1 中的代码来获取：

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/10/4-1.png)

所以，通常的做法是，先获取设备的 `device model` 值，再手动映射为具体的设备型号（或者直接把`device model` 值传给后端，让后端去做映射，这样的好处是可以随时兼容新设备）。

例如：去年发布的第一代 iPhone X 对应的 `device mode` 为 `iPhone10,3` 和 `iPhone10,6`，而今年最新发布 iPhone XS 对应 `iPhone11,2`，iPhone XS Max 对应 `iPhone11,4` 和 `iPhone11,6`，iPhone XR 对应 `iPhone11,8`，完整的 device mode 数据参考 Wiki：

* [https://www.theiphonewiki.com/wiki/Models](https://www.theiphonewiki.com/wiki/Models)

综上，我们可以先获取 `device model` 值，记为 `platform`，然后进行对比判断，转换成具体的设备类型。实现代码如图 2、3 所示：

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/10/4-2.png)
![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/10/4-3.png)

备注：图中代码只给了对 iPhone 设备型号的判断，而完整的包括 iPad 和 iPod touch 型号我已经放在 GitHub Gist 上，大家可以参考，[详见这里](https://gist.github.com/kangzubin/5b4f989d6b1113bfbe43c5772f3ba1fd)。

参考链接：

* [The iPhone Wiki](https://www.theiphonewiki.com/wiki/Models)
* [fahrulazmi/UIDeviceHardware](https://github.com/fahrulazmi/UIDeviceHardware)