iOS App 启动时间测量
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

当我们的 App 大到一定规模时，就需要开始关注应用的启动时间了，因为这关系到用户体验问题。

我们通常说的启动时间为：用户点击应用图标，显示闪屏页，到该应用首页界面被加载出来的总时间（冷启动），对于 iOS App 来说，启动时间包括两部分：Launch Time = Pre-main Time + Loading Time，如下图所示，其中：

* `Pre-main Time` 指 main 函数执行之前的加载时间，包括 dylib 动态库加载，Mach-O 文件加载，Rebase/Binding，Objective-C Runtime 加载等；

* `Loading Time` 指 main 函数开始执行到 `AppDelegate` 的 `applicationDidBecomeActive:` 回调方法执行（App 被激活）的时间间隔，这个时间包含了的 App 启动时各初始化项的执行时间（一般写在 `application:didFinishLaunchingWithOptions:` 方法里），同时包含首页 UI 被渲染并显示出来的耗时。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/08/2-1.png)

对于第二个时间 Loading Time，比较好测量，我们可以在 main 函数开始执行和 `applicationDidBecomeActive:` 方法执行末尾时分别记录一个时间点，然后计算两者时间差即可，大致如下：

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/08/2-2.png)

而对于第一个时间 Pre-main Time，目前没有比较好的人工测量手段，好在 Xcode 自身提供了一个在控制台打印这些时间的方法：在 Xcode 中 Edit Scheme -> Run -> Auguments 添加环境变量 `DYLD_PRINT_STATISTICS` 并把其值设为 `1`，如下图：

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/08/2-3.png)

这样我们就可以在编译运行工程时，在控制台看到 Total pre-main time 总耗时了，如下图所示，包含 main 函数执行之前各项的加载时间，我们可以多次运行取一下平均值，苹果推荐这个时间应在 400ms 以内。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/08/2-4.png)

综上两步，我们就可计算出一个 iOS App 的启动耗时，并针对性进行优化。

不过，有一个比较滑稽的问题是：目前很多 App 都会在启动后加载一个 3~5 秒的广告页面，给用户的主观感受是这个 App 的启动时间包括了这个广告页的显示时间，于是我们在代码维度做的 App 启动时间优化显得似乎好无意义，sad...

**参考链接**

* [优化 App 的启动时间](http://yulingtianxia.com/blog/2016/10/30/Optimizing-App-Startup-Time/)
* [iOS App 启动性能优化](https://chars.tech/blog/ios-app-launch-time-optimize/)