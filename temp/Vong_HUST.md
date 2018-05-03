CoreData 关系的4种删除规则
--------
**作者**: [Vong_HUST](https://weibo.com/VongLo)

由于项目是基于 `CoreData` 的，所以 `CoreData` 方面遇到的问题比较多。今天主要为大家分享一下 CoreData 中关系的4种删除规则。

先假设我们有两个实体，`Blog` 和 `Category`，一篇 `Blog` 只能属于一个 `Category`，一个 `Category` 可以有多篇 `Blog`。
如图:
![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/05/1-1.jpg?raw=true)
![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/05/1-2.jpg?raw=true)

1.No Action

规则为 `No Action` 时，当 `category` 删除时， `blogs` 是不会被通知到的，由于 `CoreData` 里关系是双向的，`blog` 这边依然认为他被关联到对应的 `category`。这种规则到目前还没用到过，也没有具体的使用场景，如果设置成 `No Action`，如果操作不当，可能会有崩溃发生

2.Nullify

还是拿上面举例，如果 `category` 被删除，`blog` 对应的 `category`  关系会被置为 `nil`。这个是系统默认删除规则，也是日常中用的最多的删除规则。

3.Cascade

`Cascade` 规则某些场景下也十分有用。还是用上面例子，一般情况下，我们想 `category` 被删除之后，其拥有的所有 `blog` 实例也要删除，那这个时候直接将删除规则设置成这个即可。`CoreData` 在 `category` 删除后会自动将其关联的 `blog` 也全部删除。但这种情况一般只存在与一对多(或一对一)的情况，如果是多对多，就不适合用这种规则。

4.Deny

这个规则刚好和 `Cascade` 相反，`category` 只有在其所拥有的 `blogs` 都被删除的情况下才会被删除。这种情况在我们项目中，也没有具体使用场景。

综上，一般业务场景下 `Nullify` 和 `Cascade` 规则已经可以满足。如果有其他特殊场景也可以考虑1和4。欢迎补充和讨论~



替换系统音量提示
--------
**作者**: [Vong_HUST](https://weibo.com/VongLo)

相信平时大家在用 iPhone 看视频调节音量时，总会被系统的音量提示所打扰，因为它会遮住一部分内容。所以很多视频应用都使用自定义音量视图的方式来替代系统的音频。比如下面三张截图，分别来自 Instagram、哔哩哔哩、即刻

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/05/2-1.png?raw=true)

其实要实现这个，主要是实现下面几个要点

- 激活 AudioSession
- 创建一个 MPVolumeView，并将其添加到当前可见的视图层级当中，同时将其 frame 设置到不可见区域
- 监听音量按钮触发事件，改变音量提示（监听方式有两种：KVO、NSNotification）

代码分别为

```objc
// KVO
- (void)dealloc {
    [[AVAudioSession sharedInstance] removeObserver:self
                                         forKeyPath:NSStringFromSelector(@selector(outputVolume))];
}

- (void)addObserver {
    [[AVAudioSession sharedInstance] addObserver:self
                                      forKeyPath:NSStringFromSelector(@selector(outputVolume))
                                         options:NSKeyValueObservingOptionNew
                                         context:nil];
}

- (void)observeValueForKeyPath:(NSString *)keyPath
                      ofObject:(id)object
                        change:(NSDictionary<NSKeyValueChangeKey,id> *)change
                       context:(void *)context {
    if ([change isKindOfClass:[NSDictionary class]]) {
        NSNumber *volumeNum = change[@"new"];
        if (volumeNum) {
            [self volumeDidChange:[volumeNum floatValue]];
        }
    }
}

- (void)volumeDidChange:(CGFloat)volume {
    // 显示自定义音量提示
}

```

```objc
// Notification
static NSNotificationName const kSystemVolumeDidChangeNotification = @"AVSystemController_SystemVolumeDidChangeNotification";

- (void)dealloc {
    [[NSNotificationCenter defaultCenter] removeObserver:self];
}

- (void)addObserver {
    [[NSNotificationCenter defaultCenter] addObserver:self
                                             selector:@selector(volumeDidChange:)
                                                 name:kSystemVolumeDidChangeNotification
                                               object:nil];
}

- (void)volumeDidChange:(NSNotification *)notification {
    NSString *category = notification.userInfo[@"AVSystemController_AudioCategoryNotificationParameter"];
    NSString *changeReason = notification.userInfo[@"AVSystemController_AudioVolumeChangeReasonNotificationParameter"];
    if (![category isEqualToString:@"Audio/Video"] || ![changeReason isEqualToString:@"ExplicitVolumeChange"]) {
        return;
    }

    CGFloat volume = [[notification userInfo][@"AVSystemController_AudioVolumeNotificationParameter"] floatValue];
    // 显示自定义音量提示
}
```


- KVO 在音量调节至最大/最小时，这个时候再调大/调小音量，由于 `outputVolume` 的值不变，所以不会触发 `KVO`，也就无法展示自定义音量视图，
- 监听系统私有(未公开的)通知，名字是 `AVSystemController_SystemVolumeDidChangeNotification`，这个监听不会受到最大/最小音量时，调大/调小音量的影响，只要音量键按下，始终都会触发。但是这个通知由于是私有的，可能存在被拒风险，而且将来系统版本该通知名字发生改变，由于是硬编码而不像其它系统通知使用的是常量，会导致监听不到的问题。

参考链接：[VolumeBar](https://github.com/gizmosachin/VolumeBar)


