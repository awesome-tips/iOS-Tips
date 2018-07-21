怎么解决网络请求的依赖关系
--------
**作者**: [蒋匿](https://weibo.com/cimer)

怎么解决网络请求的依赖关系：当一个接口的请求需要依赖于另一个网络请求的结果﻿?

1) 思路 1：操作依赖：NSOperation 操作依赖和优先级。

例如` [operationB addDependency:operationA]`; 虽然这个想法很好，但不适用异步，异步网络请求并不是立刻返回，无法保证回调时再开启下一个网络请求。

2) 思路 2：逻辑判断：在上一个网络请求的响应回调中进行下一网络请求的激活。

这是最原始的想法，但还是有 BUG：可能拿不到回调无法执行到 block 块里面的代码。

3) 思路 3：线程同步 -- 组队列（`dispatch_group`）。

先建一个全局队列 queue，并新建一个 group(用 dispatch_group_create())，然后向 Group Queue 依次追加 block，最后用 dispatch_group_notify 添加 block。当前面的 block 全部执行完，就会执行最后的 block。例如下图。

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/07/10-1.jpg)

4) 思路4：线程同步 --任务阻塞（`dispatch_barrier`）。
 
通过 dispatch_barrier_async 添加的操作会暂时阻塞当前队列，即等待前面的并发操作都完成后执行该阻塞操作，待其完成后后面的并发操作才可继续。使用 dispatch_barrier_async 可以实现类似组队列的效果。例如图2。

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/07/10-2.jpg)

5) 思路5：线程同步 -- 信号量机制（dispatch_semaphore）。

除了任务阻塞，还可以利用信号量实现这种阻塞效果：在异步开启任务 1 和任务 2 之前，初始化一个信号量并设置为 0，然后在任务 1 的 block 中写好请求操作，操作执行完后对前面的信号量加 1，在任务 2 的 block 中，需要在开始请求之前加上等待信号量的操作。这样一来，只有任务 1 中的请求执行完后，任务 2 等到了信号量加 1 才接着执行它的请求。例如图 3。

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/07/10-3.jpg)

