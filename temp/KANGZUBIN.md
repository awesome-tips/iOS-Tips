iOS 自带九宫格拼音键盘与 Emoji 表情之间的坑
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

最近产品提了一个需求：要求某个“输入框”禁止输入 Emoji 表情，我们能想到的方案是：在 `UITextField` 的 `textField:shouldChangeCharactersInRange:replacementString:` 代理方法中判断即将输入的字符串是否包含 Emoji 表情，如果包含，就在该方法中返回 `NO`，不允许输入。

关于如何判断一字符串是否包含 Emoji 表情的方法，网上已经有很多代码片段，一般是通过 `Unicode` 编码范围来判断 ，详见这里：[https://gist.github.com/cihancimen/4146056](https://gist.github.com/cihancimen/4146056) ，方法名记为：

```
- (BOOL)stringContainsEmoji:(NSString *)string;
```

按照上述思路开发完后，Emoji 表情确实是被限制住无法输入了，但是当把键盘切换为 iOS 系统自带的九宫格拼音键盘准备输入汉字时，却发现拼音无法输入。这是怎么回事？

首先通过观察系统自带拼音键盘的行为，可以发现，当通过拼音来输入汉字时，系统会先在输入框中“预输入”拼音字母作为占位，等用户在键盘上选中汉字时，输入框中的占位“拼音字母”就会被替换为所对应的汉字，如下图：

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/05/10-1.jpg)

通过断点调试我们还发现，在输入拼音过程中，以“知识小集”（zhishixiaoji）为例，当我们通过点击第 9 个键来输入字母 `z` 时，在 UITextField 的代理方法中获取到的即将输入的字符不是 `z` ，而是一个符号 ➒ ，而输入结束后（`textFieldDidChange:`）该符号 ➒ 就会被替换为所对应的字母，然后当点击第 4 个键来输入字母 `h` 时，同样地得到即将输入的字符为 ➍ ，然后再被替换为 `h`，以此类推...

我们猜测，苹果之所以这么做是因为，对于九宫格拼音键盘，一个键代表着 3 或 4 个字母，当你点击一个键时，它并不知道你要输入那个字母，所以用一个带圆圈的数字符号作为临时占位，等输入结束时才替换为相应的字母。

在九宫格拼音键盘中，"ABC" 键 ~ "WXYZ" 键所对应的临时占位符号分别为 ➋➌ ... ➒ ，表情 "^-^" 键所对应的为符号 ☻ ，而这些符号在 `stringContainsEmoji:` 方法中刚好都被判为是 Emoji，所以当输入框禁止输入 Emoji 表情时，就会导致拼音也无法输入。

解决方案就是在 Emoji 判定方法中，过滤掉上述符号（对应的 `Unicode` 编码为 `U+278b` ~ `U+2792` 和 `U+263b`），如下：

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/05/10-2.png)

但我们发现系统自带的“全键盘拼音输入”不会有上述问题，因为每个键都只代表一个字母：

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/05/10-3.jpg)

而且，国内常用的第三方输入法也不会有这个问题，因为它们不会在输入框中“预输入”拼音字符（而是把拼音显示在键盘上方），只有等用户选中汉字时，才把汉字填写到输入框中，如下（搜狗输入法）：

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2018/05/10-4.jpg)
