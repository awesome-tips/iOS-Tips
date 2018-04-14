关于 Xcode console 输出的 UIImage 警告的解决方式
--------
**作者**: [Vong_HUST](https://weibo.com/VongLo)

最近项目中遇到 Xcode console 偶尔输出 `[framework] CUICatalog: Invalid asset name supplied: '(null)'` 这样一段 `warning`，毫无头绪。在爆栈上看到有人遇到一样的问题，原因是由于 `[UIImage imageNamed:]` 传了 `nil` 或者传入的 `string` 的 `length` 为0。至于怎么找到具体是哪里传了 `nil`，可以打一个全局断点，然后加一个条件来判断入参是否为空，即可找到有问题的地方。如图所示

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/04/4-1.jpg?raw=true)

还有遇到 `Could not load the "some-image-name" image referenced from a nib in the bundle with identifier "com.xxxx"` 这种情况，一般情况下是这张图片被删除了，但是 `Xib/Storyboard` 中还引用了这张图片，表现形式主要是 `UIImageView` 的 `image` 属性一栏是 `Unknown`，如下图

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/04/4-2.png?raw=true)

只要把这个 `Unknown` 改成对应图片即可。

参考链接：
[Error: CUICatalog: Invalid asset name supplied](http://t.cn/R06T3OW)
[Could not load the “xxx” image referenced from a nib in the bundle with identifier](http://t.cn/RmXu0sN)

