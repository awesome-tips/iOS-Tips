使用 LLDB bugreport 命令导出 App 运行崩溃日志
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

在日常开发调试 App 过程中，当我们写的代码有 Bug 导致崩溃时，此时我们通常会断点到崩溃的位置，然后查看 Xcode 控制台输出崩溃原因进行解决。

但有些时候我们手头可能有其它的活不能立即进行排查，或者崩溃的是其他同事的代码，需要先把控制台的崩溃日志复制粘贴到其他地方保存起来，过后再看或者告知同事进行解决。强大的 LLDB 调试工具提供了一个 `bugreport` 命令帮我们快速完成导出日志这件事。

例如，有一段数组越界崩溃的代码如下：

```objc
- (void)testBugReport {
    NSArray *testArray = @[@"1", @"2", @"3"];
    NSLog(@"%@", testArray[4]);
}
```

此时在控制台执行如下命令：

```
bugreport unwind --outfile /Users/kangzubin/Desktop/buglog.txt
```

它可以生成一份当前 App 运行状态的完整报告，包含崩溃的调用栈信息，大致如下：

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/04/7-1.png)

另外，我们可以在上述命令后面加一个 `--append-outfile` 修饰符，用于在已有的日志文件中追加新的崩溃日志信息，而不是覆盖。

```
bugreport unwind --outfile <path to output file> --append-outfile
```

参考：[Debugging Swift code with LLDB](https://medium.com/flawless-app-stories/debugging-swift-code-with-lldb-b30c5cf2fd49)
