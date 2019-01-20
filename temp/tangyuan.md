Debug Memory Graph检查内存泄漏
-------
**作者**: [这个汤圆没有馅](https://weibo.com/u/6603469503)


在日常检查内存泄漏时，除了 Instruments 里的 Leaks，还有一个就是 Xcode 8推出的 Debug Memory Graph。

为了能看到内存详细信息，先打开 Edit Scheme-->Diagnostics, 勾选 Malloc Scribble 和 Malloc Stack。为了避免过多的性能消耗，在 Malloc Stack 中直接选择 Live Allocations Only 即可。
![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/01/2-1.jpeg)

运行 App，找到查看视图层级 Debug View Hierarchy 边上的三个小圈圈的按钮，这个就是Debug Memory Graph按钮，点击后页面变化如下图。
![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/01/2-2.jpeg)

左边栏会有当前运行 App 的文件信息，若有内存泄漏，边上会有一个紫色的感叹号。也可以通过下方的 show only leaked blocks 过滤文件。

中间区域内容是当前文件内存详细信息及对象之间的关联关系。黑色线条代表强引用，不过灰色的线不代表弱引用，只是一些系统级别的引用或者苹果为了优化显示效果而添加的，可直接忽略。

右边栏点击右上角的 Show the Memory Inspector，会有堆栈信息，并且能直接定位到内存泄漏的代码块。

当然，在 Runtime Issue navigator 中也可以直接看到内存泄漏的地方。
![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/01/2-3.jpeg)

Debug Memory Graph  它能很方便的定位到内存泄漏的地方，但同时它会有误报的情况。例如，当创建 UIButton 对象并将其添加到 UIToolBars 项目数组时，会发现它被识别为内存泄漏，但我们不明白为什么。它也会将一些系统的信息识别为内存泄漏，如下图，定位到了一个叫`UIKeyboardPredictionView`的地方。代码中未用到三方键盘，纯系统键盘唤起。个人理解为系统键盘回收后，其实并没有真正被释放，等到下次唤起键盘时再次使用。我觉得类似这种内存泄漏可以不用管。
![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/01/2-4.jpeg)

如有表述不当，欢迎指出~~
