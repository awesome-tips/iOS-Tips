c++ 库不兼容问题处理
--------
**作者**: [Lefe_x](https://weibo.com/u/5953150140)


最近遇使用 WCDB 的时候遇到个 Error，当 `pod install` 的时候，会抛出异常信息：

```
[!] Can't merge user_target_xcconfig for pod targets: ["WCDB", 
"XXEngine"]. Singular build setting CLANG_CXX_LANGUAGE_STANDARD has 
different values.

[!] Can't merge user_target_xcconfig for pod targets: ["WCDB", 
"XXEngine"]. Singular build setting CLANG_CXX_LIBRARY has different 
values.

[!] Can't merge user_target_xcconfig for pod targets: ["WCDB", 
"XXEngine"]. Singular build setting CLANG_CXX_LANGUAGE_STANDARD has 
different values.

[!] Can't merge user_target_xcconfig for pod targets: ["WCDB", 
"XXEngine"]. Singular build setting CLANG_CXX_LIBRARY has different 
values.
```

在项目中查了下 `CLANG_CXX_LANGUAGE_STANDARD` 发现 WCDB 使用的 c++ 配置是：

```
CLANG_CXX_LANGUAGE_STANDARD = gnu++0x
CLANG_CXX_LIBRARY = libc++
```

而我们自己的项目本身也使用了 c++，但我们使用的库是：

```
'CLANG_CXX_LANGUAGE_STANDARD' => 'gnu++98',
'CLANG_CXX_LIBRARY' => 'libstdc++',
```

这就导致有你没我，有我没你的尴尬局面。更重要的是在 Xcode10 中已经去掉了 `libstdc++6.0.9` 这个库，这就导致使用这个库的应用在 Xcode10 上会报错。

`clang: warning: libstdc++ is deprecated; move to libc++ [-Wdeprecated]"`

遇到这种问题最好的做法是把不支持 `libc++` 的库使其支持。
	