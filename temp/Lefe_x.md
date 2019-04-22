获取UIImage时的时间差异对比
----------
**作者**: [Lefe_x](https://weibo.com/u/5953150140)

对比2组数据，数据由iPhoneX模拟器采集，下面这两组数据不同操作系统可能数据有所差别。整体来说从aseet中获取图片性能更优，在不同设备下 ` [UIImage imageNamed:inBundle:compatibleWithTraitCollection:]` 获取图片可能优于 ` [UIImage imageNamed:]`。希望对你有所启发。知识小集上次发布了一个这方面的文章，可以参考一下。

其它设备采集数据来源于 https://forums.developer.apple.com/thread/17888。

> Here are the timings I got on an iPhone 6 running iOS 9.0.2.  This is loading 4 small images 100 times in a loop:
>
>  From Asset Catalog with [UIImage imageNamed:]   0.81
>
> From Asset Catalog with [UIImage imageNamed:inBundle:compatibleWithTraitCollection:]   0.21
>
> From Bundle with [UIImage imageNamed:]   0.35
>
> From Bundle with [UIImage imageNamed:inBundle:compatibleWithTraitCollection:]    0.1



「从 bundle 中获取图」

使用`imageNamed:`获取图，耗时为 81ms;

```objective-c
int64_t imageBefortTime = [[NSDate date] timeIntervalSince1970] * 1000;
UIImage *image = [UIImage imageNamed:@"lefe"];
int64_t imageAfterTime = [[NSDate date] timeIntervalSince1970] * 1000;
NSLog(@"imageNamed: %@-%@", image, @(imageAfterTime - imageBefortTime));
```

```
imageNamed: image:<UIImage: 0x60000103e6f0>, {1500, 1500}, time=81
```

采用 `imageNamed:inBundle:compatibleWithTraitCollection:`从bundle中获取图片，耗时 144ms：

```objective-c
int64_t imageAssetBefortTime = [[NSDate date] timeIntervalSince1970] * 1000;
UIImage *image2 = [UIImage imageNamed:@"lefe" inBundle:nil compatibleWithTraitCollection:nil];
int64_t imageAssetAfterTime = [[NSDate date] timeIntervalSince1970] * 1000;
NSLog(@"inBundle: %@-%@", image2, @(imageAssetBefortTime - imageAssetAfterTime));
```

```
inBundle: image= <UIImage: 0x6000034b7170>, {1500, 1500}, time = 144
```

「从 asset 中获取图」

采用 `imageNamed:`从asset中获取图片，耗时 3ms：

```
int64_t imageBefortTime = [[NSDate date] timeIntervalSince1970] * 1000;
UIImage *image = [UIImage imageNamed:@"lefe_asset"];
int64_t imageAfterTime = [[NSDate date] timeIntervalSince1970] * 1000;
NSLog(@"imageNamed: image:%@, time=%@", image, @(imageAfterTime - imageBefortTime));
```

```
 imageNamed: image:<UIImage: 0x60000012a0d0>, {750, 750}, time=3
```

采用 `imageNamed:inBundle:compatibleWithTraitCollection:`从asset中获取图片，耗时 13ms：

```objective-c
    int64_t imageAssetBefortTime = [[NSDate date] timeIntervalSince1970] * 1000;
    UIImage *image2 = [UIImage imageNamed:@"lefe_asset" inBundle:nil compatibleWithTraitCollection:nil];
    int64_t imageAssetAfterTime = [[NSDate date] timeIntervalSince1970] * 1000;
    NSLog(@"inBundle: %@-%@", image2, @(imageAssetBefortTime - imageAssetAfterTime));
```

```
inBundle: image= <UIImage: 0x6000038bd960>, {750, 750}, time = 13
```

