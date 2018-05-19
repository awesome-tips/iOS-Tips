如何对NSMutableArray进行KVO
--------
**作者**: [halohily](https://weibo.com/halohily)

我们知道，iOS 中 KVO (key-value-observing) 的原理，简单来说就是重写了被观察属性的 set 方法。自然，一般情况下只有通过调用 set 方法对值进行改变才会触发 KVO，直接访问实例变量修改值是不会触发 KVO 的。

对于 NSMutableArray 内容的变化进行观察，是我们比较常见的一个需求。但是在调用它的 addObject、removeObject 系列方法时，并不会触发它自己的 set 方法。所以，对一个可变数组进行观察，在它加减元素时不会收到期望的消息。

那么，该如何实现对 NSMutableArray 的 KVO 呢？官方为我们提供了这个方法` - (NSMutableArray *)mutableArrayValueForKey:(NSString *)key`

像之前一样，为可变数组添加 KVO。在加减元素时，使用这个方法来获取我们要进行操作的可变数组，便可以像普通的属性一样，收到它变化的消息。

举个例子，myItems 是我们要进行 KVO 的一个属性，它的定义如下：

`@property (nonatomic, strong) NSMutableArray *myItems;`

在它进行添加元素时，使用如下方法：

`[[self mutableArrayValueForKey:@"myItems"] addObject:item]; `这样，我们便实现了对 NSMutableArray 的 KVO。


