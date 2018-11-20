句子拆分
--------

**作者**: [Lefe_x](https://weibo.com/u/5953150140)

把下面这段话拆分成句子，你会用什么方案呢？

```objective-c
知识小集是由几位志同道合的伙伴组成。你了解这个团队吗？我们在一起相处了 1 年多的时光！我想说：“我们是最棒的！”
```

我想到的方案有：正则表达式；使用 NSScanner ；使用 componentsSeparatedByCharactersInSet: ；但这几种方案都比较麻烦，后来不经意间发现了下面这个方法。 

代码如下：

```objective-c
NSString *text = @"知识小集是由几位志同道合的伙伴组成。你了解这个团队吗？我们在一起相处了 1 年多的时光！我想说：“我们是最棒的！”";
[text enumerateSubstringsInRange:NSMakeRange(0, [text length]) options:NSStringEnumerationBySentences usingBlock:^(NSString * _Nullable substring, NSRange substringRange, NSRange enclosingRange, BOOL * _Nonnull stop) {
    NSLog(@"sentence: %@ range: %@", substring, NSStringFromRange(substringRange));
}];
```

运行结果如下：

```objective-c
sentence: 知识小集是由几位志同道合的伙伴组成。 range: {0, 18}
sentence: 你了解这个团队吗？ range: {18, 9}
sentence: 我们在一起相处了 1 年多的时光！ range: {27, 17}
sentence: 我想说：“我们是最棒的！” range: {44, 13}
```



