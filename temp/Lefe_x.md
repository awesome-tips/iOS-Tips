iOS 内存泄露工具
--------
**作者**: [Lefe_x](https://weibo.com/u/5953150140)

在日常开发中总会遇到内存泄漏的的问题，而排除内存泄漏一般会依靠以下这些工具：

- [MLeaksFinder](http://wereadteam.github.io/2016/02/22/MLeaksFinder/)

这个 WeRead 团队开发的一个内存泄漏检测工具，主要用来检测 UIViewController 和 UIView 中存在的内存泄漏。如果检查到内存泄漏，会弹出 Alert 提示存在内存泄漏。当然，如果某个 UIViewController 是单例，将会误检。

如果检查出内存泄漏，点击 Alert 上的 `Retain Cycle` 将使用 FBRetainCycleDetector 检查存在循环引用的对象。比如：

```
-> DownloadAudioListViewController ,
-> _callblock -> __NSMallocBlock__ 
```

- [FBRetainCycleDetector](https://github.com/facebook/FBRetainCycleDetector)

这是 facebook 开源的一个内存泄漏检测工具，它可以检测出循环引用：

```
FBRetainCycleDetector *detector = [FBRetainCycleDetector new];
[detector addCandidate:myObject];
NSSet *retainCycles = [detector findRetainCycles];
```

检查出的内存泄漏将打印出来：

```
-> DownloadAudioListViewController ,
-> _callblock -> __NSMallocBlock__ 
```

- [Instrument 的 Leak 工具](https://juejin.im/entry/58b105b48ac24728d53e28cf)

Instrument 中的 Leak 工具主要用来“突袭”，开发者定期地使用它来检测内存泄漏。而上面介绍的工具主要在开发过程中即可发现内存问题，提前暴露给开发者。

- [Xcode 中的 Debug Memory Graph]

这个工具主要以图表的形式显示了当前内存的使用情况，可以查看循环引用，如果有内存问题会显示一个叹号。

