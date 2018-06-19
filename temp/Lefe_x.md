提升终端体验的两把厉剑
--------
**作者**: [Lefe_x](https://weibo.com/u/5953150140)

在以往的小集中已介绍过 iTerm2 和 oh-my-zsh 的使用，如果你还不了解这两个工具，不妨到以往的小集中看看他们的作用，包您满意。而今天介绍另外两个提升终端体验的工具。

### tree

如果想在终端查看当前目录的层级结构，不妨了解下 tree，它可以以树状的形式显示当前的目录结构。

安装：
在终端输入：`brew install tree` 。

使用:
在当前目录下，显示树状目录结构：`tree -L 2 -d` 。其中 -L 表示遍历的深度，这里为 2；-d 表示只显示目录。更多参数可以使用 `man tree` 查看。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/06/2-1.jpg)


### Go2Shell

有时候在 Finder 中的目录，想在终端中直接切换到 Finder 当前显示的目录。使用 Go2Shell 即可，一步到位，非常方便。在官网上 [下载](http://zipzapmac.com/Go2Shell)，安装，打开 Finder，按住 command 键，拖动 Go2Shell 的图标到 Finder 菜单，在 Finder 的菜单栏中会显示 Go2Shell 图标。下次想在终端显示当前 Finder 的目录，直接点击图标即可。

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/06/2-2.jpg)
