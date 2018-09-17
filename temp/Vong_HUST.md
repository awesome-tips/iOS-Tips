`instancetype` 和 `id` 的区别
--------
**作者**: [Vong_HUST](https://weibo.com/VongLo)

日常开发中，我们通常会复写各种指定构造器或者自定义指定构造器，一般返回值都会写成 instancetype，但是为什么要写 instancetype 而不是 id 呢？他们之间的区别在哪呢？

我们先来看下代码

```objc
@interface TestObjectA : NSObject
  
+ (id)createObjectA;
- (void)methodA;

@end
  
@interface TestObjectB : NSObject
  
+ (instancetype)createObjectB;
- (void)methodB;

@end
  
// 假设上面4个方法都有实现

[[TestObjectA createObjectA] methodB];      // 无编译错误，但是崩溃
[[TestObjectB createObjectB] methodA];      // 编译报错：No visible @interface for 'TestObjectB' declares the selector 'methodA'

```

从上图可以看出，区别就在于：`instancetype` 能够做到类型检测而 `id` 不行。前者仅可做方法返回值，不能作为参数。但是可能会有人会有疑问，为什么 `- (id)initWithxxx:` 也可以做到类型检测呢？因为类方法只要以 `alloc`、`new` 开头就会有关联返回类型（即类型检测），实例方法只要以 `init`、`autorelease`、`retain`、`self` 开头就会有关联返回类型。具体可以参考[这篇文章](https://clang.llvm.org/docs/LanguageExtensions.html#objective-c-features)

但是 ARC 下实测，实例方法只有 `init` 开头的才有关联返回类型。

如有有不当之处或者你有其它观点，欢迎一起交流探讨~
