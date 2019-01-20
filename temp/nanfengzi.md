Framework 中混合编程时 umbrella header 设置注意事项
--------
**作者**: [南峰子](https://weibo.com/3321824014)

Swift 和 Objective-C 混合编程，当需要在 Swift 中调用 Objective-C 代码时，在 App Target 中，我们依托的是 `Objective-C Bridging Header`，而在 Framework Target 中，依托的是 `unbrella header` ，即 Framework 的主头文件。我们需要做如下配置：

* 在 Build Setting -> Packaging 中将 Defines Module 设置为 YES，如下图所示；

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/01/6-1.png)

* 在 unbrella header  中导入需要暴露的 Objective-C 头文件

如果这样配置后，发现编译器还是报 `Use of undeclared type '**'` 错误，则确认以下两点：

* unbrella header 和需要暴露的 Objective-C 头文件是否包含在 Framework Target 中，如下图所示；

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/01/6-1.png)

* 在 Build Phases -> Headers 中，将 unbrella header 和需要暴露的 Objective-C 头文件放置在 Public 区域中，所下图所示!

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/01/6-1.png)

这样确认后，基本就没什么问题了。


