This block declaration is not a prototype 编译警告处理
--------
**作者**: [南峰子](https://weibo.com/3321824014)

在 Objective-C 中，经常会使用到 block，在声明 block 时，如果没有参数，我们经常是会将参数省略，而不写 void，如

```c
typedef void (^Completion)();
```

特别是在老代码中，这样的情况应该是多数。

而到了 Xcode 9 之后，编译器对这样的代码给出一个警告：

```c
This block declaration is not a prototype
```

即编译器希望你把参数 void 给加上。

最直接的方法当然是声明 block 时，对无参的 block 加上 void，但对于老代码或者是第三方的代码，我想很少有人想去改。如果想过滤这种烦人的提示又想偷懒，那就只能借助编译器配置了，如下图，将 Strict Prototypes 的值设置为 NO，警告就不会再出现了。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/01/5-1.png)


