两种 App 启动连续闪退检测策略
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

当我们要做 App 日志上报时，需要考虑到一种行为：App 在启动时就崩溃闪退了，而且当遇到连续启动闪退（也就是每次打开 App 必崩）时，那几乎是灾难，但更可怕是，如果没有有效的监测手段，我们可能对已发生的这种线上严重问题毫不知情。

WeRead 团队博客的[《iOS 启动连续闪退保护方案》](http://wereadteam.github.io/2016/05/23/GYBootingProtection/)和 MrPeak 老师的[《iOS App 连续闪退时如何上报 crash 日志》](http://mrpeak.cn/blog/ios-instacrash-reporting/)分别介绍了两种简易的如何检测连续闪退的策略，在这里跟大家分享一下。

* 计时器方法

1）App 本地缓存维护一个计数变量，用于表示连续闪退的次数；

2）在启动入口方法 `application:didFinishLaunchingWithOptions:` 里判断 App 之前是否发生过连续闪退，如果有，则启动保护流程，自我修复，日志上报等，否则正常启动。判断的逻辑如下：

3）先取出缓存中的启动闪退计数 crashCount，然后把 crashCount 加 1 并保存；

4）接着使用 `dispatch_after` 方法在 5s 后清零计数，如果 App 活不过 5 秒计数就不会被清零，下次启动就可以读取到；

5）如果发现计数变量 > maxCount，表明 App 连续 maxCount 次连续闪退，启动保护流程，重置计数。

具体的代码如下图所示：

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/07/3-1.png)

这种计数器方法逻辑简单，与原有的代码耦合小。但存在误报可能（用户在启动 App 后又立即 kill 掉，会被误认为是 crash），不过可以通过设置时间阈值或者在 `applicationWillTerminate:` 里标记 App 是被手动 kill 来减少误报。

* 时间数组比对

我们可以在本地保存一个 App 每次启动时间、闪退时间、手动关闭时间的时间数组，然后在 App 启动时根据分析各个时间戳判断是否存在连续闪退（当闪退时间减去启动时间小于阈值 5 秒时，则认为是启动闪退），具体如下：

1）App 每次启动时，记录当前时间 launchTs，写入时间数组；

2）App 每次启动时，通过 crash 采集库，获取上次 crash report 的时间戳 crashTs，写入时间数组；

3）App 在接收到 `UIApplicationWillTerminateNotification` 通知时，记录当前时间戳 terminateTs，写入时间数组。注意，之所以要记录 terminateTs，是为了排除一种特殊情况，即用户启动 App 之后立即手动 kill app。

如果我们正确记录了上面三个时间戳，那么我们可以得到一个与 App crash 行为相关的时间线，如下图：

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/07/3-2.png)

根据各种时间线的行为特征，我们只需要加上时间间隔判断，就能得知是否为连续两次闪退了。注意，如果两个 crashTs 之间如果存在 terminateTs，则不能被认为是连续闪退。

以上，介绍了两种检测 App 是否存在启动连续闪退的策略。

此外，对于连续闪退的保护方案以及连续闪退如何上报日志，请详细阅读开头提到的两篇博文。
