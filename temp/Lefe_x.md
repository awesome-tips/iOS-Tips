NSLog 遇到的问题
--------
**作者**: [Lefe_x](https://weibo.com/u/5953150140)

- 问题一：

有时候 Xcode 控制台突然打印不出信息了，按照下面的步骤操作一下即可解决：

View -> Debug Area -> Activate Console

- 问题二：

有时候打印网络请求的时候，发现打印的信息只显示了部分信息，这时候可以使用 `printf` 来打印。

```
#define LLog( s, ... ) printf("[ %s:(%d) ] %s :%s\n", [[[NSString stringWithUTF8String:__FILE__] lastPathComponent] UTF8String], __LINE__, __PRETTY_FUNCTION__, [[NSString stringWithFormat:(s), ##__VA_ARGS__] UTF8String])
```

使用时直接用 LLog 即可：

```
LLog(@"Hello world");
[ ViewController.m:(22) ] -[ViewController viewDidLoad] :Hello world
```