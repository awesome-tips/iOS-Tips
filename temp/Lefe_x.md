# Diff:/Podfile.lock NO such file or directory

**作者**: [Lefe_x](https://weibo.com/u/5953150140)

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/12/2-1.png)



当 `Pod install` 后，运行项目后发现报错，错误提示如图所示。按提示看了下 `Podfile.lock` 是存在的。试了各种办法，都没有解决（删除 pods 文件夹，重新安装，都不好使）。无奈之下，看了下文件的路径。发现文件路径错了，`XXX/Pods/Pods/Target Support Files/xxx`，发现文件路径多了个 `Pods`。这个路径我并没有设置，是 Pod 自己管理的。最后发现在下图的位置中可以配置路径，把这个路径修改成正确的地址就可以了：



![![](![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/12/2-2.png))