Swift 版本建私有库时需要注意的地方
-------
**作者**: [这个汤圆没有馅](https://weibo.com/u/6603469503)

利用 `cocoapods` 建 `swift` 版本私有库步骤和 `OC` 版本一样，只要把语言 `Objc` 切换成 Swift 即可。一般情况下，`pod lib lint`验证会报警告，如下图，加 `--allow-warnings` 直接忽略即可。

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/07/11-1.jpg)

但是如果私有库里依赖了其他三方库，且该三方库的 swift 版本不一致，则 pod lib lint 会报一堆 error，如下图。

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/07/11-2.jpg)

这个时候就需要根据警告里的提示配置 `.swift-version`。该文件默认情况是不会有的，需要手动添加，如下图。这个时候再次执行 `pod lib lint --allow-warnings` 验证就能通过。

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/07/11-3.jpg)

