iOS App 异常捕获相互覆盖问题
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

在开发和维护 App 过程中，我们通常需要去捕获并上报导致 App 崩溃的异常信息，以便于分析，一般我们会使用一些成熟的第三方 SDK，例如 Bugly 或者友盟等。

但如果我们想自己捕获异常信息，做一些相关处理，其实也很简单，苹果为开发者提供了两个异常捕获的 API，如下：

```objc
typedef void NSUncaughtExceptionHandler(NSException *exception);

NSUncaughtExceptionHandler * NSGetUncaughtExceptionHandler(void);
void NSSetUncaughtExceptionHandler(NSUncaughtExceptionHandler *);
```

其中，`NSSetUncaughtExceptionHandler` 函数用于设置异常处理的回调函数，在程序终止前的最后一刻会调用我们设置的回调函数（Handler），进行崩溃日志的记录，代码如下：

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/01/1-1.jpg)

但是，大部分第三方 SDK 也是通过这种方式来收集异常的，当我们通过 `NSSetUncaughtExceptionHandler` 设置异常处理函数时，会覆盖其它 SDK 设置的回调函数，导致它们无法上报统计，反之，也可能出现我们设置的回调函数被其他人覆盖。

那如何解决这种覆盖的问题呢？其实很简单，苹果也为我们提供了 `NSGetUncaughtExceptionHandler` 函数，用于获取之前设置的异常处理函数。

所以，我们可以在调用 `NSSetUncaughtExceptionHandler` 注册异常处理函数之前，先通过 `NSGetUncaughtExceptionHandler` 拿到已有的异常处理函数并保存下来。然后在我们自己的处理函数执行之后，再调用之前保存的处理函数就可以了。 

完整的示例代码如下图所示：

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/01/1-2.jpg)

最后，如果你的 App 接入了多个异常捕获 SDK，而出现了其中一个异常上报不生效的情况，有可能就是因为这个覆盖问题导致的。

参考连接：https://mp.weixin.qq.com/s/vmwj3Hs8JTg3WmB70xhqIQ
