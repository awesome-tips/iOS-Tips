简单聊聊美团 EasyReact
--------
**作者**: [halohily](https://weibo.com/halohily)

一直以来美团都是响应式编程的深度践行者，在美团点评技术团队的博客上有许多关于响应式编程、ReactiveCocoa 的高质量文章。前不久美团开源了自己的响应式编程框架 EasyReact，并且配备了较为完善的文档支持。

在过去 ReactiveCocoa 被视为 iOS 端响应式编程的首选，但由于它选择了函数响应式编程的手段，使得 ReactiveCocoa 的学习路径变得陡峭。然而，响应式编程思想本来是很好理解的，它重在描述数据流动的关系，数据变化触发的动作在数据发生变化之前即被定义好，是一种声明式编程。因此，美团选择了使用有向图这一较为具象的数据结构来描述“数据流动”的过程。就我的个人感受来看，美团官方发布的文章和 EasyReact 自身的文档对于响应式编程理论的阐述非常友好且到位，花几个小时阅读一番收获良多，回头看 ReactiveCocoa 也变得清晰起来。不管你是否打算使用 EasyReact，它的文档及官方的文章都非常值得阅读。

不管 ReactiveCocoa 还是 EasyReact，即使它们都不是响应式编程在 iOS 下的最终答案，响应式编程在客户端这种充满异步的场景下却是切实有意义的。学习一个框架的真正有意义之处在于它背后体现的思想，之前 ReactiveCocoa 也许让很多人望而却步，但我相信 EasyReact 绝对是一个帮助我们开始响应式编程学习之路的优秀教材。

参考资料：
- https://tech.meituan.com/react_programming_framework_easyreact_opensource.html
- https://github.com/meituan/EasyReact

更多知识小集的内容，请查看：https://github.com/iOS-Tips/iOS-tech-set/blob/master/README.md

@南峰子_老驴 @Lefe_x @Vong_HUST @高老师很忙 @故胤道长 @halohily @KANGZUBIN @蒋匿
