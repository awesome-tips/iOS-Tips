ReactNative从入门到精通(2)-理解iOS开发-FE向
--------

**作者**: [mactive](https://weibo.com/mactive)

## TL;DR
笔者做过几年的iOS-UI工程师(-_-!!), 做过不少类型的App, 后来也玩过RAC之类的流弊架构, 后来转战FE届. 对两种开发都有切身的体会. 总体的感觉是两边互相借鉴和学习, 从MVC,MVVM等开发架构, 到生命周期, 到FRP 等, 很多东西都是相似的. 下面讲点具体的

* iOS开发工具一句话介绍
* iOS的编译过程
* iOS的包管理方案对比
* 对应的 RN-Cli  命令做了什么


## iOS开发工具

![iOS开发三剑客](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/04/2-1.png)


### Xcode: 

* 一个GUI IDE. 可以开发 iOSApp, iWatchApp,  MacApp 甚至 iTVApp
* 可以写代码, debug, 打包和上传至iTunes Store.
* 他不是唯一的开发iOS App的工具, 还有第三方的 AppCode

### XcodeBuild: 

* 一个没有界面的CLI工具, 也能做到编辑和打包. 
* 只要你给他一个bee_shell.xcodeproj 或者 bee_shell.xcworkspace, (一个xcworkspace可以包含多个xcodeproj, 可以理解为公共库单独放在一个project里打包成二进制文件)
* 语言的编译需要用到 LLVM, 一个C/C++/ObjC/Swift 的编译器. debug iOS的时候会用到他的一些命令
* 有了这一系列的命令行工具, 类似webpack 等. 一些开发和打包的自动化才成为可能. 

### iOS Simulator:

* iOS 模拟器, 可以运行你拥有源码的App, 但没有AppStore中安装
* 可以模拟位置和移动, 可以模拟键盘和切换输入法, 可以模拟手势等.不能模拟Push通知
* 可以多开, 就是通知开不同版本的 Simulator

### 注意:

* 开发RN的时候可以不用打开Xcode, 你运行 `react-native run-ios` 的时候其实就是在使用 XcodeBuild 编译并且帮你安装到Simulator中,让后帮你打开Simluator
* Xcode 是一个比较直观的管理你 编译配置文件(也就是你功能文件)的工具而已.


## iOS的编译过程

![iOS编译过程](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/04/2-2.png)

这里我们不展开讲了, 在你按Command+R的时候系统会帮你做很多. 具体的编译过程可以查看[动手玩 LLVM](https://xiaozhuanlan.com/topic/3169254807)

我们说一说个步骤可能会出现的问题:


### 解析:

语法错误:  就想ESLint帮我们做的. 不过iOS的语法要严格许多, 少一个分号也是过不了了. 

而且强类型语言对可变数据和不可变数据也会检查. 基本都是静态检查

### 构建:

这里可能会发现动态链接库的问题, 文件没找到等问题. 因为他存在target的概念, 可能有32位机有64位机.类似我们`ES5`和`ES6`的区别

而且iOS的各个版本之间也有差异. 有点类似FE需要为浏览器兼容性做考虑.

### 打包之后:

这里的报错都是运行时的, 常见数组越界, 内存泄漏, 内存溢出等. 

FE这里很多时候会被接口的错误返回值给坑了. 不过FE表现是卡住,或者功能不能使用.iOS就直接闪退了. 

所以在iOS开发的时候Model层的封装是必须的, 程序的健壮性考虑的也多, 比如异步操作的时候, 线程操作的时候都有些安全的写法. 而且很多组件也要考虑 OOM(内存溢出)的时候手动释放内存等等.

## 包管理方案对比

![cocoaPods vs npm](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/04/2-3.png)


这个就要好好吐槽一下iOS开发了, 苹果爸爸这么有钱都没有把自己的开发人员搞舒服.

iOS上使用CocoaPods来做包管理. 和NPM做下对比

* 没有自己的中心服务器, npm是有自己托管的, 国内大厂还有自己的镜像
* 组件索引使用github托管. 组件本身的code也默认托管在github. 官方网站可以查看文档
* 索引文件必须全量下载到本地 (泪)
* 全包式管理, 会生成*.xcworkspace. 不过后来有了 carthage
* 也有 lock文件, 因为有版本就会有 相应的 lock
* 都可以把组件的源码指向本地地址或者私有的git仓库等.
* (纯吐槽)本身用Ruby写的,  为什么不用 Node.js/Python (吐槽), 而且fastlane还是ruby写的, 难道ruby写不下去了来写iOS.


总体来说还是方便了广大iOS开发者的. 不过整理还是没有NPM好用.

这里值得一提的是 很多 第三方的RN组件, 都选择用NPM来管理 iOS/Android 的源代码. RN本身的安装包也托管在 NPM的cdn上. 然后 iOS项目从 ../node_modules/ 中去加载iOS代码

![Podfile](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/04/2-4.png)


## RN-Cli  命令
* `react-native start`: 启动 localhost的node服务, 提供动态的jsbundle
* `react-native run-ios`: 调用 xcodebuild 并 打开 simulator
* `react-native run-android` 同理

## Q&A

问: 为什么我在Xcode中 Command+R 可以自动打开 NodeServer 和 模拟器

![Build Phase/shell](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/04/2-5.png)

答: Xcode 可以配置在你 Run的时候顺便执行一些 shell脚本. 基本都在 `node_modules/react-native/Packager` 中


## 结语

Xcode只是表象, Xcodebuild才是根本. 如果我们再配合 Microsoft/vscode-react-native. 可以不用打开也不用Xcode和Chrome开心的debug RN程序了.

关于 Debug中的原理和NodeServer的细节可以参考 [深入理解 React Native Debugging
](https://zhuanlan.zhihu.com/p/32547562)



祝你玩得开心😊

