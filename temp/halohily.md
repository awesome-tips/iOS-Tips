# iOS 9 以后通知不再需要手动移除
--------
**作者**: [halohily](https://weibo.com/halohily)

通知 NSNotification 在注册者被回收时需要手动移除，是一直以来的使用准则。原因是在 MRC 时代，通知中心持有的是注册者的 unsafe_unretained 指针，在注册者被回收时若不对通知进行手动移除，则指针指向被回收的内存区域，成为野指针。这时再发送通知，便会造成 crash 。而在 iOS 9 以后，通知中心持有的是注册者的 weak 指针，这时即使不对通知进行手动移除，指针也会在注册者被回收后自动置空。我们知道，向空指针发送消息是不会有问题的。

但是有一个例外。如果用

`- (id <NSObject>)addObserverForName:(nullable NSNotificationName)name object:(nullable id)obj queue:(nullable NSOperationQueue \*)queue usingBlock:(void (^)(NSNotification *note))block API_AVAILABLE(macos(10.6), ios(4.0), watchos(2.0), tvos(9.0));`

这个API来注册通知，可以直接传入 block 类型参数。使用这个API会导致注册者被系统 retain ，因此仍然需要像以前一样手动移除通知，同时这个 block 类型参数也需注意避免循环引用。
