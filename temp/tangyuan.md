获取App冷启动所耗时长
-------
**作者**: [这个汤圆没有馅](https://weibo.com/u/6603469503)

在App性能优化中，有一块就是启动时间的优化。那如何获取App冷启动所需要的时间呢？

找到 `Edit scheme -> Run -> Auguments` 将环境变量 `DYLD_PRINT_STATISTICS` 设为 1，如下图，然后运行。
![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/05/1-1.jpg)

运行后，能看到控制台打印出日志。
![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/05/1-2.jpg)
可以看到在进入`main()`函数之前，一共耗时396.73ms，并且列举了加载比较慢的文件。

把 `DYLD_PRINT_STATISTICS` 改成 `DYLD_PRINT_STATISTICS_DETAILS` 后运行，能打印出更加详细的日志，如下图。
![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/05/1-3.jpg)

另外推荐一个[代码耗时打点计时器](https://github.com/beiliao-mobile/BLStopwatch)，可以记录SDK加载时间、广告页加载时间、首页加载时间等等。


如有表述不当，欢迎指出~~
