延时动画的两种方式对比
--------
**作者**: [Vong_HUST](https://weibo.com/VongLo)

一般情况下，做延时动画有下面常见的两种方式，方式1采用 `UIView` 提供的带延迟参数的类方法，方式2则是使用 `NSObject` 的实例方法来延迟执行某个方法。如下图所示，二者都能在3秒之后做一个时长为0.3秒的渐隐动画，那区别在哪呢？

区别就在于：方式1在执行 `[self dismissWithDelay:3];` 后，`self` 的 `alpha` 会马上变成0（但还是可见的），导致点击事件不响应，方式2则可以正常响应。

原因在于 `UIView` 的动画类方法，只是对 `CoreAnimation` 的封装，在调用了该方法后，相当于给 `self.layer` 加了一个 `opacity` 的 `CABasicAnimation`。`self` 的 `modelLayer` 的透明度（`opacity`）已经被设置成了动画结束时的值（0）（`modelLayer` 的属性和 `view` 的对应属性是一致的，比如这里的 `modelLayer` 的 `opacity` 和 `view` 的 `alpha`），进而导致无法响应点击事件。`presentationLayer` 则是动画过程中近似我们实时看到的内容。

所以一般情况下，如果延时动画操作的是 `alpha` 或者 `hidden` 属性，建议采用 `performSelector:withObject:afterDelay:` 的方式，这样可以在延迟时间未到之前还是能够响应对应的交互。

PS：如果想在延时还未到的时候取消，方式1可以采用 `[self.layer removeAllAnimations]`，方式2可以采用 `[NSObject cancelPreviousPerformRequestsWithTarget:self]` 的方式。

更多关于 `CoreAnimation` 的内容可以查看 [动画解释](https://objccn.io/issue-12-1/) 以及 [iOS-Core-Animation-Advanced-Techniques](https://github.com/AttackOnDobby/iOS-Core-Animation-Advanced-Techniques)。

```objc
// 方式1
- (void)dismissWithDelay:(NSTimeInterval)delay {
    [UIView animateWithDuration:0.3
                          delay:delay
                        options:UIViewAnimationOptionCurveEaseInOut|UIViewAnimationOptionAllowUserInteraction
                     animations:^{
                         self.alpha = 0.f;
                     }
                     completion:^(BOOL finished) {
                         
                     }];
}

[self dismissWithDelay:3];

NSLog(@"%f, %f, %f", self.alpha, self.layer.presentationLayer.opacity, self.layer.modelLayer.opacity);      // ---> 0.000000, 1.000000, 0.000000

// 方式2
- (void)dismiss {
    [UIView animateWithDuration:0.3
                          delay:0
                        options:UIViewAnimationOptionCurveEaseInOut|UIViewAnimationOptionAllowUserInteraction
                     animations:^{
                         self.alpha = 0.f;
                     }
                     completion:^(BOOL finished) {
                         
                     }];
}

[self performSelector:@selector(dismiss) withObject:nil afterDelay:3 inModes:@[NSRunLoopCommonModes]];
NSLog(@"%f, %f, %f", self.alpha, self.layer.presentationLayer.opacity, self.layer.modelLayer.opacity);      // ---> 1.000000, 1.000000, 1.000000
```





