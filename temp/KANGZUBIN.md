Xcode 断点调试时打印变量值报错的问题（编译优化相关）
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

在日常开发中，我们经常会在 Debug 模式下打断点进行调试，并通过 LLDB 的 `po` 命令在控制台打印一些变量的值，以方便排查问题。

今天在 Release 模式下编译运行项目，发现要打印某一变量的值时（`po xxx`），报如下错误：

```
error: Couldn't materialize: couldn't get the value of variable xxx: no location, value may have been optimized out
error: errored out in DoExecute, couldn't PrepareToExecuteJITExpression
```

大致意思是说，`xxx` 的值不存在，可能已经被编译优化了。而且在断点模式下当我们把鼠标的箭头移到某一变量上要进行快速浏览时，发现它们的值都是 `nil`。

查了一下才发现，原来这与 Xcode 工程的编译选项 `Optimization Level` 设置有关，它是指编译器的优化级别，优化后的代码效率比较高，但是可读性比较差，且编译时间更长，它有 6 个选项值如下图：

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/07/5-1.png)

上述每选项值的详细说明可以参考[《Xcode 中 Optimization Level 的设置》](https://www.jianshu.com/p/b38052ee56af)和[《如何加快编译速度》](https://www.zybuluo.com/qidiandasheng/note/587124)两篇文章，我们这里不再赘述。

Xcode 工程的 `Optimization Level` 值在 Debug 模式下默认为 `None [-O0]`，表示编译器不会尝试优化代码，保证调试时输出期望的结果；而在 Release 模式下默认为 `Fastest, Smallest[-Os]`，表示编译器将执行所有优化，且不会增加代码的长度，它是可执行文件占用更少内存的首选方案。

这也是为什么我们在 Release 模式下断点打印变量会报错，因为编译器已经给代码做了优化，它将不在调试时记录变量的值了。

此外，有时候遇到一些线上 Bug 但是在 Debug 调试时却无法复现，我猜有可能会跟编译优化有关，你觉得呢？欢迎留言讨论。
