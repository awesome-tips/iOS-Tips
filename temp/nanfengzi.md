在 UILabel 中渲染 HTML
--------
**作者**: [南峰子](https://weibo.com/3321824014)

我们可以使用 NSAttributedString 在 UILabel 中渲染 HTML 字符串，不过需要使用 NSAttributedString 特定的初始化方法

```swift
init(data: Data, 
options: [NSAttributedString.DocumentReadingOptionKey : Any] = [:], 
documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws
```

在这个初始化方法的 options 参数中，指定 .documentType 的值为 NSAttributedString.DocumentType.html。不过大多数情况下这还不够，我们可能还需要指定文本的样式，例如指定文本的字体或颜色，这时我们就需要在 html 文本中通过 css 来设置 style，如下代码所示：

```swift
import UIKit

extension String {

    func htmlAttributedString(with fontName: String, fontSize: Int, colorHex: String) -> NSAttributedString? {
        do {
            let cssPrefix = "<style>* { font-family: \(fontName); color: #\(colorHex); font-size: \(fontSize); }</style>"
            let html = cssPrefix + self
            guard let data = html.data(using: String.Encoding.utf8) else {  return nil }
            return try NSAttributedString(data: data, options: [.documentType: NSAttributedString.DocumentType.html, .characterEncoding: String.Encoding.utf8.rawValue], documentAttributes: nil)
        } catch {
            return nil
        }
    }
}

let html = "<strong>Dear Friend</strong> I hope this <i>tip</i> will be useful for <b>you</b>."
let attributedString = html.htmlAttributedString(with: "Futura", fontSize: 14, colorHex: "ff0000")
```

效果如下图所示

![](https://github.com/awesome-tips/iOS-Tips/blob/master/images/2019/01/3-1.png)

