使用__kindof关键字来扩大变量类型限定范围
--------
**作者**: [NotFound--](https://weibo.com/3951595216)

通常来说，如果我们不确定一个变量的类型，可以使用id来代表变量的类型，但是这样做的坏处是编译器在编译时不会对真实类型进行类型检查，如果我们只是想指定一个变量为一个类的类型或其子类的类型，我们可以使用__kindof来表示。例如在图一的代码中，我们定义了一个元素类型为UIView或者UIView子类的数组，如果往数组中添加UIImageView类型的对象，编译器会报错"Incompatible pointer types initializing 'UIImageView *' with an expression of type 'UIView *'"

如图二所示，当我们使用__kindof UIView * 来对数组元素进行修饰，就不会报错了。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/05/4-1.png?raw=true)
![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/05/4-2.png?raw=true)


