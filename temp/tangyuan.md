NSScanner 过滤字符串
-------
**作者**: [这个汤圆没有馅](https://weibo.com/u/6603469503)

在使用`<ContactsUI/ContactsUI.h>`框架获取通讯录手机号码时，不同的 iOS 系统最后得到的手机号码也不同。有的是`xxx-xxxx-xxxx`，有的是 `xxx xxxx xxxx`。为了得到有效的手机号码，可以用正则过滤字符串。如以下代码。

```
NSMutableString *mobile = [NSMutableString stringWithString:@"131-0000-2222"];
NSMutableString *phone = [NSMutableString string];
for(int i =0; i < [mobile length]; i++) {
    NSString *temp = [mobile substringWithRange:NSMakeRange(i,1)];
    NSString *regex = @"^[0-9]+$";
    NSPredicate *pred = [NSPredicate predicateWithFormat:@"SELF MATCHES %@", regex];
    if ([pred evaluateWithObject:temp]) {
       [phone appendString:temp];
    }
}
```

除了正则外，今天要介绍的是`NSScanner `过滤器。先看一下 apple 文档里对 NSScanner 的说明。【一个字符串解析器，用于扫描字符集中的子字符或字符，以及十进制、十六进制和浮点表示形式的数值。】
![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/01/10-1.jpg)


常用属性有以下几个：

`charactersToBeSkipped`，设置忽略指定字符，默认是空格和回车。

`isAtEnd`，是否扫描结束。

`scanLocation`，扫描开始的位置。

用 `NSScanner` 扫描字符串得到有效的手机号码，代码如下：
```
NSString *originalStr = @"131-0000-2222";
NSMutableString *stripStr = [NSMutableString stringWithCapacity:originalStr.length];
NSScanner *scanner = [NSScanner scannerWithString:originalStr];
NSCharacterSet *numbers = [NSCharacterSet characterSetWithCharactersInString:@"0123456789"];
while ([scanner isAtEnd] == NO) {
    NSString *buffer;
    if ([scanner scanCharactersFromSet:numbers intoString:&buffer]) {
        [stripStr appendString:buffer];
    } else {
        [scanner setScanLocation:[scanner scanLocation] + 1];
    }
}
```

平时我们用的条件判断一般以 `if` 或 `正则表达式` 居多，`NSScanner` 其实也是一个陌生且又强大的条件判断器。

如有表述不当，欢迎指出~~
