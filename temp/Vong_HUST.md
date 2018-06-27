git 恢复误删的 stash
--------
**作者**: [Vong_HUST](https://weibo.com/VongLo)

日常开发过程中，相信大家都使用 git，团队协作使用 git-flow。也经常会遇到需求做到一半，产品或者测试反馈一个线上问题，不得不 stash 当前已经写了一半的代码，然后切回到 master 查看问题，然后又恢复会原来的 stash。但是这样操作有时候可能会把之前 stash 的代码误删，辛辛苦苦写的代码说没就没了。那么问题来了，stash 能否像 commit 那样可以随时恢复？

答案当然是肯定的。我们知道只要有提交记录，git 肯定能恢复。其实 stash 某种程度上也可以看做一种 commit，如果还记得当时 stash 的名称，就更加容易恢复了。可以使用如下命令行来恢复，其中 'your stash name' 处填入 stash 操作时留的名称

```
$ git fsck 2> /dev/null | awk '/commit/{print $3}' | git show --stdin --grep 'your stash name'
```

最终可以在终端中看到一些 commit 信息和日期，找到对应想恢复的 SHA，然后执行

```
$ git stash apply your-commit-sha
```

关于第一处代码的解释：

> 1. The funny 2> /dev/null part ignores all error messages (they are thrown to /dev/null a dark hole in every UNIX system).
> 2. git fsck checks your repo for orphaned commits.
> 3. This prints a list of information, containing the id of the commit and it’s type, for example:

       dangling commit 6108663eaaac4b7e850f6d492cf83e7b65db2c97
       dangling commit b526a825c7730075eb5938917c8b8b7a98f63cdf
       dangling commit 04479ae959fc7470d04e1743f1c7149414c366fa
       dangling blob c6609e5099056da80ea1cdf5bea302225bd6b7ed
       dangling commit 9d65fa867f23d28ce618fcb5d7988180efb67f9c
    
> 4. We’re after commit ids, which is the third part of each line, so we run: awk '/commit/{print $3}’ to obtain the third part of each line.
> 5. git show shows information about that particular commit. So if we filter and print those containing the bug number… voilà!


**参考** 

[How to recover a deleted git stash](https://mobilejazz.com/blog/how-to-recover-a-deleted-git-stash/)

[Can we recover deleted commits? ](https://stackoverflow.com/a/34751863)



