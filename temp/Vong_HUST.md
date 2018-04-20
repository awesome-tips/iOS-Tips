CoreData 检索遇到的坑及其解决方式
--------
**作者**: [Vong_HUST](https://weibo.com/VongLo)

项目中有用到 `CoreData` 的同学应该对 [`MagicalRecord`](https://github.com/magicalpanda/MagicalRecord/) 这个库或多或少有一点了解，我们项目中也用到这个库的搜索功能即 `NSManagedObject (MagicalFinders)` 这个分类。

最近遇到一个问题就是两个 `CoreData` 的 `Model`，`Father` 和 `Son`，`Son` 继承自 `Father`。在 `Father` 执行 `MR_findxxx` 等一系列方法时，会把 `Son` 的实例也找出来。一番搜索下来发现有人在 [`MagicalRecord`](https://github.com/magicalpanda/MagicalRecord/) 提了个类似的 [issue](http://t.cn/RmQD2Rj)。然后发现 `NSFetchRequest` 有一个 `includesSubentities` 属性，直接将其设置成 `NO`，即可。代码如下

```objc
+ (NSArray *)findAllOrderBy:(NSString *)orderItem ascending:(BOOL)ascending inContext:(NSManagedObjectContext *)context {
    NSFetchRequest *request = [self requestAllInContext:context];
    [request setIncludesSubentities:NO];
    [request setFetchBatchSize:[self defaultBatchSize]];
    NSSortDescriptor *sortBy = [[NSSortDescriptor alloc] initWithKey:orderItem ascending:ascending];
    [request setSortDescriptors:[NSArray arrayWithObject:sortBy]];
    
    return [self executeFetchRequest:request inContext:context];
}
```

参考链接：

[mr_fetchAllSorted fetches not only the parent entity but also the child entity](http://t.cn/RmQD2Rj)

[NSPredicate that filters out subclass results](http://t.cn/RmQDqYa)
