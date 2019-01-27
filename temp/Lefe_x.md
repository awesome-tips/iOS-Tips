Command Not Found
----------
**作者**: [Lefe_x](https://weibo.com/u/5953150140)

使用终端命令的时候常会出现`Command Not Found`这个错误，我们今天聊一聊这个错误出现的基本原因，出现这个问题一般因为下面4种原因；

- 输入命令时语法错误，命令行有语法规则，必须按语法规则写；
- 命令并没有安装，有时候安装的时候忽略了错误；
- 命令被删除或破坏了；
- 用户的 `$PATH` 不正确，大部分原因都是这个导致的；

出现前三种错误都比较好解决，第四中错误比较常见，有时候明明安装完成了，却还会报这个错误。命令行程序之所以可以执行是因为它本身是一个可执行程序或者是一个脚本。当在终端中输入命令的时候，操作系统会找对应的可执行文件并执行。操作系统会从环境变量`$PATH`中依次查找可执行文件，直到找到，如果找不到将报 `Command Not Found` 这个错误。

查看我电脑的环境变量  `$PATH` 中包含了（每个路径通过冒号分割）：

```
➜  ~ echo $PATH
/opt/MonkeyDev/bin:/Library/Frameworks/Python.framework/Versions/3.7/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
```

如果报 `Command Not Found` 这个错误，首先通过`echo $PATH`查看环境变量中是否已经存在了可执行文件的路径。如果没有打开`.bash_profile`把可执行文件地绝对路径写进去即可。

```
➜ vi $HOME/.bash_profile
export PATH="$HOME/Library/Android/flutter/bin:$PATH"

// 想让刚配置的 PATH 生效，需要刷新终端
➜  source $HOME/.bash_profile
```

