关于 UITableView 的 willDisplayCell
-------
**作者**: [这个汤圆没有馅](https://weibo.com/u/6603469503)

willDisplayCell 是 UITableView 的一个代理方法，跟Display相关的方法一共有如下几个。
![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/02/2-1.jpg)

说到 willDisplayCell，很多人会把它和 cellForRowAtIndexPath 做对比。

通过打断点发现，tableview 中先走 cellForRowAtIndexPath 方法，然后再走 willDisplayCell 方法。网上很多人建议，对于数据绑定填充放到 willDisplayCell 中执行。但是通过试验，一般情况下，在 cellForRowAtIndexPath 中进行数据绑定填充，并不会造成卡顿和过度消耗性能的情况。特别复杂的 cell 除外。

另外，willDisplayCell还有一个用处是可以预加载feed流，当滑动到倒数第几个cell时，预先进行网络请求，加载下一页的数据。(来自小伙伴 @NotFound-- 的补充)

willDisplayCell 平时用的最多的场景是自定义 UITableView 分割线。系统默认情况下，UITableView 的分割线左边是没有置顶的。打印它的 inset 可以得到值为 {0, 15, 0, 0}

```
NSLog(@"%@", NSStringFromUIEdgeInsets(tableView.separatorInset));
```

如果想要自定义分割线的长度，例如左右两边都顶格，有两个方法。

- 方法一
```
- (void)viewDidLayoutSubviews {
   if ([_tableView respondsToSelector: @selector(setSeparatorInset:)]) {
      [_tableView setSeparatorInset:UIEdgeInsetsZero];
   }
   if ([_tableView respondsToSelector: @selector(setLayoutMargins:)])  {
      [_tableView setLayoutMargins:UIEdgeInsetsZero];
   }
}
```

- 方法二
```
- (void)tableView:(UITableView *)tableView willDisplayCell:(UITableViewCell *)cell forRowAtIndexPath:(NSIndexPath *)indexPath {
   if ([cell respondsToSelector:@selector(setSeparatorInset:)]) {
      // 可以根据 indexPath 对不同的cell设置不同的分割线长度
      [cell setSeparatorInset:UIEdgeInsetsZero];
   }
   if ([cell respondsToSelector:@selector(setLayoutMargins:)]) {
      [cell setLayoutMargins:UIEdgeInsetsZero];
   }
}
```

方法一只能修改整体分割线，如果要针对不同的 cell 设置不同的分割线，方法二比较适用。以后面对各种 cell 都不需要在自定义时再去拖个 view 画个分割线上去了。

如有表述不当，欢迎指出~~
