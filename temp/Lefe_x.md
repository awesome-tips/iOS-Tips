iOS 你的APP中能藏的住秘密吗？
--------
**作者**: [Lefe_x](https://weibo.com/u/5953150140)

今天 Lefe_x 打算和大家讨论一个非常常见的需求。如果是你，你会咋么做？你会不会使用一种更优雅的方式？

**PM**：我们要实现一个下载音频的功能，下载前需要做这些处理。

- 如果网络异常，直接提示网络异常并退出下载；
- 如果是 4G 网络，需要弹窗提醒用户选择是否继续下载，用户点击下载后进入下载流程，取消后直接退出下载；
- 如果 wifi 直接进入下载；
- 下载时需要获去下载地址，获取到下载地址后，进入下载；
- 下载完成需要刷新 UI；

梳理完逻辑后是这样的：

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/04/6-1.jpg?raw=true)

**我**：这个好办，不一会就写完了，结果是这样的。

```
- (void)downloadCallBack:(void(^)(BOOL isSuccess))callback
{
    if ([self isBadNetwork]) {
        callback(NO);
        return;
    }
    
    if ([self is4GNetwork]) {
        [self showAlert:^(NSInteger index) {
            if (index == 1) {
                [self requestDownloadUrl:^(NSString *url) {
                    [self startDownloadWithURLString:url callback:^(BOOL isSuccess) {
                        callback(YES);
                    }];
                }];
            } else {
                callback(NO);
            }
        }];
    } else {
        [self requestDownloadUrl:^(NSString *url) {
            [self startDownloadWithURLString:url callback:^(BOOL isSuccess) {
                callback(YES);
            }];
        }];
    }
}
```

上面这种写法主要有回调地狱和很多冗余代码，解决这种问题，我们可以使用 Promise 这种异步编程的方式来避免这些问题。如下：

```
- (void)downloadForPromiseCallBack:(void(^)(BOOL isSuccess))callback
{
    // 检查是否可以下载
    AnyPromise *checkPromise = [self checkCanDownloadPromise];
    checkPromise.then(^(){
        // 请求下载地址
        return [self requestUrlPromise];
    }).then(^(NSString *downloadUrl){
        // 开始下载音频
        return [self downloadPromiseWithURLString:downloadUrl];
    }).then(^(){
        // 下载成功
        if (callback) {
            callback(YES);
        }
    }).catch(^(NSError *error){
        // 所有的异常
        callback(NO);
    });
}
```

如果你有好的想法，不防提出来，我们一起讨论哈。

[primise 的使用](https://github.com/lefex/LefexWork/blob/master/blog/iOS/Promise.md)
