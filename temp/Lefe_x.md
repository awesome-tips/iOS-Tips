Quick Look Debugging
--------
**作者**: [Lefe_x](https://weibo.com/u/5953150140)

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/05/5-1.png)

上面这张图在开发中你应该经常看到，今天主要介绍快速调试的一个小技巧。有时候想知道某个 image 对象的具体对应的图片长什么样；某条贝塞尔曲线的形状；某个 View 长什么样，它上面有哪些子视图；某个 NSURL 对象是否可以访问等；想快速跳转到沙盒中的某个目录文件下。今天这个小技巧可以帮你解决这些问题。

从第一张图直接点击小眼睛即可预览图片，查看视图，跳转到网页，进入沙盒目录等。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/05/5-2.png)


![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/05/5-3.png)


系统默认支持下面这几种类型：

- 图片： UIImage，UIImageView，和 NSBitmapImageRep 都可以快速查看。
- 颜色： UIColor
- 字符串： NSString 和 NSAttributedString。
- 几何： UIBezierPath 和 NSBezierPath，以及 CGPoint，CGRect，和 CGSize。
- 地区 CLLocation 将显示一个很大的，互动的映射位置，并显示高度和精度的细节。
- URLs： NSURL 将显示 URL 所指的本地或远程的内容。
- 数据： NSData 将漂亮的显示出偏移的十六进制和 ASCII 值。
- 视图： 最后但并非最不重要的，任何 UIView 子类都将在快速查看弹出框中显示其内容，方便极了。


如果想让自定义的类也支持这种快速调试可以重写方法

```
- (id)debugQuickLookObject
{
    // 返回系统支持的类型
    return self.avatarImage;
}
```

[参考](http://nshipster.cn/quick-look-debugging/)