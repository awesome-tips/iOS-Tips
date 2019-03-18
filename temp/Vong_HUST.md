少见但实用的 NSPointerFunctions
--------
**作者**: [Vong_HUST](https://weibo.com/VongLo)

最近在看 IGListKit 的相关源码，IGListKit 某些场景下，容器类并没有使用普通的 NSArray、NSSet 或者 NSDictionary，而是使用了 NSMapTable 或者 NSHashTable。而这两个类有两种指定构造器方法：一种是使用 Options 的方式，另一种是使用 PointerFunctions 的方式，如图1、2。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/03/2-1.jpg)

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/03/2-2.jpg)

一般情况下，我们会选择使用 Options 的方式，来实现一些简单的功能，比如弱引用容器中的对象可以传入 NSPointerFunctionsWeakMemory。这里的枚举其实是 NS_OPTIONS 的，他有两种类型，第一种内存管理方式，第二种是唯一性判定方式。

一般情况下，唯一性判定类型默认为 NSPointerFunctionsObjectPersonality，即利用存储对象本身的 hash 和 isEqual 方法来做唯一性判定（去重逻辑），当然系统也提供了一些其它枚举来实现不同的需求。但是这些枚举都无法满足需求时，可以使用 NSPointerFunctions 自定义唯一性判定方式，它提供了两个用来做 hash 计算和 isEqual 判断的函数指针。

IGListAdapterUpdater 也正是利用了这一点，来实现 NSMapTable 中 key 的自定义唯一性判定（去重）方式，如图3所示。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/03/2-3.jpg)

PS：我猜使用 options 的方式内部应该也是根据 options 生成对应的 PointerFunctions，然后再调用 initWithPointerFunctions:，但是如果这样的话，这种方式应该就不是指定构造器了，所以这一点有点好奇。

关于其它更多关于 NSPointerFunctions/NSMapTable 等相关介绍和使用方式可以参考 @saitjr 大佬的[博客](http://www.saitjr.com/ios/nspointerarray-nsmaptable-nshashtable.html)






