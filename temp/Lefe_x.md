给 如何快速定位哪个 View 出现了约束警告？
--------
**作者**: [Lefe_x](https://weibo.com/u/5953150140)

```
[
	<MASLayoutConstraint:0x1492211d0 UILabel:0x147f56930.right == UITableViewCellContentView:0x147d35140.right - 20>,
	<MASLayoutConstraint:0x147f529a0 UIButton:0x149222b60.right == UITableViewCellContentView:0x147d35140.right - 20>,
	<MASLayoutConstraint:0x147f3dbf0 UILabel:0x147f56930.right == UIButton:0x149222b60.right - 20>
]

Will attempt to recover by breaking constraint 
<MASLayoutConstraint:0x147f529a0 UIButton:0x149222b60.right == UITableViewCellContentView:0x147d35140.right - 20>
```

这种约束警告很常见，每次遇到这种问题即使不解决，页面通常也会正常显示（但不一定都会正常），唯一不好的地方就是控制台会打印出一堆无用的信息，看着头疼。

解决这个问题头疼的一点是不知道具体是那个 View 导致的约束警告，如果知道是那个 View 导致的问题，我想这个问题已经有 80% 的把握能解决，剩下的 20%，看你对自动布局的掌握情况了。

我们把上面的警告换成下面这种方式：

```
[

Label1 距离 Cell1 的右边为 20
<Label1.right == Cell1.right - 20>,

Button1 距离 Cell1 的右边为 20
<Button1.right == Cell1.right - 20>,

Label1 距离 Button1 的右边为 20
<Label1.right == Button1.right - 20>
]

通过移除下面这个约束来纠正约束
<Button1.right == Cell1.right - 20>

```

相信你看完上面的注释已经知道为什么会出现了约束警告，我只是简单的做了个替换操作。

我这里做的就是把 View 的内存地址换成了具体的 View，其实我们可以通过 Xcode 中的 【Debug View Hierarchy】，根据约束警告的内存地址（比如：0x147f56930）找到内存地址对应的 View（）把内存地址粘贴到搜索框，然后和我一样做替换操作，即可解决约束警告。