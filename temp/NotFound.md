使用 strong 而不是 assign 修饰 dispatch 对象
--------
**作者**: NotFound--

当运行系统是在 iOS6 以下时，是需要通过 `dispatch_retain` 和 `dispatch_release` 来管理 `dispatch queue` 的生命周期的，此时应该使用 `assign` 来修饰 `dispatch_queue_t` 类型的对象。在 iOS6 及以后是通过 ARC 来管理 `dispatch queue` 对象的生命周期的，所以应该使用 strong 来修饰 `dispatch_queue_t` 类型的对象。这里以支持 iOS5 系统的 `SDWebImage(version:3.7.6)` 的代码举例：

```objc
#if OS_OBJECT_USE_OBJC
    #define SDDispatchQueueSetterSementics strong
#else
#define SDDispatchQueueSetterSementics assign
#endif

@property (SDDispatchQueueSetterSementics, nonatomic) dispatch_queue_t barrierQueue;
```

`OS_OBJECT_USE_OBJC` 是一个编译器选项，当我们工程里面设置的 `Deployment target` 大于或等于 iOS 6 时，`OS_OBJECT_USE_OBJC` 的值会是 1，否则会是 0。因为我们现在的 app 普遍都是支持到 iOS9 或者 iOS8，所以 `dispatch_queue_t` 类型的对象都是使用 ARC 来进行管理的，我们使用 strong 来修饰就好了。

【示例】

在美团近期开源的 `UI` 渲染框架 `Graver` 中也发现，错误得使用 assign 来修饰 `dispatch_queue_t` 类型的属性（如图一所示），

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/01/7-1.jpg)

对 Graver 框架实际测试时，发现将一个 dispatch_queue_t 类型的局部变量赋值给对 assign 修饰的 `dispatch_queue_t` 后（如图二所示），

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/01/7-2.jpg)

会抛出了野指针异常（如图三所示）。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/01/7-3.jpg)

然后去 github 上搜了一下“`assign dispatch_queue_t`”，发现很多代码也是使用这种错误的写法，所以觉得有必要写个 tip，提醒一下大家。



