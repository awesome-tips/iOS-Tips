如何定制一个 UIView 类型控件的出入动画
--------
**作者**: [halohily](https://weibo.com/halohily)

在iOS开发中，自定义的弹层组件非常常见，比如分享框、自定义的  actionSheet 组件等。有的场景下，会选择使用 UIViewController 类型来实现，这时定制这个视图的出现、隐藏动画非常方便。然而，有时候需要选择轻量级的 UIView 类型来实现。这时该怎么定制它的出现、隐藏动画呢？这里提供一个思路：使用 UIView 的 `willMoveToSuperview:` 和 `didMoveToSuperview`这组方法，它们会在 `UIView` 作为subView 被添加到其他 UIView 中时调用。这里需要注意，自身调用 `removeFromSuperview ` 方法时，同样会触发这组方法，只不过这时的参数会是一个 nil。

提供一个例子来说明：一个选择 UIView 类型实现的自定义 actionSheet 的出入动画，交互基本和微信一致。

```objective-c
#pragma mark - show & dismiss
- (void)didMoveToSuperview {
if (self.superview) {
[UIView animateWithDuration:0.35 delay:0 usingSpringWithDamping:0.9 initialSpringVelocity:10 options:UIViewAnimationOptionCurveEaseIn animations:^{
_backgroundControl.alpha = 1;
self.actionSheetTable.frame = CGRectMake(0, SCREEN_HEIGHT - _sheetHeight, SCREEN_WIDTH, _sheetHeight);
} completion:^(BOOL finished) {
[super didMoveToSuperview];
}];
}
}

- (void)hideSelf {
[UIView animateWithDuration:0.35 delay:0 usingSpringWithDamping:0.9 initialSpringVelocity:10 options:UIViewAnimationOptionCurveEaseIn animations:^{
_backgroundControl.alpha = 0;
self.actionSheetTable.frame = CGRectMake(0, SCREEN_HEIGHT, SCREEN_WIDTH, _sheetHeight);
} completion:^(BOOL finished) {
[self removeFromSuperview];
}];
}
```

