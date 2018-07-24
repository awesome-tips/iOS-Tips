如何更容易看懂宏
--------
**作者**: [Lefe_x](https://weibo.com/u/5953150140)

相信你和我一样，也遇到过特别难理解的宏定义，比如宏与宏之间嵌套、带参数的宏。我们看个例子(这个宏并不是特别难，但也很绕)：

```
#define JPBOXING_GEN(_name, _prop, _type) \
+ (instancetype)_name:(_type)obj  \
{   \
    JPBoxing *boxing = [[JPBoxing alloc] init]; \
    boxing._prop = obj;   \
    return boxing;  \
}

JPBOXING_GEN(boxObj, obj, id)
```

这个例子看着总是怪怪的，如果把上面的宏转换成实际代码，相信你会很容易看懂。

```
+ (instancetype)boxObj:(id)obj
{
    JPBoxing *boxing = [[JPBoxing alloc] init];
    boxing.obj = obj;
    return boxing;
}
```

其实就是各种参数的替换导致阅读起来比较困难。我们都知道程序经过预处理后就会把宏转换为实际的代码，而 Xcode 为我们提供了对单个文件进行预处理（Produce -> Perform Action -> Preprocess 'xxxx.m'），这样处理后，上面的宏就变成了：

```
+ (instancetype)boxObj:(id)obj { 
   JPBoxing *boxing = [[JPBoxing alloc] init]; 
   boxing.obj = obj; 
   return boxing; 
}
```

经过预处理后和我们手动翻译的结果一样。

