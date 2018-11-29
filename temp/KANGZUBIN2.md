Xcode 工程添加 “动态” Framework 的几种方式
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

在上一条小集，我们分别介绍了 “.a 静态库”、“静态 framework” 和 “动态 framework” 的异同。

接下来我们将介绍一下，如何在 Xcode 工程中添加动态库（Dynamic Library）。

首先我们知道，对于 “.a 静态库” 和 “静态 framework”，直接把相关文件拖拽到工程中，并勾选 Copy if needed 选项即可，无需其它额外的设置；

而对于添加“动态 framework”，稍微比较麻烦，主要有以下几种方式。

PS：我们这里说的“添加动态库”是指第三方动态库，而不是像 UIKit.framework、Foundation.framework 或者 libc++ 等系统自带的动态库，对于它们的依赖添加很简单，直接在 **General -> Linked Frameworks and Libraries** 中点击加号搜索添加即可。

### 手动方式

在 Xcode 工程中选中 app 对应的 target，然后在 **General -> Embedded Binaries** 下点击加号，如图 1，在弹出的窗口选择 Add Other...，最后在 Finder 中选择你要添加的“动态 framework”，并勾选 Copy if needed 即可。需要注意的是，你不能直接在 Finder 中把 .framework 文件拖拽到 Embedded Binaries 中，否则会报错。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/11/4-1.png)

关于手动添加动态库的更多细节以及遇到问题的解决办法，可参考苹果官方的教程：[《Embedding Frameworks In An App》](https://developer.apple.com/library/archive/technotes/tn2435/_index.html)

但是！这种方式看似很方便，其实有个坑是：我们上一条小集提到，一般动态二进制文件都会包含很多处理器架构，例如：i386, x86_64, armv7, armv7s, arm64 等，然后 Xcode 在编译链接时，对动态二进制文件是直接拷贝到 .ipa 包中，并不会像链接静态库那样筛选掉未用到 architecture，而苹果又不允许把包含 i386, x86_64 等模拟器架构的包上传到 App Store Connect 后台，会报错。因此，我们在打 Release 正式包时往往需要手动通过 lipo 命令或者编写脚本移除掉这些 Invalid Architectures。（除非你的开发工程只通过真机来调试，不准备在模拟器里运行，且添加的动态库刚好又不包含 i386、x86_64）

### 使用 Carthage 集成

对于通过 [Carthage](https://github.com/Carthage/Carthage#quick-start) 集成的第三方库，在 Cartfile 文件中添加好依赖后，然后执行 `carthage update` 命令会帮我们生成一个个“动态 framework”，例如 AFNetworking.framework、SDWebImage.framework 等，然后把它们拖拽到工程中，详细可参考 Carthage 的 [Quick Start](https://github.com/Carthage/Carthage#quick-start) 教程。

这里有个关键操作是，需要在 Xcode 工程的 Build Phases 中添加一个执行脚本（New Run Script Phase），并在脚本中执行如下命令：

```shell
/usr/local/bin/carthage copy-frameworks
```

该命令的作用大概就是，在打包拷贝动态库时自动帮我们移除掉其中的 i386、x86_64。

### 使用 CocoaPods 集成

同样地，通过 CocoaPods 集成动态库时，也会在工程中自动帮我们添加一个 Shell 脚本用于做这件事，如图 2 中的 [CP] Embed Pods Frameworks，大家可以自行查阅该 Pods-xxx-frameworks.sh 脚本的内容，里面有个函数 `strip_invalid_archs()` 就是用于在打包时移除无用的处理器架构。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/11/4-2.png)

因此，我们可以把自己开发的或者他人提供的动态 framework，通过 CocoaPods 来集成到工程中：创建一个 Pods 私有 git 库（相信大家已经很熟悉了），在 git 库中添加相关动态 .frameworks 文件，然后其 Podspec 文件的写法大致如图 3 所示，最后在你的工程中 `pod install` 即可。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/11/4-3.png)

最后我们思考一个问题：“静态 framework” 和 “动态 framework” 在使用上似乎也没什么不同，而工程添加 “动态 framework” 又比较繁琐，那么在 iOS/macOS 开发中什么情况下会使用动态库呢？
