Swift 中实现 synchronized
--------
**作者**: [南峰子](https://weibo.com/3321824014)

Objective-C 中的 `@synchronized` 大家都应该很熟悉，用来对一段代码块加锁。不过在 Swift 中没有提供对应的关键字执行相同的操作。所以如果要使用类似的 `synchronized`，则需要自己动手。

以下是 `RxSwift` 中的实现方式：

```c
extension Reactive where Base: AnyObject {
    func synchronized<T>(_ action: () -> T) -> T {
        objc_sync_enter(self.base)
        let result = action()
        objc_sync_exit(self.base)
        return result
    }
}
```

可以看到是通过 `objc_sync_enter` 和 `objc_sync_exit` 来对代码块加锁。而实际上 Objective-C 中的 `@synchronized` 也是基于这两个函数来实现的。如果有兴趣，可以查看一下[源代码](https://github.com/gcc-mirror/gcc/blob/master/libobjc/objc/objc-sync.h)

#### 参考链接

* [关于 @synchronized，这儿比你想知道的还要多](http://yulingtianxia.com/blog/2015/11/01/More-than-you-want-to-know-about-synchronized/)
* [LOCK](https://swifter.tips/lock/)

