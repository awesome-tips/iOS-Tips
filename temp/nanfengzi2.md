Objective-C 泛型的协变与逆变
----
**作者**: [南峰子_老驴](https://weibo.com/touristdiary)

Objective-C 引入泛型后，就可能会遇到一个类型转换的问题，如下代码所示：

```objc
@interface Base : NSObject
@end

@implementation Base
@end

@interface Sub : Base
@end

@implementation Sub
@end

@interface Queue<ObjectType> : NSObject

- (void)enqueue:(ObjectType)value;
- (ObjectType)dequeue;

@end

@implementation Queue

- (void)enqueue:(__unused id)value {}
- (id)dequeue { return nil; }

@end

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        Queue<Sub *> *subQueue = [[Queue alloc] init];
        Queue<Base *> *queue = subQueue; // Warning: Incompatible pointer types initializing 'Queue<Base *>' with an expression of type 'Queue<Sub *>'
        
        [queue enqueue:[Sub new]];
    }
    return 0;
}
```

`Sub` 是 `Base` 的子类，如果我将一个 `Queue<Sub *>` 类型的对象指派给 `Queue<Base *>` 对象，则编译器会给出警告。这主要是因为这两个类型实际上是不同的，这种情况下，编译器不会做强制转换。如果希望子类型强制转换为父类型，就涉及到泛型的 “协变(covariant)” 操作。可以在 `Queue` 声明中，对泛型类型加上 `__covariant` 修饰符，表示元素可以接受子类型，如下代码所示：

```objc
@interface Queue<__covariant ObjectType> : NSObject

- (void)enqueue:(ObjectType)value;
- (ObjectType)dequeue;

@end
```

当然，如果想反过来，将 `Queue<Base *>` 类型的对象指派给 `Queue<Sub *>` 类型的对象，可以加上 `__contravariant` 修饰符，称为 “逆变”，表示可以接受父类类型元素。

另外有两点需要注意：

1. 如果声明对象时，不指定泛型类型，直接用 `Queue`，那么可以和 `Queue<Base *>` 、 `Queue<Sub *>` 互相转换；
2. 这两个修饰符不能同时使用；根据 Mike Ash 的描述，还有一个所谓的 “双变性(bivariance)”，即同时接受父类和子类，不过这种情况在 Objective-C 里面不存在；

参考：[Friday Q&A 2015-11-20: Covariance and Contravariance](https://www.mikeash.com/pyblog/friday-qa-2015-11-20-covariance-and-contravariance.html)

