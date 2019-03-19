iOS 判断设备是否静音
--------
**作者**: [KANGZUBIN](https://weibo.com/kangzubin)

在 iOS 设备中，主要有以下两种类型的声音：

* **铃声和提醒**：包括电话、短信、通知等系统类的声音（也包括按键音、锁定声，这两者可在设置中设置是否开启），它们受物理静音开关键的控制，也就是说，当设备开启静音时，这些声音是不会播放的。

* **媒体声音**：一般为 App 播放音视频时的声音，音量大小可通过物理音量 + - 键来控制，但它不受设备静音开关键的控制，即当静音键开启时，我们仍然可以通过相关 API 正常播放声音。

因此，这里说的静音分为两种情况，“通过物理静音键开启静音” 和 “将媒体音量调小至 0”。对于后者比较简单，我们可以通过 `[AVAudioSession sharedInstance].outputVolume` 获取当前音量大小是否为 0 来判断。

下面我们介绍一下如何检测设备静音开关键的状态。

在 iOS 5 之前，我们可以使用以下方式判断静音键的开关：

```objc
- (BOOL)isMuted {
    CFStringRef route;
    UInt32 routeSize = sizeof(CFStringRef);
    OSStatus status = AudioSessionGetProperty(kAudioSessionProperty_AudioRoute, &routeSize, &route);
    if (status == kAudioSessionNoError) {
        if (route == NULL || !CFStringGetLength(route))
            return YES;
    }
    return NO;
}
```

但苹果在 iOS 5 之后禁止了这种方式的使用，并且也没有提供相关新的 API 来判断，于是网上有一种曲线救国的方式，大致实现为：

使用 AudioServicesPlaySystemSound 函数播放一段极短的空白音频（假设为 0.2s），并监听音频播放完成事件，如果从开始播放到回调完成方法的间隔时间小于 0.1s，则意味当前静音开关为开启状态。这是因为，AudioServicesPlaySystemSound 有一个特性是：它播放的声音属于系统音效，所以是受静音按键控制的，且如果当前处于静音模式的话，调用此函数后会**立即**执行播放完成的回调，这样计算得到的时间间隔会很小，就可以用来判断设备是否静音了。代码大致如下：

```objc
static CFTimeInterval startPlayTime;

- (void)monitorMute {
    // 记录开始播放的时间
    startPlayTime = CACurrentMediaTime();
    // 假设本地存放一个长度为 0.2s 的空白音频，detection.aiff
    CFURLRef soundFileURLRef = CFBundleCopyResourceURL(CFBundleGetMainBundle(), CFSTR("detection"), CFSTR("aiff"), NULL);
    SystemSoundID soundFileID;
    AudioServicesCreateSystemSoundID(soundFileURLRef, &soundFileID);
    AudioServicesAddSystemSoundCompletion(soundFileID, NULL, NULL, PlaySoundCompletionBlock, (__bridge void *)self);
    AudioServicesPlaySystemSound(soundFileID);
}

static void PlaySoundCompletionBlock(SystemSoundID SSID, void *clientData) {
    AudioServicesRemoveSystemSoundCompletion(SSID);
    // 播放结束时，记录时间差，如果小于 0.1s，则认为是静音
    CFTimeInterval playDuring = CACurrentMediaTime() - startPlayTime;
    if (playDuring < 0.1) {
        NSLog(@"静音");
    } else {
        NSLog(@"非静音");
    }
}
```

[参考连接1](https://www.jianshu.com/p/6db6065b6b3d)、[参考链接2](https://mp.weixin.qq.com/s/yYCaPMxHGT9LyRyAPewVWQ)
