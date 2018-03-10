iOS知识小集#「 再谈 timer 之 CFRunLoopTimerRef 」
----
**作者**: [Lefe_x](https://weibo.com/u/5953150140)

阅读本小集可以参考以前的一篇小集「 定时器引发的思考 」

学习 runLoop 的知识时如果有一些使用场景，我想对理解 runLoop 有很大帮助。而 timer 和 runLoop 息息相关。没有 runLoop，timer 不会跑起来。也就是说如果不把 timer 添加到 runLoop 中，timer 就不会被执行。而且 runLoop 和线程是一一对应的，如果非主线程的情况下，只有运行 runLoop 时它才好创建 runLoop

在非主线程中创建一个定时器:

```
[self performSelectorInBackground:@selector(createTimerInOtherThread) withObject:nil];
```

由于函数 createTimerInOtherThread 不在主线程执行，那么可以使用 [NSThread currentThread] 获取当前的线程，使用 CFRunLoopGetCurrent() 获取当前的 runLoop。由于只有主线程的 runLoop 才会开启，而其他线程的 runLoop 需要通过 CFRunLoopRun() 手动开启。

注意这里发现一个诡异的问题。执行 CFRunLoopRun() 后，它后面的代码将在 runLoop 停止后执行，这是因为 runloop 相当于一个循环，循环结束后它后面的代码才会执行。

```
- (void)createTimerInOtherThread
{
CFAllocatorRef allocator = kCFAllocatorDefault;
CFAbsoluteTime fireDate = CFAbsoluteTimeGetCurrent();
CFTimeInterval interval = 2.0;
CFOptionFlags flag = 0;
CFIndex index = 0;

// 定时器的回调
CFRunLoopTimerCallBack callback = lefexTimerAction;

// 定时器上下文
CFRunLoopTimerContext context = {0, (__bridge void *)(self), NULL, NULL, NULL};

// 创建定时器
CFRunLoopTimerRef timer = CFRunLoopTimerCreate(allocator, fireDate, interval, flag, index, callback, &context);

// 获取当前线程的 runlopp，并且开启 runLoop 定时器才能正常执行
threadRunloop = CFRunLoopGetCurrent();
currentThread = [NSThread currentThread];

// 把timer添加到runloop中，timer将会跑起来
CFRunLoopAddTimer(threadRunloop, timer, kCFRunLoopCommonModes);

// 在 run 之后的代码将不会执行
CFRunLoopRun();

// 下面这行打印将在停止 runLoop 后执行。
NSLog(@"runLoop stop");
}
```

定时器跑起来后，它的回调函数将被执行，回调函数将在它所在的 runLoop 对应的线程中执行。如果 timer 被添加到 mainRunLoop 回调函数在主线程中执行。

```
void lefexTimerAction(CFRunLoopTimerRef timer, void *info){
NSLog(@"timer called on thread: %@", [NSThread currentThread]);
}
```

当不在使用 timer 时需要释放掉 timer，而其实也可以直接停止 runloop 的运行 （通过 `CFRunLoopStop(threadRunLoop)）`，timer 也会停止。

```
- (void)invalidTimer:(CFRunLoopTimerRef)timer
{
  if (timer) {
    CFRunLoopTimerInvalidate(timer);
    CFRelease(timer);
    timer = 0;
  }

  if (threadRunloop) {
  // 如果不暂停 runLoop，当前对象不会释放
  CFRunLoopStop(threadRunloop);
  threadRunLoop = NULL;}
}
```