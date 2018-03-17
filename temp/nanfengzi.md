三个打印类信息的私有方法
----

**作者**: [南峰子_老驴](https://weibo.com/touristdiary)

想在 `NSLog` 打印变量的类型信息，无意中找到了看到 `Extended Type Info in Objective-C` 这篇文章，发现了 `NSObject` 的打印类相关信息的三个私有方法，分享一下：

1. `_methodDescription/_shortMethodDescription`：打印接收者的所有实例方法和类方法，包括私有方法；
2. `_ivarDescription`：打印接收者的成员变量，包括类型和值；

我们可以如下使用这几个方法：

```objc
UIView *view = [[UIView alloc] init];
NSLog(@"%@", [view performSelector:@selector(_ivarDescription)]);
```

打印的信息如下所示。

```
<UIView: 0x7fa18a7022d0>:
in UIView:
	_constraintsExceptingSubviewAutoresizingConstraints (NSMutableArray*): nil
	_cachedTraitCollection (UITraitCollection*): nil
	_layer (CALayer*): <CALayer: 0x604000222ac0>
	_layerRetained (CALayer*): <CALayer: 0x604000222ac0>
	_enabledGestures (int): 0
	_gestureRecognizers (NSMutableArray*): nil
	_window (UIWindow*): nil
	_subviewCache (NSArray*): nil
	_templateLayoutView (UIView*): nil
	_charge (float): 0
	_tag (long): 0
	_viewDelegate (UIViewController*): nil
	_backgroundColorSystemColorName (NSString*): nil
	_countOfMotionEffectsInSubtree (unsigned long): 0
	_unsatisfiableConstraintsLoggingSuspensionCount (unsigned long): 0
	_countOfTraitChangeRespondersInDirectSubtree (unsigned long): 1
	_cachedScreenScale (double): 0
	_viewFlags (struct ?): {
		userInteractionDisabled (b1): NO
		implementsDrawRect (b1): NO
		implementsDidScroll (b1): NO
		implementsMouseTracking (b1): NO
		implementsIntrinsicContentSize (b1): NO
		hasBackgroundColor (b1): NO
		......
```

如果对这些信息感兴趣，可以重写类的 `debugDescription()` 方法，在这个方法里面调用上面几个方法。

需要注意一个问题：这些方法在是 `iOS 7+` 中，在 `UIKit` 里面实现的，所以在 `Mac OS` 中用不了，可以尝试建一个控制台程序，看看结果。

参考：[Extended Type Info in Objective-C](http://bou.io/ExtendedTypeInfoInObjC.html)

