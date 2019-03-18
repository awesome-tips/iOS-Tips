解决 tableview 刷新闪一下或抖动的问题
-------
**作者**: [这个汤圆没有馅](https://weibo.com/u/6603469503)

我们知道 tableview 刷新有分全局刷新和指定区域刷新。

- 全局刷新 `- (void)reloadData`;

- 指定区域刷新有以下两个方法。

```
- (void)reloadRowsAtIndexPaths:(NSArray<NSIndexPath *> *)indexPaths withRowAnimation:(UITableViewRowAnimation)animation NS_AVAILABLE_IOS(3_0);

- (void)reloadSections:(NSIndexSet *)sections withRowAnimation:(UITableViewRowAnimation)animation NS_AVAILABLE_IOS(3_0);
```
tableview 或者是 collectionview，reload 时默认会有一个隐式的 Fade 动画，有时视觉上会有闪一下的情况。指定区域刷新时，只要将 UITableViewRowAnimation 设为 UITableViewRowAnimationNone 即可取消隐式动画。

那么全局刷新时，该如何取消隐式动画？

方法一：
如果你的 tableview 的行高是根据数据自适应的，那么在设置完 estimatedRowHeight 后，在需要 reloadData 的地方加上。
```
[self.tableView beginUpdates];
[self.tableView endUpdates];
```
(ps: 以上方法用于 tableview 刷新时因预估行高和实际行高不一致情况下抖动的问题，有些人视觉上可能也觉得会闪一下。)

方法二：
使用 UIView 类方法去取消隐式动画，在 block 回调里去 reloadData。该方法对 collectionview 刷新同样有效。
```
+ (void)performWithoutAnimation:(void (NS_NOESCAPE ^)(void))actionsWithoutAnimation NS_AVAILABLE_IOS(7_0);
```
参考链接：https://stackoverflow.com/questions/15196927/reload-uitableview-with-new-data-caused-flickering

如有表述不当，欢迎指出~~
