如何优雅地获取 ScrollView 的滚动方向
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

在有些场景，我们可能需要获取 `UIScrollView`（及其子类）的滚动方向来做不同的操作。

我们首先能想到最直观的方法是：用一个变量或属性 lastContentOffset 去保存 scrollView 上次的 `content offset` 值，然后在 `UIScrollView` 的 `scrollViewDidScroll:` delegate 方法中跟 scrollView 当前实时的 `content offset` 做对比来判断滚动方向，代码大致如下：

```objc
// @property (nonatomic, assign) CGFloat lastContentOffset;

- (void)scrollViewDidScroll:(UIScrollView *)scrollView {
    if (self.lastContentOffset > scrollView.contentOffset.y) {
        // 向下滚动
    } else if (self.lastContentOffset < scrollView.contentOffset.y) {
        // 向上滚动
    }
    self.lastContentOffset = scrollView.contentOffset.y;
}
```

今天我们同事在阅读第三方开源代码时，看到一个更简便的方法，同样在 `scrollViewDidScroll:` 方法中，先获取 scrollView 的 `panGestureRecognizer`（拖拽/移动动作）手势，然后把手势滑动的相对偏移在当前 view 上转换成一个 `point`，最后根据 `point` 的 x 或 y 来判断左右/上下滚动方向，代码如下：

```objc
- (void)scrollViewDidScroll:(UIScrollView *)scrollView {
    CGPoint point = [scrollView.panGestureRecognizer translationInView:self.view];
    if (point.y > 0) {
        // 向下滚动
    } else {
        // 向上滚动
    }
}
```

虽然这种方式看似很优雅，可以不用借助额外的变量来完成，但它存在一个问题，如下图所示，我们手指按住屏幕不放，先向上滑动一段距离（从 A -> B，向上）然后改变滑动方向再向下滑动一段距离，（从 B -> A -> C，向下）：

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/04/3-1.png)

但这时候通过第二种方法判断实际得到的结果是：A -> B 向上滚动，B -> A 向上滚动，A -> C 向下滚动，显然，其中 B -> A 的方向判断是错的，应该是向下。

原因在于，上述方法中拖拽手势的相对偏移 `point` 是根据滑动的起始点 A 来进行计算的，所在只要手势停留在起始点 A 之上，不管向上还是向下滑动，它都认为是向上滚动了。

所以这种优雅的方法只适用于 scrollView 一次手势滑动中不改变方向的情况。

参考连接：[Finding the direction of scrolling in a UIScrollView?](https://stackoverflow.com/questions/2543670/finding-the-direction-of-scrolling-in-a-uiscrollview)

