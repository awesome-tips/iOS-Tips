使用 iconfont 替换 Assets 里的图标资源
-------
**作者**: [这个汤圆没有馅](https://weibo.com/u/6603469503)

我们一般对 App 的体积大小会有一定的要求，一般会先从图标资源着手。这边推荐两个压缩图标的网站，不会影响画质，也不会变形或模糊。

* **[Optimizilla](https://imagecompressor.com)**

* **[img.top](https://img.top)**

不过今天主要介绍的是 iconfont，像使用字体一样的使用图标。它可以减小 App 的体积，同时也省去 @2x 和 @3x 图的适配。

> 先在 [阿里巴巴矢量图标库](https://imagecompressor.com) 注册账号，再按照下图的步骤将 UI 设计好的图标下载到本地。每个图标都会对应一个`unicode码`和名称。 这些代码是`&#xXXXX`格式的，但是在 Xcode 中需要转换成`\U0000XXXX`格式的。
![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/03/4-1.jpg)

> 下载完以后，我们会发现文件夹里包含如下图文件。我们只需要将`iconfont.tff`拖入工程中即可。
![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/03/4-2.jpg)

> 为了保证 `iconfont.tff `已导入成功，在`Target--Build Phases--Bundle Resource` 里检查一下。
![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/03/4-3.jpg)

> 打开 `info.plist `文件，添加 `Fonts provided by application `字段。
![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/03/4-4.jpg)

关于使用方法，把之前项目里的 iconfont 整理了一下，[iconfont 封装](https://github.com/TangyuanLiu/TYIconfont)可直接下载使用。可以像设置文字一样设置图标。
```
#define IconfontName(name)  [IconFont iconFontUnicodeWithName:(name)]
#define IconFontSize(value) [IconFont iconFontWithSize:(value)]


label.text = IconfontName(@"mine_logout"); // 这里的“mine_logout”就是图标的名称。
label.font = IconFontSize(64);
label.textColor = [UIColor grayColor];
label.textAlignment = NSTextAlignmentCenter;

// 如果是设置 button 的图标
[btn setTitle:IconfontName(@"chat_voice_normal") forState:(UIControlStateNormal)];
[btn setTitle:IconfontName(@"chat_voice_pressed") forState:(UIControlStateSelected)];
```


如有表述不当，欢迎指出~~
