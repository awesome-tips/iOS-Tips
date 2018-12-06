覆盖父类同名属性
--------
**作者**: [Vong_HUST](https://weibo.com/VongLo)

日常开发中，我们都可能会碰到这种情况，继承系统的某个类，但是想要覆盖父类的某个属性名（大部分情况是 `delegate`、`dataSource`）会发现两个烦人的 `warning`，代码如下所示。

```objc
@protocol VVLTextViewDelegate;

@interface VVLTextView : UITextView

// warning1: Property type 'id<VVLTextViewDelegate>' is incompatible with type 'id<UITextViewDelegate> _Nullable' inherited from 'UITextView'
// warning2: Auto property synthesis will not synthesize property 'delegate'; it will be implemented by its superclass, use @dynamic to acknowledge intention
@property (nonatomic, weak) id<VVLTextViewDelegate> delegate;

@end

@protocol VVLTextViewDelegate <UITextViewDelegate>

- (void)test;

@end

@implementation VVLTextView

@end
```

这个时候除了重命名 `delegate` 之外，还有没有其它操作能够消除警告而且能正常使用呢？答案是肯定的。

根据警告，我们可以把 `delegate` 在 .m 里声明为 `dynamic` 的，然后再把 `protocol` 的定义放到类定义之前，即可实现，代码如下。

```objc
@protocol VVLTextViewDelegate <UITextViewDelegate>

- (void)test;

@end

@interface VVLTextView : UITextView

@property (nonatomic, weak) id<VVLTextViewDelegate> delegate;

@end


@implementation VVLTextView
@dynamic delegate;

@end
```

像系统自带的一些类（比如 `UICollectionView/UITableView`）应该也是用类似方式来实现的吧，我猜。现在也终于想明白为什么系统的大部分协议定义都放在类之前了，应该跟这个有点关系。所以以后有类似需求，可以不需要再去重写一个属性名，然后复写其 `setter` 方法来赋值了。
如有不对之处，欢迎指出，期待你的分享~


