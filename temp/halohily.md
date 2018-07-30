用 NSDecimalNumber 处理 iOS 中的货币金额
--------
**作者**: [halohily](https://weibo.com/halohily)

在iOS开发中，经常遇到货币金额的表示与计算，你可能会使用 double 或 float 这样的浮点数，也可能使用 NSString 。无论用哪个，都需要再编写繁琐的精度控制、小数位数控制等代码。其实，苹果为我们提供了一个标准类 NSDecimalNumber 来处理这样的需求。

NSDecimalNumber 是 NSNumber 的子类，它提供了完善的初始化方法。对于令人头疼的金额计算，它还提供了贴心的加、减、乘、除运算方法。在进行这些运算的时候，你还可以通过 NSDecimalNumberHandler 对象来对运算的处理策略进行设置，比如舍入模式的选择，数据溢出、除零等异常情况的处理等。

下次遇到货币金额的需求，不妨了解一下 NSDecimalNumber。

参考资料：

- https://www.jianshu.com/p/ea4da259a062
- https://www.jianshu.com/p/25d24a184016

