WWDC 2018 苹果推荐的大图加载方式
--------
**作者**: [halohily](https://weibo.com/halohily)

在 iOS 开发中，图片载入到内存中占用的空间和它的二进制文件大小无关，而是基于图片的尺寸。在 WWDC 2018 中，苹果为我们建议了一种大家平时使用较少的大图加载方式，它的实际占用内存与理论值最为接近。下面是示例代码：

```
func downsample(imageAt imageURL: URL, to pointSize: CGSize, scale: CGFloat) -> UIImage
{
let sourceOpt = [kCGImageSourceShouldCache : false] as CFDictionary
// 其他场景可以用createwithdata (data并未decode,所占内存没那么大),
let source = CGImageSourceCreateWithURL(imageURL as CFURL, sourceOpt)!

let maxDimension = max(pointSize.width, pointSize.height) * scale
let downsampleOpt = [kCGImageSourceCreateThumbnailFromImageAlways : true,
kCGImageSourceShouldCacheImmediately : true ,
kCGImageSourceCreateThumbnailWithTransform : true,
kCGImageSourceThumbnailMaxPixelSize : maxDimension] as CFDictionary
let downsampleImage = CGImageSourceCreateThumbnailAtIndex(source, 0, downsampleOpt)!
return UIImage(cgImage: downsampleImage)
}
```

参考资料：https://juejin.im/post/5b2ddfa7e51d4553156be305


