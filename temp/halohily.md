如何重写自定义对象的 hash 方法
--------
**作者**: [halohily](https://weibo.com/halohily)

hash 是 NSObject 协议中定义的一个属性，也就是说，任何一个 NSObject 的子类都会有 hash 方法（对应属性的 getter，下文称哈希方法）。一般情况下，手动调用自定义对象的哈希方法，会返回当前对象的十进制内存地址，这是哈希方法的父类实现。

什么时候对象的哈希方法会被调用呢？那就是它被加入 NSSet 中，或者作为 NSDictionary 的 key 时。为什么这个时候调用呢？其实不难猜测，是为了利用哈希来加快这些无序集合的检索速度。

当我们需要重写某个类的 isEqual 方法时，配套地便要重写对象的哈希方法，因为被判等的两个对象需要有相同的哈希值，这里可以参考系统对 NSString 的实现，具有相同内容的两个 NSString 的实例 isEqual 方法会返回 true，它们的哈希值也会相同，而它们的内存地址当然是不相同的。此时，对于我们的自定义对象，若依然使用父类的哈希方法实现（返回对象内存地址）自然是不可取的。

那么，该如何正确地重写哈希方法呢？Mattt Thompson 给出了自己的建议：对关键属性的 hash 值进行位或运算作为自己的 hash 值。在我的偶像 @ibireme 的 YYModel 中，他对 yy_modelHash 方法的实现也是采用了这种方案。

参考资料：

- [iOS开发 之 不要告诉我你真的懂isEqual与hash!](https://www.jianshu.com/p/915356e280fc)
- [Implementing Equality and Hashing](https://www.mikeash.com/pyblog/friday-qa-2010-06-18-implementing-equality-and-hashing.html)


