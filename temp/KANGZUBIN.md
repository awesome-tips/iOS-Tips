iPhone 屏幕分辨率终极指南
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

上周，苹果发布了三款新的 iPhone 设备，它们的屏幕数据分别如下：

* iPhone XS: 5.8 英寸，375pt * 812pt (@3x)；
* iPhone XR: 6.1 英寸，414pt * 896pt (@2x)；
* iPhone XS Max: 6.5 英寸，414pt * 896pt (@3x)；

在国外的 PaintCode 网站上，整理了包括从第一代 iPhone 到最新发布的 iPhone XS Max 等所有 iPhone 设备的屏幕数据，包括：开发尺寸（points）、物理尺寸（pixels）以及实际渲染像素、1倍/2倍/3倍模式等，如图 1 所示（建议大图查看更加清晰）。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/09/1-1.png)

原文链接：[The Ultimate Guide To iPhone Resolutions](https://www.paintcodeapp.com/news/ultimate-guide-to-iphone-resolutions)

从图中数据我们可以总结一下几点：

* 5.8 英寸的 iPhone X/XS 与 6.1 英寸的 iPhone XR 和 6.5 英寸的 iPhone XS Max 的**屏幕宽高比**是一致的，约为 `0.462`；

* iPhone X/XS 的屏幕宽度（开发尺寸）与 4.7 英寸的 iPhone 8 相同，都为 375pt，只是在高度上增加了 145pt；

* iPhone XR 和 iPhone XS Max 的屏幕宽度（开发尺寸）与 5.5 英寸 iPhone 8 Plus 相同，都为 414pt，只是在高度上增加了 160pt；

因此，设计师在出图时，仍然可以以 iPhone 8 和 iPhone 8 Plus 的屏幕宽度为基准分别进行 UI 布局，而对于不同高度的屏幕只要在纵向上进行内容延伸即可。

此外，我们发现，对于未进行新屏幕尺寸适配的工程，直接编译，在新设备 iPhone XR 和 iPhone XS Max 上运行，它们是以**放大模式**自动适配的（以 5.8 寸的 iPhone X 屏幕为基准等比例放大），此时在代码中获取到的屏幕宽高都为 375pt * 812pt。

那么如何正确适配新的屏幕尺寸呢？

* 如果你的工程是以 `LaunchScreen.storyboard` 作为启动页，则只需要在 Xcode 10 下重新编译工程即可；

* 如果你的工程是通过配置 `Assets.xcassets` 里的 `LaunchImage` 不同尺寸的启动图片作为启动页，则你需要新增两张 828px * 1792px 和 1242px * 2688px 分辨率的图片，如图 2 所示。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/09/1-2.png)

最后，我们如何在代码中判断当前设备是否为 iPhone X 呢？（这里的 iPhone X 泛指上述介绍的 5.8/6.1/6.5 英寸三种尺寸的带顶部刘海和底部操作条的设备）有一种比较简便的方法就是获取屏幕的高度，判断是否等于 812 或 896，代码如图 3 所示。 

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/09/1-3.png)