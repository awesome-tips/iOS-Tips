Aspects hook 类方法的正确姿势 
--------
**作者**: [Vong_HUST](https://weibo.com/VongLo)

说起 AOP，相信大家对 Aspects 都有所耳闻，这里不再做原理解读，如果对其原理感兴趣推荐自行阅读源码或者阅读网上大神写的文章。

根据其 README，我们知道它对类方法和实例方法都能 hook，那么 hook 类方法第一感觉，直接用类名去调用 Aspects 提供的分类类方法就好，大概像图1这样。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/01/4-1.png)

运行起来发现，没有并没有打印我们想要输出的内容，反而输出了一段 Aspects 的错误日志 “Aspects: Blog signature <NSMethodSignature: 0x600001a58c00> doesn't match (null).”（我猜 Blog 应该是作者笔误，实际上是 Block）。即我们指定的 block 签名和我们要 hook 的方法签名不一致。查看源码，发现用图1这种方式，Aspects 在获取方法签名的时候，使用的是 [[object class] instanceMethodSignatureForSelector:selector]，这个时候获取到的方法签名是 nil。这是为什么呢？

这里主要是 class 方法和 object_getClass 方法的区别，前者当 object 是类时，则返回本身，当 object 为实例时，则返回类；后者则返回的是 isa 指针的指向，如图2所示。由于这里 object 是类，所以 object.class 返回自身，而自身是没有 selector 对
应的实例方法，所以方法签名返回了 nil。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/01/4-2.png)

因此，如果我们如果要 hook 类方法正确的姿势应该如图3所示。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/01/4-3.png)

即对其 metaClass 进行 hook，因为其实 class 也可以理解成 metaClass 的实例对象。回到上面的例子对 metaClass 调用 class 方法时，返回的是 metaClass 本身，所以 [[object class] instanceMethodSignatureForSelector:selector] 实际上是去 metaClass 的 selector 对应的实例方法，也就是类方法，而 selector 对应的类方法是存在的，所以一切流程正常。这里说的比较绕，推荐一下这张经典的图供（图4）大家参考。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/01/4-4.png)



