iOS 金额字符串格式化显示的方法
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

在一些金融类的 App 中，对于表示金额类的字符串，通常需要进行格式化后再显示出来。例如：

* `0` --> `0.00`，
* `123` --> `123.00`
* `123.456` --> `123.46`
* `102000` --> `102,000.00`
* `10204500` --> `10,204,500.00`

它的规则如下：

**个位数起每隔三位数字添加一个逗号，同时保留两位小数**，也称为“千分位格式”。

我们一开始的采取了一种比较笨拙的处理方式如下：

首先根据小数点 `.` 将传入的字符串分为两部分，整数部分和小数部分（如果没有小数点，则补 `.00`，如果有多个小数点则报金额格式错误）。对于小数部分，只取前两位；然后对整数部分字符串进行遍历，从右到左，每三位数前插入一个逗号 `,`，最后再把两部分拼接起来，代码大致如下：

```objc
- (NSString *)moneyFormat:(NSString *)money {
    if (!money || money.length == 0) {
        return money;
    }

    BOOL hasPoint = NO;
    if ([money rangeOfString:@"."].length > 0) {
        hasPoint = YES;
    }

    NSMutableString *pointMoney = [NSMutableString stringWithString:money];
    if (hasPoint == NO) {
        [pointMoney appendString:@".00"];
    }

    NSArray *moneys = [pointMoney componentsSeparatedByString:@"."];
    if (moneys.count > 2) {
        return pointMoney;
    } else if (moneys.count == 1) {
        return [NSString stringWithFormat:@"%@.00", moneys[0]];
    } else {
        // 整数部分每隔 3 位插入一个逗号
        NSString *frontMoney = [self stringFormatToThreeBit:moneys[0]];
        if ([frontMoney isEqualToString:@""]) {
            frontMoney = @"0";
        }
        // 拼接整数和小数两部分
        NSString *backMoney = moneys[1];
        if ([backMoney length] == 1) {
            return [NSString stringWithFormat:@"%@.%@0", frontMoney, backMoney];
        } else if ([backMoney length] > 2) {
            return [NSString stringWithFormat:@"%@.%@", frontMoney, [backMoney substringToIndex:2]];
        } else {
            return [NSString stringWithFormat:@"%@.%@", frontMoney, backMoney];
        }
    }
}
```

其中，`stringFormatToThreeBit:` 方法的实现如下：

```objc
- (NSString *)stringFormatToThreeBit:(NSString *)string {
    NSString *tempString = [string stringByReplacingOccurrencesOfString:@"," withString:@""];
    NSMutableString *mutableString = [NSMutableString stringWithString:tempString];
    NSInteger n = 2;
    for (NSInteger i = tempString.length - 3; i > 0; i--) {
        n++;
        if (n == 3) {
            [mutableString insertString:@"," atIndex:i];
            n = 0;
        }
    }
    return mutableString;
}
```

上述实现看起来非常繁琐。

其实，苹果提供了 `NSNumberFormatter` 用来处理 `NSString` 和 `NSNumber` 之间的转化，可以满足基本的数字形式的格式化。我们通过设置 `NSNumberFormatter` 的 `numberStyle` 和 `positiveFormat` 属性，即可实现上述功能，非常简洁，代码如下：

```objc
- (NSString *)formatDecimalNumber:(NSString *)string {
    if (!string || string.length == 0) {
        return string;
    }
    
    NSNumber *number = @([string doubleValue]);
    NSNumberFormatter *formatter = [[NSNumberFormatter alloc] init];
    formatter.numberStyle = kCFNumberFormatterDecimalStyle;
    formatter.positiveFormat = @"###,##0.00";
    
    NSString *amountString = [formatter stringFromNumber:number];
    return amountString;
}
```

关于 `NSNumberFormatter` 更详细的用法，可以参考这篇文章的介绍：[NSNumberFormatter 介绍和用法](https://www.jianshu.com/p/95952b145a8e)
