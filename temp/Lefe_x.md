你的项目中还用热修复吗？
--------
**作者**: [Lefe_x](https://weibo.com/u/5953150140)

前两天知识小集群里有人讨论关于热修复的问题，对此我非常感兴趣，今天作为一个小集和大家探讨一下。虽然目前苹果严禁带有热修复功能的 APP 上线，一旦发现，将增加审核时间（大约是一周的时间）。苹果主要考虑到了安全问题，避免给自己找事，所以干脆禁用了 JSPatch。但是 JSPatch 使用的 API 并没有违反苹果的规定，他也就没有一个十足的理由拒绝你的 APP 上线。这样就导致还有很多公司在悄悄地用 JSPatch。不过原理基本都是对 JSPatch 进行混淆后使用，当然如果你有能力自己实现一个 JSPatch 也可以。

被拒苹果的拒绝理由大概是这样的：

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/07/1-1.jpeg)

目前我了解到市面上主要通过以下几种方式进行混淆（如果对这个话题感兴趣，后续我们会在【知识小集】gong-zhong-hao 进一步探讨）：

### 方式一：使用官方提供的混淆方式

目前使用官方提供的 JSPatch 服务任然可以过审，据说也是通过静态混淆-宏定义 这中方式。

### 方式二：Bugly（静态混淆-宏定义）

Bugly 提供了热修复功能，它提供了一种对 JSPatch 混淆的方式。在 `BuglyHotfixConfuse_pch.h` 文件中把需要混淆的类名方法名替换掉。有兴趣的读者可以 [下载](https://bugly.qq.com/v2/downloads) 查看详细代码。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/07/1-2.jpeg)

### 方式三：自己混淆

自己混淆当然是最保守的，苹果很难察觉。某天网上爆出一个 ZipArchive 安全漏洞，而这个漏洞的一个条件就是使用了类似 JSPatch 这种可以动态执行脚本的功能，而被爆出的 APP 经查确实使用混淆后 JSPatch，而他们采用的混淆方式也就是自己混淆。所以自己混淆 JSPatch 这条路是通的。自己混淆主要是理解 JSPatch 的原理，换一种方式来实现。


