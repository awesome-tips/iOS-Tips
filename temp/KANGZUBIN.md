再谈 iOS 输入框的字数统计/最大长度限制
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

前两周我们发了一个小集[「iOS 自带九宫格拼音键盘与 Emoji 表情之间的坑」](https://github.com/awesome-tips/iOS-Tips/blob/master/2018/05.md#ios-%E8%87%AA%E5%B8%A6%E4%B9%9D%E5%AE%AB%E6%A0%BC%E6%8B%BC%E9%9F%B3%E9%94%AE%E7%9B%98%E4%B8%8E-emoji-%E8%A1%A8%E6%83%85%E4%B9%8B%E9%97%B4%E7%9A%84%E5%9D%91)，介绍了如何解决由于输入框限制 Emoji 表情的输入导致中文拼音也无法输入的问题。

后面我们又有了新需求：**对输入框已输入的文本字数进行实时统计，并在界面上显示剩余字数，且不能让所输入的文本超过最大限制长度**。但这个简单的功能仍然有不少小坑。

在上一个小集中，我们讲到，对于 iOS 系统自带的键盘，有时候它在输入框中填入的是占位字符（已被高亮选中起来），等用户选中键盘上的候选词时，再替换为真正输入的字符，如下：

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/06/1-1.jpg)

这会带来一个问题：比如输入框限定最多只能输入 10 位，当已经输入 9 个汉字的时候，使用系统拼音键盘则第 10 个字的拼音就打不了（因为剩余的 1 位无法输入完整的拼音）。

怎么办呢？上面提到，输入框中的拼音会被高亮选中起来，所以我们可以根据 `UITextField` 的 `markedTextRange` 属性判断是否存在高亮字符，如果有则不进行字数统计和字符串截断操作。我们通过监听 `UIControlEventEditingChanged` 事件来对输入框内容的变化进行相应处理，如下：

```objc
[self.textField addTarget:self action:@selector(textFieldDidChange:) forControlEvents:UIControlEventEditingChanged];
```

```objc
- (void)textFieldDidChange:(UITextField *)textField {
    // 判断是否存在高亮字符，如果有，则不进行字数统计和字符串截断
    UITextRange *selectedRange = textField.markedTextRange;
    UITextPosition *position = [textField positionFromPosition:selectedRange.start offset:0];
    if (position) {
        return;
    }
    
    // maxWowdLimit 为 0，不限制字数
    if (self.maxWowdLimit == 0) {
        return;
    }
    
    // 判断是否超过最大字数限制，如果超过就截断
    if (textField.text.length > self.maxWowdLimit) {
        textField.text = [textField.text substringToIndex:self.maxWowdLimit];
    }
    
    // 剩余字数显示 UI 更新
}
```

对于 `UITextView` 的处理也是类似的。

另外，对于“字数”的定义是很多种理解：在 Objective-C 中字符串 `NSString` 的长度 `length`，对于一个中文汉字和一个英文字母都是 1；但如果我们要按**字节**来统计和限制，同一字符在不同编码下所占的字节数也是不同的；另外有时我们要统计的是所输入文本的单词个数，而不是字符串的长度，所以我们需要根据不同的使用场景进行分析。
