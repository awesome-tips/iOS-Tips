# podspec 中预编译宏的使用
--------
**作者**: [Vong_HUST](https://weibo.com/VongLo)

相信大家在写一个独立的组件的时候可能都会遇到一个问题，写了一个大而全的库发布到 Cocoapods 上，但是接入者可能只想使用其中几个功能，但是却不得不引入所有代码，有点伤。那有没有对应的解决方案呢？答案是肯定的，就是使用 Cocoapods 中提供的 GCC_PREPROCESSOR_DEFINITIONS。这个是从 SDWebImage 中学到的。

SD 有一个功能是使用 libwebp 来解码展示 WebP 图片。但是一般情况下，引入方是不需要这个功能的。所以作者巧妙的使用了如下方式，来实现 WebP 的引入。即

```ruby
# 省略了很多不是重点的代码，具体可以参考 SDWebImage
s.subspec 'WebP' do |webp|
    webp.xcconfig = { 
      'GCC_PREPROCESSOR_DEFINITIONS' => '$(inherited) SD_WEBP=1',
    }
  end
```


