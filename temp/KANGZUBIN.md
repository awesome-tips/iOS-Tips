使用 otool 命令查看 App 所使用的动态库
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

在之前的小集中，我们介绍了 iOS 开发中“静态库”和“动态库”库的区别。对于工程中使用到的第三方 “.a 静态库” 或者 “静态 framework”，在编译链接时，就会被合并到主 Mach-O 二进制文件中，而对于“动态 framework”，则会被拷贝到 .ipa 包中的 .app 文件里的 “Frameworks” 文件夹下，在 App 启动时才会被动态链接。

今天我们介绍一下如何查看一个 App 都使用了哪些动态库，包括系统自带的动态库和第三方动态库。

创建一个新工程 “TestApp”，点击编译后，在 Products 文件夹中找到 “TestApp.app” 文件，该文件中包含了当前 App 的 Mach-O 二进制文件 “TestApp”，此时我们在命令行中执行：

```sh
otool -L /path/to/TestApp.app/TestApp
```

即可查看当前 App 需要链接的所有动态库，如图 1 所示：

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/12/3-1.jpg)

可以看出，一个简单的 iOS 工程，至少会链接 `UIKit.framework`、`Foundation.framework`、`libobjc.A.dylib`（Objective-C Runtime 库）、`libSystem.B.dylib`（系统基础库）等动态库；如果工程依赖了其他系统库，也会在这里看到。

此外，如果我们工程添加了一些自己开发的 “动态 framework”，或者通过 `Carthage`、`CocoaPods` 等依赖的第三方 “动态 framework”，通过 otool 命令也能看到，如图 2 红框内所示，非系统自带的动态库的路径以 `@rpath/` 开头。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/12/3-2.jpg)

PS：上述命令也可以用于查看从 App Store 下载的 .ipa 包里 Mach-O 二进制文件所依赖的动态库。

参考链接：http://blog.sunnyxx.com/2014/08/30/objc-pre-main/
