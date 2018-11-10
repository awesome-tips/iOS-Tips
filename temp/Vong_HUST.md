Xcode 10 文件无法关联的 bug
--------
**作者**: [Vong_HUST](https://weibo.com/VongLo)

今天分享一个最近使用 Xcode 遇到的一个坑。相信大家在写（或者看开源库）一些类，都会有一个匹配的 XXX+Private.h、XXX+Subclass.h 这种头文件，里面专门用来放主类的 Extension，主要用途是为了让某些属性和方法模块内“仅模块内（或子类）可见”，这里之所以加双引号是因为在 Objective-C 中所有的公共头文件在任何类中都能被 import 到，所以这里的头文件仅从命名上做一个隔离。Class Extension 的创建也很简单，新建文件，然后选择 Objective-C File，下一步 type 选 Extension 即可。确认后 Xcode 会自动生成一个 YourClass+XXX.h 的文件（XXX 为你新建文件时输入的内容）。但是此时如果使用快捷键（command+ctrl+↑/↓），发现无法和主类关联，即无法跳转到主类的 .h/.m。

这就很难受了，之前版本 Xcode 都是可以的，具体从哪个版本开始不能关联没有去关心，只关心如何解决。恰好最近有看 IGListKit 的相关代码，发现里面也大量使用了这种方式，但是它的 Extension 头文件名都是类似 XXXInternal.h（比如 IGListAdapterInternal.h）这种，而且它是能够使用快捷键在主类和 Extension 之间跳转的，难道是文件名的原因导致的？后面手动把 YourClass+XXX.h 改名为 YourClassXXX.h，然后发现还是不行。但是 build 一下之后，又能像从前那样使用快捷键愉快地在文件间切换了。不过值得一提的是，能用快捷键跳转的仅 XXXX+Private.h 可行（同事的实践），其余的目前试过的都不行。这锅不知道该不该 Xcode 背。

最后如果你也和我有一样的困扰，可以尝试去除文件名中的+号，虽然麻烦了一点，但至少能用了😂。如果你有其他更优雅的解决方案，欢迎分享~


