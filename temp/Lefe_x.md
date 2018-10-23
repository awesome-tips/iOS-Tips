TabBar 设置图片可拉伸
--------

**作者**: [Lefe_x](https://weibo.com/u/5953150140)

有时候使用 UITabController 的时候，发现 tabBarItem 上的图片可以连续点击缩小，或者可无限拉长。这时候往往很难找到原因。

最后意外的发现，如果设置了下面这个属性会导致 tabBarItem 上的图片点击时异常。

```objective-c
[self.tabBarItem setImageInsets:UIEdgeInsetsMake(0, 1, 2, 1)];
```

如果你某天发现项目中的 tabBarItem 上的图片点击时显示异常，查看下代码中是否设置了这个属性。



![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/10/2-1.jpg)

