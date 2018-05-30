UIView 的事件透传
--------
**作者**: [Vong_HUST](https://weibo.com/VongLo)

通常我们会遇到这种需求，一个视图除了需要响应子视图的点击事件，其它空白地方希望能将点击事件透传到，比如自定义了一个“导航栏”，除了左右两边按钮，希望其它部分点击能够透传到底下的视图。这个时候我们可以通过复写 hitTest 方法，具体实现如下。

```objc
@implementation PassthroughView

- (UIView *)hitTest:(CGPoint)point withEvent:(UIEvent *)event {
    if (self.hidden || self.alpha < FLT_EPSILON || self.userInteractionEnabled) {
        return [super hitTest:point withEvent:event];
    }
    
    UIView *targetView = nil;
    for (UIView *subview in [[self subviews] reverseObjectEnumerator]) {
        if ((targetView = [subview hitTest:[subview convertPoint:point fromView:self] withEvent:event])) {
            break;
        }
    }
    
    return targetView;
}

@end
```
以上代码即可实现，只响应子视图的事件，而非子视图区域部分的交互事件则透传到响应链中的下一个响应者。
如果你有其它更好方式，也可以分享出来，一起交流下






