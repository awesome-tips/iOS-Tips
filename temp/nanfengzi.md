## Objective-C中自定义泛型类

最近看 `Facebook` 的 `promise` 源码，看到 `FBLPromise` 类定义为一个泛型类，所以就温习一下。

苹果在2015年就为 Objective-C 增加了泛型，我们现在用 `Array`、`Dictionary`、`Set`、`HashTable` 这些类时，一般都会使用泛型来指定元素的类型。除此之外，我们也可以自定义泛型类。如下代码所示，我们定义了一个 `Queue` 泛型类，并使用了 `ObjectType` 作为泛型类型的占位符。然后 `ObjectType` 就可以用于 `Queue` 类的属性、方法参数、成员变量中，作为这些值的类型。

```objc
@interface Queue<ObjectType> : NSObject

- (void)enqueue:(ObjectType)value;
- (ObjectType)dequeue;

@end

@implementation Queue {
    NSMutableArray *_array;
}

- (instancetype)init {
    self = [super init];
    
    if (self) {
        _array = [[NSMutableArray alloc] init];
    }
    
    return self;
}

- (void)enqueue:(id)value {
    [_array addObject:value];
}

- (id)dequeue {
    if (_array.count > 0) {
        id value = _array[0];
        [_array removeObjectAtIndex:0];
        return value;
    }
    
    return nil;
}

- (NSString *)description {
    return [NSString stringWithFormat:@"The queue is [%@]", _array];
}

@end
```

不过有两点需要注意：

1. `ObjectType` 只能用于类的声明中，即 `@interface` 和 对应的 `@end` 区间内。如果用在类的实现中，即 `@implementation` 中，编译器会报错，提示 “Excepted a type”。因此，在 `@implementation` 中，对应的需要改成 id 。如上代码所示；

2. 在创建对象时，如果指定了泛型类型，那么在具体使用过程中，如果违反了规则，编译器会给出警告，如下代码所示。不过仅此而已，在运行时，你依然可以传递其它类型的值。当然，如果创建对象时没有指定泛型类型，编译器也不会给出警告；

```objc
int main(int argc, const char * argv[]) {
    @autoreleasepool {
        // insert code here...
        NSLog(@"Hello, World!");
        
        Queue<NSNumber *> *queue = [[Queue alloc] init];
        [queue enqueue:@123];
        [queue enqueue:@"abc"];		// Warning: Incompatible pointer types sending 'NSString *' to parameter of type 'NSNumber *'
        
        NSLog(@"%@", queue);
    }
    return 0;
}
```

Objective-C 的泛型是所谓的 `Lightweight Generics`，主要是为了和 Swift 做混编，同时保证了与之前版本的兼容性。

