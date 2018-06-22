Xcode 设置代码只在 Debug 下起效的几种方式
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

在日常开发中，我们通常会在 Debug 开发模式下写很多测试代码，或者引入一些测试专用的 `.a` 静态库或 `.framework` 动态库，也会通过 CocoaPods 引入一些第三方测试调试工具等；但我们往往不希望这些测试代码和测试用的库（Library/Framework）在 Release 正式包中被引用或导入，如何做到呢？

* `.h/.m` 文件中的测试代码

Xcode 在 Debug 模式下已经自动帮我们定义了宏 `DEBUG=1`，所以我们可以在代码文件中把相关测试代码写在编译预处理命令 `#ifdef DEBUG ... #endif` 中间即可，如下图所示，这也是我们最常见的一种用法。

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/06/3-1.png)

* 测试用的 `.a` 静态库或 `.framework` 动态库

对于通过拖拽的方式直接在工程中添加一些用于测试 `.a` 或者 `.framework` ，我们可以在 Targets - Build Settings - Search Paths 中分别设置 `Library Search Paths` 和 `Framework Search Paths` 这两个选项，如下图所示（其中 libWeChatSDK.a 放在 WeChatSDK 目录中，而 TencentOpenAPI.framework 放在 QQSDK 目录中，假设它们只在测试时会用到），我们可以移除 Release 模式下测试用的 `.a` 或 `.framework` 所在的目录，只在 Debug 下保留，这样在打 Release 包时就不会包含这些库了。

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/06/3-2.png)

* CocoaPods 引入的测试库

对于通过 CocoaPods 方式引入的第三方测试库，就很方便了，我们可以配置 `configurations` 选项它们只在 Debug 下生效，如下图：

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/06/3-3.png)
