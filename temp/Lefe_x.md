# Cycript调试第三方APP
--------
**作者**: [Lefe_x](https://weibo.com/u/5953150140)

试想一种场景，我想知道某个第三方 APP 当前页面对应的是哪个 VC，想让某个实例执行某个函数后的效果，打印当前的视图层级，咋么办？

其实使用 Cycript 即可解决这几个问题，Cycript是一门脚本语言，可以把某段代码注入到某个进程中。比如我可以把用 Cycript 编写的代码植入到一个运行的 APP 中，这样 APP 就可以执行注入的代码。下面的测试需要安装 MonkeyDev。 

安装 Cycript 非常简单，直接下载 Cycript，并进入 Cycript 目录下，执行：

```./cycript -r 192.168.10.111:6666```

192.168.10.111:6666 是手机ip地址，6666是默认的端口。这时控制台会有：cy#。


- 1.当前页面对应的是哪个 VC?

获取当前页面是哪个页面时，可以用到响应链的知识。假如SubjectViewController有一个 UITableView， 它的内存地址是 0x106a05c00 ，那么我可以通过下列命令找到当前的VC。

```
cy# [#0x106a05c00 nextResponder]
#"<UIView: 0x105d839d0; frame = (0 0; 375 667); autoresize = W+H; layer = <CALayer: 0x1c0635460>>"
cy# [#0x105d839d0 nextResponder]
#"<SubjectViewController: 0x106a0a200>"
```

- 2.某个实例执行某个函数后的效果？

SubjectViewController 的内存地址是 0x106a0a200，直接执行下面的这条指令，SubjectViewController 的标题会离开变为 Lefe_x。

`cy# [#0x106a0a200 setTitle: @"Lefe_x"]`

- 3.打印当前的视图层级

直接执行下列指令即可。

`[[UIApp keyWindow]recursiveDescription].toString()`


[参考](http://www.cycript.org/)
