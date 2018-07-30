vc多层push后回到指定页面的几种方法
-------
**作者**: [这个汤圆没有馅](https://weibo.com/u/6603469503)

场景如下：
RootVC -- > A -- > B -- > C，然后现在要求C直接pop回到A。

方法一：C返回到B的时候写个回调，B接收到回调再自己pop到A，但是这个方法B的页面会闪现一下，用户体验不好，不推荐。

方法二：在B push 到C的时候，直接把B从导航控制器的堆栈中移除，如图一。
![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/07/15-1.jpg)

方法三：写一个UIViewController的catrgory，方法实现如图二。在C的backAct方法中使用，如图三。有的同学可能会怀疑B会不会内存泄露，可以在B中打印dealloc。
![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/07/15-2.jpg)
![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/07/15-3.jpg)

这里比较推荐方法三。不论有多少级的push，只要传入指定页面的类名，都能回到该页面。

