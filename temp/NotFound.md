使用requireGestureRecognizerToFail方法来设置手势优先级
--------
**作者**: [NotFound--](https://weibo.com/3951595216)

当我们的某个View既包含单击手势事件，也包含双击手势事件时，如果不做任何处理，当用户进行两次点击操作时，会先先触发单击手势事件一次，然后再触发双手势事件一次，如图一所示。这跟我们想要的结果不一样，我们想要的是连续双击两次时，只响应双击手势事件。要达到这样的效果，我们需要使用requireGestureRecognizerToFail方法对单击手势做一些限制，单击手势只有等双击手势确定不能触发时才会触发，运行结果如图二所示。代码如图三所示，[Demo地址](https://github.com/577528249/SwiftDemo/tree/master/GestureDemo)在这里，大家可以下载下来运行体验一下。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/03/3-2.jpg?raw=true)
![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/03/3-3.jpg?raw=true)
![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/03/3-1.jpg?raw=true)
