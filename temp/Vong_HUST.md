RACObserve 常见用法及区别
--------
**作者**: [Vong_HUST](https://weibo.com/VongLo)

用过 [`ReactiveCocoa`](https://github.com/ReactiveCocoa/ReactiveCocoa/tree/v2.5) 的应该都比较熟悉这个 `RACObserve` 这个宏，但是不知道大家有没有对这个宏具体展开，进行分析。

比较常见的用法就是 `RACObserve(someTarget, someProperty)`，但是大家了解 `RACObserve(target.someTarget, someProperty)` 和 `RACObserve(target, someTarget.someProperty)` 之间的区别么？具体可以看以下代码片段以及执行的结果

```objc
self.label = [UILabel new];
self.label.text = @"123";

[RACObserve(self.label, text) subscribeNext:^(id x) {
    NSLog(@"RACObserve(self.label, text) 的方式 %@", x);
}];

[RACObserve(self, label.text) subscribeNext:^(id x) {
    NSLog(@"RACObserve(self, label.text) 的方式 %@", x);
}];

self.label.text = @"1234";
self.label = [UILabel new];
self.label.text = @"12345";

// output

RACObserve(self.label, text) 的方式 123
RACObserve(self, label.text) 的方式 123
RACObserve(self, label.text) 的方式 1234
RACObserve(self.label, text) 的方式 1234
RACObserve(self, label.text) 的方式 (null)
RACObserve(self, label.text) 的方式 12345
```

以上面代码为例，`RACObserve(self.label, text)` 其实是监听 `self.label` 这个对象的 `text` 属性，所以当这个对象 `text` 发生变化时，第一个是 `block` 是能够收到回调的，但是当 `self.label` 被重新赋值后，原来的 `label` 无人持有相当于变成了 `nil`，所以第一个 `block` 将不再生效。而 `RACObserve(self, label.text)` 监听的是 self，然后 `keyPath` 是 `label.text`，所以当 `label` 或者其 `text` 发生变化都会触发这个回调。所以区别在于 `target` 以及 `keyPath` 的设置。

如果上述表达有不恰当的地方，欢迎指出，一起探讨~






