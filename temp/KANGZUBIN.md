对于“静态库”和“动态库”的理解总结
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

通常，我们的 Xcode 工程会依赖一些第三方库，包括：.a 静态库（Static Library）和 .framework 动态库（Dynamic Library）。

不过简单地把 .framework 后缀的文件称为“动态库”并不严谨，因为在 iOS/macOS 开发中，framework 又分为**静态 framework** 和 **动态 framework**，区别如下：

* `静态 framework`：可以理解为是 `.a 静态文件` + `.h 公共头文件` + `资源文件` 的集合，本质上与 .a 静态库是一致的；

* `动态 framework`：即真正意义上的动态库，一般包括动态二进制文件、头文件和资源文件等。

对于一个 Static Library 工程，其编译产物为 .a 静态二进制文件 + 公共 .h 头文件；

对于一个 Framework 工程，其编译的最终产物是动态库还是静态库，我们可以通过在 Build Settings -> Linking -> Mach-O Type 中进行选择设置其值为 `Dynamic Library` 或者 `Static Library`。

此外，我们知道，对于一个 Mach-O 二进制文件，不管是 static 还是 dynamic，一般都包含了几种不同的处理器架构（Architectures），例如：i386, x86_64, armv7, armv7s, arm64 等。

Xcode 在编译链接时，对于静态库和动态库的处理方式是不同的。

对于静态库，在链接时（Linking Time），Xcode 会自动筛选出静态库中的不同 architecture 合并到对应处理器架构的主可执行二进制文件中；而在打包归档（Archive）时，Xcode 会自动忽略掉静态库中未用到的 architecture，例如会移除掉 i386, x86_64 等 Mac 上模拟器专用的架构。

而对于动态库，在编译打包时，Xcode 会**直接拷贝**整个动态 framework 文件到最终的 .ipa 包中，只有在 App 真正启动运行时，才会进行动态链接。但是苹果是不允许最终上传到 App Store Connect 后台的 .ipa 文件包含 i386, x86_64 等模拟器架构的，会报 Invalid 错误，所以对于工程中的动态 framework，我们在打 Release 正式包时，一般会通过执行命令或者脚本的方式移除掉这些 Invalid Architectures。

最后，如何在 Xcode 工程中添加这些静态/动态库呢？

对于 “.a 静态库” 和 “静态 framework” ，直接拖拽到工程中，并勾选 `Copy if needed` 选项即可，无需其他设置；而对于添加“动态 framework”，稍微比较麻烦，**我们将在下一条小集介绍几种不同的方法。**

以上，希望对你能有所帮助，不足之处，欢迎指出。
