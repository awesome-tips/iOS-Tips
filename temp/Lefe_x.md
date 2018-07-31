给 UIView 添加阴影
--------
**作者**: [Lefe_x](https://weibo.com/u/5953150140)

给 UIView 添加阴影看似简单，如果操作不当也可能会浪费你一些时间。有时候明明添加了阴影可是在 UI 上却没显示出来，尤其涉及到 cell 复用的情况。这里总结几条阴影不显示的原因：

- 是否设置了 masksToBounds 为 YES，设置为 masksToBounds=YES，阴影不显示；
- 设置阴影时 view 的 frame 是否为 CGRectZero，如果是，即使设置阴影后修改 frame 不为 CGRectZero 时，也不会显示阴影；
- 使用自动布局时往往会遇到 frame 为 CGRectZero 时设置阴影无效，这时可以使用 `layoutIfNeeded` 方法；

**通过 layer 设置阴影**

```
// 阴影的颜色
self.imageView.layer.shadowColor = [UIColor blackColor].CGColor;
self.imageView.layer.shadowOpacity = 0.8;
// 阴影的圆角
self.imageView.layer.shadowRadius = 1;
// 阴影偏离的位置 (100, 50) x 方向偏离 100，y 偏离 50 正向，如果是负数正好为相反的方向
self.imageView.layer.shadowOffset = CGSizeMake(3, 4);

```

**通过 shadowPath 设置阴影**

通过这种方式设置的阴影可以自定义阴影的形状，它会使用在 layer 上设置的属性，比如 shadowRadius。

```
UIEdgeInsets edges = UIEdgeInsetsMake(15, 10, 15, 10);
UIBezierPath *path = [UIBezierPath bezierPathWithRect:CGRectMake(-edges.left, -edges.top, CGRectGetWidth(self.imageView.frame) + edges.left + edges.right, CGRectGetHeight(self.imageView.frame) + edges.top + edges.bottom)];
self.imageView.layer.shadowPath = path.CGPath;
```