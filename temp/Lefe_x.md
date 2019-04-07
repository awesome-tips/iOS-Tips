查看App中的字符串
----------
**作者**: [Lefe_x](https://weibo.com/u/5953150140)

有时候我们想查看App中的一些字符串的值，比如下面的代码：

```objective-c
static NSString *kName = @"name lefex";
static const NSString *kNameConst = @"name lefex const";

NSString *name = [NSString stringWithFormat:@"%@ - %@", kName, kNameConst];
NSLog(@"name --- %@", name);

- (void)lefex {
    NSLog(@"Hello lefex");
}

__attribute__((constructor(101)))
void before101() {
    NSLog(@"before101");
}
```

使用命令`xcrun otool -v -s __TEXT __cstring ~/Desktop/Mach-ODemo`，可以看到控制台输出了上面代码中定义的字符串。这条命令的作用是查看可执行文件`__TEXT`段内名为`__cstring`的内容，`~/Desktop/Mach-ODemo`是可执行文件的路径，获取可执行文件的方式非常多，可以查看以往的小集。如果你只是想看看效果，可以从自己项目的ipa文件中找到可执行文件。:

```objective-c
/Users/lefex/Desktop/Mach-ODemo (architecture armv7):
Contents of (__TEXT,__cstring) section
0000b67d  Hello lefex
0000b689  before101
0000b693  before103
0000b69d  before102
0000b6a7  Hello destory
0000b6b5  %@
0000b6b8  Hello load
0000b6c3  name lefex
0000b6ce  name lefex const
```

这是目前我觉得最简单的一种方式。如果代码中有比较铭感的内容，切记要经过特殊处理。可执行文件中还有好多有趣的内容。感兴趣的可以深入了解可执行文件究竟都保存了哪些信息。