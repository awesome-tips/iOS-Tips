iOS App 的反调试（Anti-Debug）
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

当我们上线一个 App，当然是不希望自己的 App 被攻击者/黑客玩弄于股掌之间。虽然说没有绝对的安全，但是我们可以做一些防护措施，增加攻击的成本和难度。

在越狱后的 iPhone 上运行 App，然后通过 GDB 进行动态调试，是大多数攻击者的首选，我们今天就来聊一聊如何防止 App 被别人调试。

在类 Unix 系统中，提供了一个系统调用 `ptrace` 用于实现断点调试和对进程进行跟踪和控制，而 `PT_DENY_ATTACH` 是苹果增加的一个 `ptrace` 选项，用于阻止 GDB 等调试器依附到某进程，用法如下：

```
ptrace(PT_DENY_ATTACH, 0, 0, 0);
```

根据念茜的博客[《iOS 安全攻防：阻止 GDB 依附》](https://blog.csdn.net/yiyaaixuexi/article/details/18222339)，我们可以在 `main.m` 中添加如下阻止调试的代码：

```objc
// 阻止 gdb/lldb 调试
// 调用 ptrace 设置参数 PT_DENY_ATTACH，如果有调试器依附，则会产生错误并退出
#import <dlfcn.h>
#import <sys/types.h>

typedef int (*ptrace_ptr_t)(int _request, pid_t _pid, caddr_t _addr, int _data);
#if !defined(PT_DENY_ATTACH)
#define PT_DENY_ATTACH 31
#endif

void anti_gdb_debug() {
    void *handle = dlopen(0, RTLD_GLOBAL | RTLD_NOW);
    ptrace_ptr_t ptrace_ptr = dlsym(handle, "ptrace");
    ptrace_ptr(PT_DENY_ATTACH, 0, 0, 0);
    dlclose(handle);
}

int main(int argc, char * argv[]) {
#ifndef DEBUG
    // 非 DEBUG 模式下禁止调试
    anti_gdb_debug();
#endif
    @autoreleasepool {
        return UIApplicationMain(argc, argv, nil, NSStringFromClass([AppDelegate class]));
    }
}
```

此时，如果尝试对 App 进行 GDB 依附，则会得到一个 Segmentation fault 错误。

另外，AloneMonkey 的[《关于反调试 & 反反调试那些事》](http://bbs.iosre.com/t/topic/8179)文中也介绍了可以通过 `sysctl`，`syscall`，... 等其他几种检测调试的手段。

但是，这些方式只能简单地防止 App 被动态调试，其实 `ptrace`、`sysctl`、`syscall` 等函数本身也可以被静态修改或 Hook。而且即便能有效阻止了调试，App 仍然可以通过 tweak 去 Hook App 内部的方法实现，也可以通过 dylib 注入去修改 App 的功能。

我们只好从多方面考虑，尽可能提高安全性，比如防止 tweak 依附（ 参考：[http://bbs.iosre.com/t/tweak-app-app-tweak/438](http://bbs.iosre.com/t/tweak-app-app-tweak/438) ）、防止网络请求抓包、对敏感数据进行加解密、代码混淆、检查二进制 binary 签名是否匹配；关键逻辑用更底层的 C 函数实现（虽然 C 函数也是可以被 Hook，例如 Facebook 开源的 fishhook），等等，同时我们也可以检查手机是否已越狱（ 参考：[https://blog.csdn.net/yiyaaixuexi/article/details/20286929](https://blog.csdn.net/yiyaaixuexi/article/details/20286929) ），并对越狱机做特殊处理。 

这里讲的只是冰山一角，更多关于 iOS 逆向和安全的知识，推荐阅读《iOS 应用逆向工程》和《iOS 应用逆向与安全》这两本书以及念茜的博客，相信你会有新的收获。

安全本身就是矛与盾的关系，对于未涉及该领域的人来说，常常处于两个极端，一种认为非常简单，一种认为难如登天。我们常说没有绝对的安全，上述书籍和博文介绍的各种 iOS 安全防护，也都有相应手段来绕过，只不过是更加繁琐了一点而已。

曾经有人说过这么一句话，**“当一个系统的攻击成本远远高于攻击所带来的收益时，这个系统就相对安全了”**，你觉得呢？
