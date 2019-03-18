Charles 和 Shadowsocks 如何同时使用
--------
**作者**: [halohily](https://weibo.com/halohily)

Charles 和上网工具客户端 Shadowsocks 是我们日常开发中经常使用的工具，它们都是通过修改代理来实现各自的功能，之前一直以为二者不可同时使用。后来找到了解决办法，分享给大家。

解决的关键点在于 Charles 支持设置外部代理 (External Proxy)，将 Charles 的外部代理设置为 Shadowsocks 的代理，即可实现二者同时使用。

首先找到 Shadowsocks 的代理地址、端口，记录下来，然后将 Shadowsocks 设置为全局模式，最后启动 Charles，点击菜单 - Proxy - External Proxy Settings，勾选 Use external proxy servers，并且填上刚刚的代理地址、端口并保存。

参考资料：http://wangjiawen.farbox.com/skill/shadowsocks-work-with-charles

