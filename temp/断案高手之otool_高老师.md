断案高手之otool
------------

前段时间一个朋友遇到了一个问题：每次打包的时候都会把某个方法注释掉，但为什么这次打包出来的效果却不对呢？按照他的思路想来的确百思不解，但秉着“世上没有无缘无故的恨”的原则，我还是想帮他解决一下疑问，我看了他的代码，并没有打Tag，也没有环境区分（`DEBUG`和`RELEASE`区分）😂，就只能用`otool`来试试，方法如下：打开.ipa文件的Unix可执行文件（图1），

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/03/7-1.jpg)


然后在Terminal中输入`otool`的命令，就可以打印出使用了哪些方法（图2）。

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/03/7-2.jpg)

这只是`otool`的一个小用法，这个工具很强大，感兴趣的小伙伴们可以深入了解一下。

不过从这个事情中可以看出来，人的记忆是不可靠的，规范项目才是王道！

