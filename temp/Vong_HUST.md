你还在使用占位 View 吗？
--------
**作者**: [Vong_HUST](https://weibo.com/VongLo)

一种常见的布局场景就是空页面上竖直方向要展示文案和按钮，同时两者要在屏幕中整体居中，这种情况相信大家在日常开发中肯定都会碰到。相信大部分都是使用一个占位视图，然后用 `ImageView` 和 `Label` 把 `View` 撑开，确定其 `size`，然后再让 `View` 放在 `SuperView` 的中心，这样也就满足了上面说的需求。在 iOS9 之前也确实只能这样实现。但是在 iOS9 之后，有了另一种新的方式，那就是使用 `UILayoutGuide`。

区别于 `UIView`，`UILayoutGuide` 继承自 `NSObject`，所以它不会触发渲染，也不会有事件响应和传递机制。它仅仅代表的是一个矩形区域，完全符合我们的要求。它使用起来也非常简单，以上面需求为例，代码如下所示，是不是会简单一些呢？

```objc
self.button = [UIButton new];
self.button.translatesAutoresizingMaskIntoConstraints = NO;
self.button.backgroundColor = [UIColor cyanColor];
[self.button setTitle:@"确定" forState:UIControlStateNormal];
self.label = [UILabel new];
self.label.translatesAutoresizingMaskIntoConstraints = NO;
self.label.text = @"这是一个测试文案";
self.containerGuide = [UILayoutGuide new];
self.containerGuide.identifier = @"占位区域";
    
[self.view addSubview:self.button];
[self.view addSubview:self.label];
[self.view addLayoutGuide:self.containerGuide];
    
[self.containerGuide.centerXAnchor constraintEqualToAnchor:self.view.centerXAnchor].active = YES;
[self.containerGuide.centerYAnchor constraintEqualToAnchor:self.view.centerYAnchor].active = YES;
[self.button.centerXAnchor constraintEqualToAnchor:self.containerGuide.centerXAnchor].active = YES;
[self.label.topAnchor constraintEqualToAnchor:self.containerGuide.topAnchor].active = YES;
[self.label.leftAnchor constraintEqualToAnchor:self.containerGuide.leftAnchor].active = YES;
[self.label.rightAnchor constraintEqualToAnchor:self.containerGuide.rightAnchor].active = YES;
[self.button.topAnchor constraintEqualToAnchor:self.label.bottomAnchor constant:10].active = YES;
[self.button.centerXAnchor constraintEqualToAnchor:self.containerGuide.centerXAnchor].active = YES;
[self.button.bottomAnchor constraintEqualToAnchor:self.containerGuide.bottomAnchor].active = YES;
```

PS 有几个小点可以稍微注意一下：
- UILayoutGuide 无法用 Xib/Storyboard 创建，所以只能代码创建。
- Masonry 目前不支持 UILayoutGuide，但是 SnapKit 是支持的。
- 可以设置 identifier 来方便调试
- 再布局完成后，可以通过 layoutFrame 来获取占位区域的大小
- 不能显式地设置其 owningView，而是要通过 view 的 addLayoutGuide:/removeLayoutGuide: 来间接的设置其 owningView

> 参考链接
>
> [UILayoutGuide](https://medium.com/the-traveled-ios-developers-guide/uilayoutguide-6b3b552b1890)
>
> [Goodbye Spacer Views Hello Layout Guides](https://useyourloaf.com/blog/goodbye-spacer-views-hello-layout-guides/)
