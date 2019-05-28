获取其他App的bundle id的几种方法
--------
**作者**: [NotFound--](https://weibo.com/3951595216)

1.使用PP助手或者老版本的itunes下载相应的app的ipa包，改后缀名解压后，获取info.plist，然后打开查看bundle id

2.在Github上下载iOSAppsInfo这个项目，在真机运行这个项目，可以获取真机上所有App的一些相关信息，bundle id，appVersion等，如图一所示，因为项目中的实现依赖于PrivateApi_LSApplicationWorkspace这个类，在iOS 11以后，这个类失效了，所有只能在iOS 10及以下的真机运行，项目地址https://github.com/wujianguo/iOSAppsInfo

3.在Mac上打开控制台应用，连接真机，然后在真机上启动App，便会打印出相关的日志，在输入框中输入"with intent foreground-interactive"对日志进行过滤，可以看到App在冷启动时，SpringBoard进程打印的"Bootstrapping com.tencent.xin with intent foreground-interactive"日志，com.tencent.xin便是微信的bundle id，必须是冷启动才会打印，如图二所示

4.在App Store中搜索相关应用，将其分享到微信，然后使用浏览器打开链接，可以看到网址是这种格式"https://itunes.apple.com/cn/app/%E5%BE%AE%E4%BF%A1/id414478124?mt=8"，其中id414478124是微信的app id，根据这个接口https://itunes.apple.com/lookup?id=414478124>可以获取到App相关的一些信息，有一些ASO网站使用这种原理，获取了大量App的信息，做成一个服务平台了，在里面也可以搜索App名字，然后获得bundle id等信息，例如七麦数据，如图三所示，链接https://www.qimai.cn/app/baseinfo/appid/414478124/country/cn


![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/05/7-1.png?raw=true)
![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/05/7-2.png?raw=true)
![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/05/7-3.png?raw=true)


