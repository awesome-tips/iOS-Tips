再谈 UITableView 的 estimatedRowHeight
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

今天发现之前写的一个基于 `UITableView` 的列表页面存在如下问题：

> 当列表在滑动过程中，特别是往下滑快接近底部时，右侧的滚动条一直在不断地抖动，并且滚动条的长度也在不断地微小变化；另外，当滑动到底部加载下一页数据并 `reloadData` 后，列表的内容会整体跳动往上偏移一段距离。这是什么原因呢？

我们知道，在 iOS 11 发布后，`UITableView` 发生了一些变化，其中对现有项目的界面布局（列表/滚动）影响最大应该是以下两点：

* (1) `UIViewController` 中用于标记是否自动调整 `UIScrollView Insets` 的 `automaticallyAdjustsScrollViewInsets` 属性被宣布弃用，代替的是 `UIScrollView` 自己新增的 `contentInsetAdjustmentBehavior` 属性；

* (2) `UITableView` 的预估 Cell 高度属性 `estimatedRowHeight` 的默认值被改为 `UITableViewAutomaticDimension`（即默认开启），而在 iOS 10 及以前，这个值默认为 0（即默认关闭行高估算）。

对于 (1) 我们这里不再赘述；但是对于 (2) 来说既是福音也是噩耗，它确实解决了一些性能的问题，但也带来了一些令人头痛的问题。

由于 `UITableView` 继承于 `UIScrollView`，而一个 scrollView 能滚动的前提是需要设置它的 `contentSize`。当 tableView 被加载时，会调用 `heightForRowAtIndexPath` 方法计算每个 Cell 的高度，然后相加得到其 `contentSize`，这显然是耗时又耗性能的，尤其是对于那种高度可变化的 Cells 更是如此。

所以为了优化这个问题，提高 `UITableView` 的加载速度（初始化和 `reloadData` 时），苹果引入了 `estimatedRowHeight`，文档描述如下：

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/05/7-1.png)

当开启 `estimatedRowHeight` 时，一个 tableView 被加载后，它的 `contentSize` 的高度通过 `estimatedRowHeight`(默认为44) * Cells 的数量即可得，不需要遍历 `heightForRowAtIndexPath` 获取并相加来计算了，缩短其加载耗时。
 
但是每个 Cell 的真实高度以及 tableView 的真实 `contentSize` 是什么时候计算的呢？正如上述文档所说，**推迟到滑动的时候**，当每个 Cell 将要被显示出来时再计算获取，并实时更新 tableView 的 `contentSize`。

这也解释了我们开头所遇到问题：当 tableView 加载时启用了预估行高，在往下滑动时，下面的 Cells 被不断地被显示出来并更新了 tableView 的 `contentSize`，同时导致右侧的滚动条的高度和位置也要相应更新，产生“抖动”现象。此外，当加载下一页数据并重新 `reloadData` 发生跳动偏移的原因也是类似的。

在 iOS 11 中，`estimatedRowHeight` 默认是开启的，我们可以通过设置 `tableView.estimatedRowHeight = 0` 来禁用。

你在使用 `UITableView` 时遇到过类似的问题吗？你是如何解决的，欢迎留言讨论~ 

参考链接：
* [关于 iOS 11 中 estimatedRowHeight](https://www.jianshu.com/p/3d9c0daddcdb)
* [Apple Docs: estimatedRowHeight](https://developer.apple.com/documentation/uikit/uitableview/1614925-estimatedrowheight?language=objc)
