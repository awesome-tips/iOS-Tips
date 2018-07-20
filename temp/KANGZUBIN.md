配置 xcodebuild 命令打包支持 Bitcode
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

我们通常会把一些公用的模块抽离出来打成一个 .a 静态库或者 .framework 动态库，然后再嵌入到宿主工程中。

最近我们的 App 工程开启 Bitcode 编译选项后（Enable Bitcode = YES），发现在进行 Archive 归档打 Release 包时，报如下错误，提示说工程使用的 libTestStaticSDK.a 静态库不支持 Bitcode：

```sh
ld: bitcode bundle could not be generated because '/.../TestApp/TestStaticSDKLib/libTestStaticSDK.a(TestStaticSDK.o)' was built without full bitcode. All object files and libraries for bitcode must be generated from Xcode Archive or Install build for architecture armv7
```

但是我们的 libTestStaticSDK 静态库工程的 Build Settings 中同样是有配置开启 Bitcode 的，为什么打出来的 .a 包却不支持 Bitcode 呢？

通过查阅 StackOverflow 我们发现，原来开启 Bitcode 后，在 Xcode 中进行 "Build" 或 "Archive" 时，Xcode 会自动在编译命令后面添加 `-fembed-bitcode` 标识，而如果使用 `xcodebuild` 命令进行打包，则需要手动添加一个 `OTHER_CFLAGS`，如下：

```sh
xcodebuild build OTHER_CFLAGS="-fembed-bitcode" -target libTestStaticSDK ...
```

另外一种解决方案是，在静态库 Xcode 工程的 Build Settings 中，添加一个 "User-Define Setting"，内容为：`'BITCODE_GENERATION_MODE' => 'bitcode'`，如下图所示：

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/07/9-1.png)

这样在使用 `xcodebuild` 命令时就不用添加 `OTHER_CFLAGS="-fembed-bitcode"` 了。

综上，为了通用，我们可以在 `xcodebuild` 命令后同时添加上述两种标识，因此一个完整的静态库打包脚本大致如下（同样适用于 Framework 的打包）：

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/07/9-2.png)

**参考链接**

* [How do I xcodebuild a static library with Bitcode enabled?](https://stackoverflow.com/questions/31486232/how-do-i-xcodebuild-a-static-library-with-bitcode-enabled)

* [iOS 中动/静态库支持 Bitcode 的问题](https://juejin.im/post/5ab311c76fb9a028c42e18a9)
