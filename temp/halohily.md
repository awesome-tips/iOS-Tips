说说 NSTimer 的新 API
--------
**作者**: [halohily](https://weibo.com/halohily)

在以往的 iOS 版本中，我们为了避免 NSTimer 的循环引用问题，一个比较常用的解决办法是为 NSTimer 添加一个 category，新增传入 block 类型参数的接口。分类内部实现是将此 block 作为 NSTimer 的 userInfo 参数传入，而 NSTimer的 target 则设置为 timer 自己。以此来避免 NSTimer 持有 VC。代码如下:

```objective-c
// NSTimer+BlocksSupport.h
#import <Foundation/Foundation.h>

@interface NSTimer (BlocksSupport)
+ (NSTimer *)ly_scheduledTimerWithTimeInterval:(NSTimeInterval)interval
repeats:(BOOL)repeats
block:(void(^)())block;
@end

// NSTimer+BlocksSupport.m
#import "NSTimer+BlocksSupport.h"

@implementation NSTimer (BlocksSupport)
+ (NSTimer *)ly_scheduledTimerWithTimeInterval:(NSTimeInterval)interval
repeats:(BOOL)repeats
block:(void(^)())block;
{
return [self scheduledTimerWithTimeInterval:interval
target:self
selector:@selector(ly_blockInvoke:)
userInfo:[block copy]
repeats:repeats];
}
+ (void)ly_blockInvoke:(NSTimer *)timer {
void (^block)() = timer.userInfo;
if(block) {
block();
}
}
@end
```

而在 iOS 10 之后，苹果终于为 NSTimer 添加了一个官方 API，支持传入 block 类型参数。可谓是千呼万唤始出来。新官方 API 包括：

```objective-c
+ (NSTimer *)timerWithTimeInterval:(NSTimeInterval)interval
repeats:(BOOL)repeats
block:(void (^)(NSTimer *timer))block API_AVAILABLE(macosx(10.12), ios(10.0), watchos(3.0), tvos(10.0));
+ (NSTimer *)scheduledTimerWithTimeInterval:(NSTimeInterval)interval
repeats:(BOOL)repeats
block:(void (^)(NSTimer *timer))block API_AVAILABLE(macosx(10.12), ios(10.0), watchos(3.0), tvos(10.0));
```

