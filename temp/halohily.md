如何正确使用初始化方法的标记宏
--------
**作者**: [halohily](https://weibo.com/halohily)

在 Objective-C 中有 designated 和 secondary 初始化方法的观念。如果一个实例的初始化需要多个参数，那么使用所有参数进行初始化的方法可以作为 designated 初始化方法。而使用一个或多个参数的初始化方法则作为 secondary 初始化方法，并且在对应实现中调用前面的 designated 初始化方法。

在开发时，可以使用 NS_DESIGNATED_INITIALIZER 宏对 designated 初始化方法进行标记，用来向调用者明确，无论其他哪个初始化方法都会通过调用这个方法来实现。对于不想让调用者使用的初始化方法，可以使用 NS_UNAVAILABLE 宏来进行标记禁用。这样一来，Xcode 的自动补全不会索引到该方法，如果强制调用，编译器会报错（但是通过 runtime 还是可以调用的）。

需要注意的是，若为子类指定了一个 NS_DESIGNATED_INITIALIZER 宏标记的初始化方法，**那么在子类中必须重写父类的 designated 初始化方法，该方法的实现是调用子类自身的 designated 初始化方法。在子类自身的  designated 初始化方法的实现中，又需要调用父类的 designated 初始化方法。**这段话比较绕，下面提供一个例子说明。

```objective-c
@interface AwesomeTips : NSObject
//该方法被禁用
- (instancetype)new NS_UNAVAILABLE;
//secondary初始化方法
- (instancetype)initWithName:(NSString *)aName;
//designated初始化方法
- (instancetype)initWithName:(NSString *)aName wish:(NSString *)ourWish NS_DESIGNATED_INITIALIZER;
@end
```

```objective-c
#import "AwesomeTips.h"

@interface AwesomeTips ()
@property (nonatomic, copy) NSString *name;
@property (nonatomic, copy) NSString *wish;
@end

@implementation AwesomeTips

//父类NSObject的designated方法为init，这里必须重写
//否则警告“Method override for the designated initializer of the superclass '-init' not found”
//在其重写实现中，调用子类指定的designated方法，并提供默认参数
- (instancetype)init {
    return [self initWithName:@"知识小集" wish:@"分享知识"];
}

//secondary初始化方法的实现，调用自身的designated方法
- (instancetype)initWithName:(NSString *)aName {
    return [self initWithName:aName wish:@"分享知识"];
}

//自身的designated初始化方法
//需先调用父类的designated方法，而后使用参数赋值
- (instancetype)initWithName:(NSString *)aName wish:(NSString *)ourWish {
    if (self = [super init]) {
        self.name = aName;
        self.wish = ourWish;
    }
    return self;
}

@end
```

