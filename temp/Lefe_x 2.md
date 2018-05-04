在 Cycript 和 LLDB 中使用私有的方法调试 iOS
--------
**作者**: [Lefe_x](https://weibo.com/u/5953150140)

下面这些方法对于使用 `Cycript` 和 `LLDB` 调试第三方应用非常方便，比如想打印当前的视图层级结构，打印某个类的属性，方法，找到当前显示的 `ViewController` 等。当然，在非逆向的环境中，可以使用 `performSelector:` 执行，可以查看到同样的效果，下面的例子通过 `performSelector:` 方法获取。

- `recursiveDescription`：打印某个视图的层级关系；

```
<UIWindow: 0x7fdc86411aa0; frame = (0 0; 375 812); gestureRecognizers = <NSArray: 0x600000248a60>; layer = <UIWindowLayer: 0x600000239e80>>
```

- `_printHierarchy`：直接获取当前显示的 `ViewController`，不必使用 `[view nextResponder]` 获取当前显示的 viewController；

```
<ViewController 0x7fdc86411270>, state: appeared, view: <UIView 0x7fdc867085e0>
```

- `_autolayoutTrace`：是 recursiveDescription 的精简版，忽略了关于 View 的描述信息；

```
UIWindow:0x7fdc86411aa0
|   UIView:0x7fdc867085e0
```

- `_ivarDescription`：打印某个实例的所有变量名和值；

```
<Lefex: 0x604000005a80>:
in Lefex:
	_name (NSString*): @"wsy"
in NSObject:
	isa (Class): Lefex (isa, 0x10cde9038)
```

- `_methodDescription`：打印某个类的所有属性，实例方法，类方法。

```
<Lefex: 0x604000005a80>:
in Lefex:
	Class Methods:
		+ (id) trueName; (0x10cde6590)
	Properties:
		@property (copy, nonatomic) NSString* name;  (@synthesize name = _name;)
	Instance Methods:
		- (void) changeName; (0x10cde6580)
		- (void) .cxx_destruct; (0x10cde6620)
		- (id) name; (0x10cde65b0)
		- (void) setName:(id)arg1; (0x10cde65e0)
in NSObject:
	Class Methods:
	省略......
```

[参考](http://iosre.com/t/powerful-private-methods-for-debugging-in-cycript-lldb/3414)
