针对 objc_exception_throw 的实用调试技巧
--------
**作者**: [Vong_HUST](https://weibo.com/VongLo)

相信调试过程中发生崩溃这种事情，大家肯定都遇到过，一般也会给 Xcode 设一个全局共享的异常断点，如图1所示，（如果没有的话，可以设置一波）。当我们调试遇到抛出异常时，Xcode 会自动断点，输出一些关于 Exception 的日志信息。但是有些时候并不见得会输出有用的日志（或者压根就没有日志）只有对应的崩溃栈，如图2所示。

示例中向 NSArray 发了一条无法响应的消息，崩溃后 Xcode 自动断点到了相应的断点位置（这里其实 Xcode 已经在 console 中输入了对应的崩溃信息，因为一时半会不知道该怎么制造 Xcode 不输出日志的环境，所以将就用这个示例来代替下），同时左边也有了对应的崩溃调用栈。我们可以将调用栈切到最上方的 objc_exception_throw，然后在 console 中输入 po $arg1，因为 arg1 代表的是对象本身，在这里就是 NSException，而它又复写了 description 方法，所以对其 print 输出的是对应的崩溃信息。

以上其实我们还可以节省一个步骤，就是编辑一下这个全局异常端点，给起加一个 Debugger Command 的 Action，如图3所示，这样就可以在发生 objc_exception_throw 崩溃的时候，就可以自动输出对应的崩溃信息了，而不用再手动切换到栈顶的 objc_exception_throw 再输一遍 po $arg1。需要明确一点的是，这种方式仅适用于 objc_exception_throw 类型的崩溃（模拟器、真机都适用）。

其他几个有意思的参数值，上面说到 arg1 是当前断点所在方法的接收对象，arg2 是被调用的方法名（在 po 的时候要做一个强转，如 po (SEL)$arg2)，如果有参数则 arg 依次递增。

另外 lldb 的其它更多命令及便捷或扩展的方式，推荐 Facebook 的 [Chisel](https://github.com/facebook/chisel)
个人使用频率最高的就是真机调试动画，放慢动画速度的命令，运行过程中触发任意一个断点，执行 slowanim 即可（默认10倍速慢放，可自行在后面指定慢放倍数，如 slowanim 0.2 就是慢放5倍）。

如果你有更多的小技巧欢迎分享，欢迎交流~

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/01/9-1.gif)
![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/01/9-2.jpg)
![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/01/9-3.jpg)

参考链接：[Xcode: One Weird Debugging Trick That Will Save Your Life](https://www.natashatherobot.com/xcode-debugging-trick/)





