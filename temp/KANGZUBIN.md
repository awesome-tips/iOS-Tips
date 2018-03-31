使用 LLDB expression 命令调试动态更新 UI
--------

**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

在日常 App 开发过程中，进行真机或者模拟器调试时，我们可能需要微调一下界面上的 UI 元素，比如色值、位置等来看看效果，但如果每次都通过修改代码，然后重新编译运行会比较麻烦，其实我们可以通过 LLDB 调试命令来动态地修改。

LLDB 的 `expression` 命令用于执行一个表达式，并将表达式返回的结果输出。

我们在 App 运行后，点击 Xcode 调试工具栏的“暂停”按钮，进入命令行调试模式，如图：

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/03/10-1.png)

然后输入如下命令：

```
po [[[UIApplication sharedApplication] keyWindow] recursiveDescription]
```

此时可以看到控制台中输出整个 UI 层级，及每个 UI 元素对象在内存中的地址，如下所示：

```
po [[[UIApplication sharedApplication] keyWindow] recursiveDescription]
<UIWindow: 0x7fd94a616c50; frame = (0 0; 375 667); autoresize = W+H; gestureRecognizers = <NSArray: 0x60c00025b120>; layer = <UIWindowLayer: 0x60c00003f7c0>>
   | <UIView: 0x7fd94a701f90; frame = (0 0; 375 667); autoresize = W+H; layer = <CALayer: 0x60400003b820>>
   |    | <UIView: 0x7fd94a709640; frame = (30 30; 315 120); autoresize = RM+BM; layer = <CALayer: 0x60400003b860>>
   |    | <UIView: 0x7fd94a709a30; frame = (30 180; 315 120); autoresize = RM+BM; layer = <CALayer: 0x60400003bac0>>
```

通过上述输出，我们可以根据内存地址取出某一 UI 元素：

```
expression -- id $testView = (id)0x7fd94a709640
```

然后，修改这个 UI 元素的相关属性：

```
expression -- (void)[$testView setBackgroundColor:[UIColor redColor]]
```

最后，通过下面命令刷新屏幕，你就可以看到 App 中的对应元素发生变化了：

```
expression -- (void)[CATransaction flush]
```

上面只是个例子，其实这个命令不限于说刷新 UI，你甚至可以通过它 Push 打开一个新页面，它相当于可以直接在命令行中执行代码。

另外，我们平时用的 `p` 和 `po` 两个命令，其实也是 `expression` 命令的别名，

`p` 命令等价于 `expression  --` ；
`po` 命令等价于 `expression -O --` ；

关于 expression 命令的更多使用方式，可通过 `help expression` 获取查看。

参考链接：[iOS/OSX 调试：跳舞吧！与LLDB共舞华尔兹](https://segmentfault.com/a/1190000002413758)

写完这个小集后，无意看到 Mac 的 Dock 栏上的 Reveal 应用图标，心想费这些周折干嘛，我为啥不用 Reveal 这个强大的 UI 调试工具来完成这件事请呢？sad...


