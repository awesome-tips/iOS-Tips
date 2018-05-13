NSFetchedResultsController 的另一个坑
--------
**作者**: [Vong_HUST](https://weibo.com/VongLo)

之前有分享过 `NSFetchedResultsController` 初始化时设置了 `cacheName` 会导致 iOS10+ 内存泄露的坑，具体可以参考之前这条[微博](https://github.com/awesome-tips/iOS-Tips/blob/master/2017/11.md#nsfetchedresultscontroller%E5%85%BC%E5%AE%B9%E6%80%A7%E9%97%AE%E9%A2%98)。

今天分享另一个坑。用过 `CoreData` 的大家应该比较了解 `NSFetchedResultsController`，这个类设计个人认为是为了和列表视图 `UITableView/UICollectionView` 做绑定，由于它内部有自带 `diff` 算法，结合两个列表类的局部刷新系列方法，可以表现出较好的性能（相对于 `reloadData` 而言），它的 API 回调其实在列表视图中都能找到对应的刷新方式，如图
![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/05/8-1.jpg?raw=true)
![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/05/8-2.jpg?raw=true)

但是有一个坑点是 `controller:didChangeObject: atIndexPath:forChangeType:newIndexPath:` 这个方法的回调时机有时候是错误的，就是一个 `object` 放生改变时，会触发两次回调一次是 `Move` 一次是 `Update`，最终导致数据源不一致导致崩溃，具体可以参考苹果开发者论坛上的这个[讨论](https://forums.developer.apple.com/thread/4999)，讨论中给出了一种解决方案就是把 `Move` 拆成 `Delete` 和 `Insert`，亲测也是可行的。

在用 `NSFetchedResultsController` 时候，你有没有遇到其他问题呢？欢迎一起探讨~






