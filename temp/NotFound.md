如何让多个手势识别器并存
--------
**作者**: [NotFound--](https://weibo.com/3951595216)

如果我们的一个View既支持长按手势，也支持拖动手势，长按时，View背景色变红，拖拽时，View进行位移。如果不进行特殊设置，当用户对View长按0.5s后，View的长按手势会触发，并被长按手势识别器识别，用户的触摸行为就已经被长按手势识别器拦截了，其他手势识别器就没有机会再接触到用户的触摸行为。为了让用户的触摸行为
被多个手势识别器识别，我们可以通过实现手势识别器的代理UIGestureRecognizerDelegate中的shouldRecognizeSimultaneouslyWithGestureRecognizer方法来让用户的触摸行为在被一个手势识别器识别后，还能继续传递，被其他手势识别器处理。这样就达到了我们想要的，长按0.5s后，长按手势识别器触发，View变红，还能继续触发拖动手势，进行位移。使用这种方式来让用户操作被多个手势触发器来处理其实应用得很广泛。例如像那种比较复杂的页面，多个TableView之间进行嵌套，当滑动TableView重叠的部分时，为了让底层的TableView也能接收到用户的滑动操作，也是会使用这种方式来实现。代码如图一，图二所示。[Demo地址](https://github.com/577528249/SwiftDemo/tree/master/GestureDemo)，大家也可以下载下来运行体验一下。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/03/6-1.png?raw=true)
![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/03/6-2.png?raw=true)
