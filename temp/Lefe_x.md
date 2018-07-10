一次内存泄漏后的思考
--------
**作者**: [Lefe_x](https://weibo.com/u/5953150140)

最近项目中遇到一个内存泄漏的问题，SecondViewController 这个类在 pop 后并没有执行 dealloc 方法，也就没有被正常被释放。使用内存泄漏工具排查，并没有发现有循环引用的地方，手动查了一下也没发现异常。正在迷茫的时候，突然看到了一个注册监听的地方。实现方式类似下面这样：

```
- (void)dealloc {
    [[Manager sharedInstance] removeObserver:self];
}

- (void)viewDidLoad {
    [super viewDidLoad];
    self.view.backgroundColor = [UIColor whiteColor];
    [[Manager sharedInstance] addObserver:self];
}
```

看到这里你应该已经猜到 SecondViewController 为什么没被释放，它被 Manager 持有了，而 Manager 是一个单例，自然 SecondViewController 也不会被释放，dealloc 方法也不会执行。

这种设计很常见，往往给某个服务注册监听，达到类似通知的效果。如果使用数组保存监听者，监听者将会被数组持有。有同学可能说，可以在 viewDidAppear 注册，在 viewWillDisappear 移除，这样 SecondViewController 就会被释放。但是，这样设计很糟糕，我们尽量不去约束调用者如何调用某个 API。

其实正确的做法是使用一个弱引用容器，我们可以使用 NSHashTable 来保存监听者，这样当监听者释放后，将自动从 NSHashTable 中移除，也不需要主动调用移除监听者的方法（也可以调用，视情况而定）。下面是一个简单的实现，你也可以参考 YYTextKeyboardManager 的实现：

```
_listenerTable = [NSHashTable weakObjectsHashTable];

- (void)addObserver:(NSObject *)obj {
    [self.listenerTable addObject:obj];
}

- (void)removeObserver:(NSObject *)obj {
    [self.listenerTable removeObject:obj];
}
```


