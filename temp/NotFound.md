使用setViewControllers方法来实现页面跳转
--------
**作者**: [NotFound--](https://weibo.com/3951595216)

当我们对UINavigationcontroller控制器进行Push和Pop操作时，其实是对UINavigationcontroller控制器的子控制器栈ViewControllers进行入栈和出栈操作，有些复杂的页面跳转需求，通过Push和Pop并不能很好实现，有例如我们需要由控制器A跳转到控制器B，B控制器返回时要返回到之前没有创建的控制器C，如果是先Pop再Push，在切换过程中，会显示出控制器A的内容， 不能很好的实现我们的需求，我们可以通过调用setViewControllers 方法来更改UINavigationcontroller的子控制器栈并应用到当前的 UINavigationController来完成页面跳转，具体代码如下：

![](https://user-gold-cdn.xitu.io/2019/2/28/16931c5f3790ad3e?w=1724&h=414&f=png&s=112998)