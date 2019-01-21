Xcode 工程设置构建版本号自动递增
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

在一个 iOS 工程中，通常有两种“版本号”，即 `Version` 和 `Build`，如图 1 所示：

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/01/8-1.jpg)

* **Version** 为发布版本号，标识应用程序发布的正式版本号，通常为两段式或者三段式，例如：`1.2.1`、`1.0` 等，其 Key 为 `CFBundleShortVersionString`，在 Info.plist 文件中对应 "Bundle versions string, short"；

* **Build** 为构建版本号，标识应用程序构建（编译）的内部版本号，可以有多种方法表示：时间表示（e.g. "20190122080211"）、字母表示（e.g "ABC"）、以及**递增的数字**（e.g. "100"）等。它一般不对外公开，在开发团队内部使用。其 Key 为 `CFBundleVersion`，在 Info.plist 文件中对应 "Bundle version"；

在 App Store 发布应用时，使用的是 “Version” 版本号，在同一个 “Version” 号下， 开发者可以上传不同 “Build” 构建版本。此外，对于 “Build” 号，我们最常使用 “递增的数字” 来表示。

同时，苹果为我们提供了一个 `agvtool` 命令行工具，用于自动增加版本号，具体使用方式如下：

首先，在 Build Settings 配置项中，设置 `Current Project Version` 为选定的值，例如 `100`（可以为整数或浮点数，新工程一般设为 `1`），`agvtool` 命令会根据这个值来递增 “Build” 号。另外需要再选择 `Versioning System` 的值为 `Apple Generic`，如图 2 所示。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/01/8-3.jpg)

然后，在 Build Phases 中，点击 “+” 号，选择 “New Run Script Phase” 添加一个执行脚本，并设置以下脚本代码，如图 3 所示：

>xcrun agvtool next-version -all

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/01/8-2.jpg)

以上，我们在每次编译工程时，“Build” 号就会自动递增加 1 了。

关于 `agvtool` 命令的更多使用方式，可以参考[这里](https://segmentfault.com/a/1190000004678950)。

最后，上述配置在多人开发或者多分支开发时，可能会导致 “Build” 号冲突，因此，我们可以只在日常给测试人员打包的机器上配置就好了。
