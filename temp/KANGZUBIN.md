Objective-C 可变容器对象的初始化方法使用总结
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

最近在 Review Code 时，发现团队中不同成员对一个 `可变字典空对象` 的初始化方式写法都不太一致，主要有以下几种：

```objc
// 第 1 种
NSMutableDictionary *dict1 = [[NSMutableDictionary alloc] init];

// 第 2 种
NSMutableDictionary *dict2 = [NSMutableDictionary new];

// 第 3 种
NSMutableDictionary *dict3 = [NSMutableDictionary dictionary];

// 第 4 种
NSMutableDictionary *dict4 = [NSMutableDictionary dictionaryWithCapacity:10];

// 第 5 种
NSMutableDictionary *dict5 = @{}.mutableCopy;
```

我们知道在 Objective-C 中主要有三大容器，分别是数组、字典、集合，它们各自都对应有可变对象和不可变对象，如：`NSArray`/`NSMutableArray`, `NSDictionary`/`NSMutableDictionary`, `NSSet`/`NSMutableSet`, 我们这里不再赘述它们的区别和使用方式，下面主要以 `NSMutableDictionary` 为例介绍以上几种初始化写法的不同。

第 1 种就是我们常见初始化一个 `NSObject` 对象的写法，其中 `alloc` 为 `NSObject` 的类方法，它用于创建（分配内存）并返回指定类一个的新对象，而 `init` 为 `NSObject` 的实例方法，一般由子类重新实现，用于初始化一个刚创建 (allocated) 的对象。

第 2 种写法，对于 `NSObject` 的 `new` 方法，[苹果文档](https://developer.apple.com/documentation/objectivec/nsobject/1571948-new) 是这么说的：Allocates a new instance of the receiving class, sends it an init message, and returns the initialized object. 因此，它就是 `alloc` 和 `init` 方法的组合，与第 1 种写法是等价的。

第 3 种，[文档描述](https://developer.apple.com/documentation/foundation/nsdictionary/1574180-dictionary?language=objc)：Creates and returns an empty dictionary. 它也是一种快速的初始化写法。在 **ARC** 下，它与 `[[NSMutableDictionary alloc] init]` 是相同的；但在 **MRC** 手动管理内存时，使用 `[[NSMutableDictionary alloc] init]` 创建并初始化对象，后续我们需要手动调用 `release` 方法释放，而 `[NSMutableDictionary dictionary]` 相当于 `[[[NSMutableDictionary alloc] init] autorelease]`，区别在于你不用再调用 release 方法去释放它了。

第 4 种，相当于调用 `[[NSMutableDictionary alloc] initWithCapacity:10]` 方法，它用于创建一个可变字典对象并初始化分配给它足够的内存空间以存储指定长度（10）个内容对象，且当动态添加的数据超过初始化时指定的长度，也会自动增加分配新的内存，所以如果你可以确定要用的可变字典大致的存储个数，推荐使用这种方式。

对于第 5 种，我们知道 `@{}` 字面值相当于创建了一个不可变的 `NSDictionary` 空对象，然后调 NSObject 的 `mutableCopy` 拷贝成一个新的可变对象赋给 `dict5`。

此外，对于 `NSMutableArray` 和 `NSMutableSet` 也有与上述类似的几种不同的初始化写法，不再一一分析。

以上是对可变字典空对象的几种不同初始化写法的简单对比，你习惯用哪一种呢？欢迎留言讨论...

[参考链接1](https://stackoverflow.com/questions/4152322/to-create-an-empty-dictionary-nsmutabledictionary-dictionary-or-nsmutabledi)、[参考链接2](https://stackoverflow.com/questions/11256228/what-is-the-difference-between-class-new-and-class-alloc-init-in-ios/11256290)