再谈 timer 之 CFRunLoopTimerRef
----
**作者**: [Lefe_x](https://weibo.com/u/5953150140)

开发过程中，有时为了满足需求，通常会 Hook 系统或第三方库的一些方法。每次写一长串模版代码，是不是很痛苦？

其实可以换一种 Hook 的姿势 ------ 使用 `CaptainHook` 库。它非常友好地提供一些宏来 Hook 某些方法。其实在逆向中，开发者通常使用这个库来 Hook 一些方法来达到目的。比如使用 class-dump 导出某个项目的头文件，然后替换掉需要 Hook 的方法。

简单举个例子：

替换掉 HookObject 类中的 hookMe 和 userName 方法。

```
// 声明要 Hook 的类，HookObject 是已经声明的一个类
CHDeclareClass(HookObject);

// Hook 无返回值，无参数的方法
CHMethod0(void, HookObject, hookMe){
    NSLog(@"I am a hook method: hookMe");
    CHSuper0(HookObject, hookMe);
}
// Hook 有返回值，无参数的方法
CHMethod0(NSString *, HookObject, userName){
    NSLog(@"I am a hook method: userName");
    return CHSuper0(HookObject, userName);
}
// 构造 Hook 的类
CHConstructor{
    CHLoadClass(HookObject);
    CHHook0(HookObject, hookMe);
    CHHook0(HookObject, userName);
}
```

[参考](https://github.com/rpetrich/CaptainHook/wiki)