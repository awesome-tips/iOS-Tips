iOS 如何调试 WebView
--------
**作者**: [Lefe_x](https://weibo.com/u/5953150140)

目前 iOS 端几乎都会接入 Web 页面，与前端接触也越来越多，如果不了解点前端知识，当出现问题的时候双方沟通起来非常不顺畅，便开始接触前端。我们今天聊聊如何调试 Web 页。当运行 APP 的时候，iOS 端加载 WebView（WKWebView 或 UIWebView ）时可以通过 Mac 自带的 Safari 来调试所显示的页面，其实调试 JSPatch 的时候也是这么用的。

我们来模拟加载 Web 页时的场景，首先需要开启本地的 WebServer，mac 自带 Apache 服务器，我们只需启动这个服务器，即可加载一个网页。

```
// 开启 Apache
sudo apachectl start
```

Apache 开启后，站点的目录在 `/Library/WebServer/Documents` 下，我们把写好的网页放到这个目录下，然后直接可以根据 URL 访问对应的页面，比如在浏览器中输入：`http://电脑ip地址/web/index.html` 即可访问 `index.html` 这个页面。

使用 WKWebView 加载 `index.html` 这个页面，即可调试这个页面，调试前需要做以下两件事：

- 手机端开启Web 检查器：设置 -> 通用 -> Safari -> 高级 -> Web 检查器
- Mac端显示开发菜单：Safari 浏览器默认没有显示“开发”菜单，需要通过：Safari 浏览器  -> 偏好设置 -> 高级 -> 勾选在菜单中显示“开发”设置。

设置完后，当启动 APP ，加载 WKWebView 后即可看到 `index.html` 这个页面。这时即可通过断点进行调试，当然可以查看当前的 HTML 代码，JS 代码，网络情况等。具体如下图所示：

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/05/12-1.jpg)

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/05/12-2.jpg)