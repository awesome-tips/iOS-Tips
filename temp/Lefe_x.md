让线程携带数据
----------
**作者**: [Lefe_x](https://weibo.com/u/5953150140)

有时候我们需要在某个线程中传递一些数据， `pthread_t` 或者 `NSThread`提供了相关API。`NSThread`中有一个属性 `threadDictionary`，可以通过这个字典进行数据传递，比如：

```objective-c
[mainThread.threadDictionary setObject:@"Lefex" forKey:@"name"];
```

`pthread_t`通过 `pthread_setspecific` 和 `pthread_getspecific`这两个API进行数据传递：

```objective-c
pthread_key_t thread_key;
pthread_key_create(&thread_key, pthreadKey);
pthread_setspecific(thread_key, "Lefe_x");

char *name = pthread_getspecific(thread_key);
```

 `NSThread`是 `pthread_t` 的一个封装，`pthread_t`是跨平台的。

