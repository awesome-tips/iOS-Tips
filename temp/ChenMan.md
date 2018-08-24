区分SDWebImage的三种缓存
--------
**作者**: [陈满iOS](https://weibo.com/cimer)

SDWebImage的三种缓存分为：内存图片缓存，磁盘图片缓存，内存操作缓存，步骤如下

*   先查看内存图片缓存，内存图片缓存没有，后生成操作，查看磁盘图片缓存
*   磁盘图片缓存有，就加载到内存缓存，没有就下载图片
*   在建立下载操作之前，判断下载操作是否存在
*   默认情况下，下载的图片数据会同时缓存到内存和磁盘中

流程如下图1所示。

![图1](https://upload-images.jianshu.io/upload_images/1283539-a475c67e295bc39e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


> 关于缓存位置

*   内存缓存是通过 NSCache的子类AutoPurgeCache来实现的；
*   磁盘缓存是通过 NSFileManager 来实现文件的存储(默认路径为/Library/Caches/default/com.hackemist.SDWebImageCache.default)，是异步实现的。

> 关于图片下载操作

SDWebImage的大部分工作是由缓存对象SDImageCache和异步下载器管理对象SDWebImageManager来完成的。

SDWebImage的图片下载是由SDWebImageDownloader这个类来实现的，它是一个异步下载管理器，下载过程中增加了对图片加载做了优化的处理。而真正实现图片下载的是自定义的一个Operation操作，将该操作加入到下载管理器的操作队列downloadQueue中，Operation操作依赖系统提供的NSURLConnection类实现图片的下载。

> 关于SDWebImageManager与SDWebImageDownloader的分工
- SDWebImageManager提供的关键API是loadImageWithURL开头的，负责加载的，加载load这个词跟下载download不同，比它更广，加载负责管理下载之前的操作：

管理下载操作的开始和取消
下载之前查询图片的内存缓存和磁盘缓存
下载之后保存图片到内存缓存和磁盘缓存
返回一个操作对象给上级对象UIImageView+WebCache作为操作缓存数组属性中去

- SDWebImageDownloader提供的关键API是downloadImageWithURL开头的，可见它仅仅管理下载的操作，没有缓存的管理功能。




