UIViewController 设置导航栏和标签栏不同 title 的问题
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

我们通常会在一个 `UIViewController` 的 `viewDidLoad` 方法中通过 `self.title = xxx` 的方式给一个页面设置其导航栏标题，相信大家对这再熟悉不过了。

如果一个 VC 页面中同时具有 `NavigationBar`（导航栏）和 `TabBar`（标签栏），而且我们又想让这两个地方的标题显示不一致，如下图所示，在首页顶部导航栏标题中显示“知识小集”，而在底部标签栏标题中显示“首页”：

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/07/13-1.jpg)

但是，当我们在 `UITabBarController` 中初始化好上述页面结构后，且设置首页 VC 的 `tabBarItem.title` 为 “首页”，然后在首页 VC 的 `viewDidLoad` 方法中设置 `self.title` 为 “知识小集”，编译运行后我们发现首页底部的标签栏的标题也变成“知识小集”了，而不是刚设置的“首页”。

查了苹果文档中关于 `UIViewController` 中 `title` 属性的定义，有如下一段描述：

>If the view controller has a valid navigation item or tab-bar item, assigning a value to this property updates the title text of those objects.

也就是说，如果一个 VC 同时有导航栏和标签栏，那么当给 `title` 赋值时，会同时修改这两个地方的标题。所以如果我们只想设置导航栏的标题，可以通过 `self.navigationItem.title = xxx` 的方式来实现。

因此，在一个 VC 中设置相关标题简单总结如下：

* **self.navigationItem.title:** 设置 VC 顶部导航栏的标题

* **self.tabBarItem.title:** 设置 VC 底部标签栏的标题

* **self.title:** 同时修改上述两处的标题

这个看似简单的问题，你是否也遇到过呢？欢迎留言讨论。

参考文档：[UIViewController.title](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621364-title?language=objc)
