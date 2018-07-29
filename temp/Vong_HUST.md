Storyboard/Xib 颜色空间的坑
--------
**作者**: [Vong_HUST](https://weibo.com/VongLo)

今天分享一下 `Xcode Interface Builder` 设置背景色的一个坑。从 `Xcode8` 起，`Xib/Storyboard` 里的颜色空间默认从 `Generic RGB` 换成了 `sRGB`，但又不是所有的都会转换，很奇怪。所以当时在适配 `Xcode8` 的时候，颜色空间都统一全局替换了一遍。最近又遇到一次这个坑，在 `Storyboard` 把某个视图背景色从白色更改为 `0xf0f1f2`，然后 run 起来，和其 `superview` (`superview` 的背景色是用代码设置的 `0xf0f1f2`)竟然有一个明显的分割线，所以回想起当时适配时的这个问题，然后取到 `Storyboard` 里面一看，果然是颜色空间被莫名改为了 `Generic RGB`，如图所示。所以手动改变其颜色空间为 `sRGB` 即可。

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/07/14-1.jpg)

参考链接：http://t.cn/RgpFOPg、http://t.cn/ReADdu7



