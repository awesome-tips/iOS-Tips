Objective-C import 第三方库头文件总结
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

当我们的工程要引用其它第三方开源库时，有以下几种方式：

（1）下载源代码直接拖拽到工程中；

（2）使用 CocoaPods 管理，当开启 `use_frameworks!` 标记时，第三方库会被编译成 `.framework` 引入工程，否则就会编译成 `.a` 静态库；

（3）使用 Carthage 管理，第三方库会被编译成 `.framework` 然后导入工程；

（4）直接下载作者编译好的 `.framework` 导入工程。

但当我们在代码中要 import 第三方库的头文件时，对于这几种情况，写法都不太一样，以 `AFNetworking` 为例，总结如下：

对于（1），只能以 `""` 引号的方式 import，

```objc
#import "AFNetworking.h"
```

对于（2），如果开启 `use_frameworks!`，则将编译成 `.framework` 库，只能以 `<>` 尖括号的方式 import，此外（3）和（4）也是这样：

```objc
#import <AFNetworking/AFNetworking.h>
```

对于（2），如果不开启 `use_frameworks!`，则将编译成 `.a` 库，此时有如下 3 种方式 import，

```objc
#import "AFNetworking.h"
// 或着
#import <AFNetworking.h>
// 或者
#import <AFNetworking/AFNetworking.h>
```

那么问题来了，如果我们在写一个 SDK 或者私有的 Pods 库，需要宿主 App 工程引用某一个第三方库，如上所述，宿主工程有很多方式引用第三方库，这样我们就无法确定我们应该以哪种方式 import 头文件，怎么办呢？这时候我们就可以使用 `__has_include()` 宏来判断。

`__has_include()` 宏接收一个预引入的头文件名称（引号或者尖括号都可以）作为参数，如果该头文件能够被引入则返回 `1`，否则返回 `0`，使用起来如下：

```objc
#if __has_include(<AFNetworking/AFNetworking.h>)
#import <AFNetworking/AFNetworking.h>
#else
#import "AFNetworking.h"
#endif
```
