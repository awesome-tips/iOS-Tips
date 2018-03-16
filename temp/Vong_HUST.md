Pod 关于 unknown UUID 警告的解决方式
----
**作者**: [Vong_HUST](https://weibo.com/VongLo)

最近某次在 pod install 之后会发现终端会输出类似

```
[!] `<PBXBuildFile UUID=`xxxxxxx`>` attempted to initialize an object with an unknown UUID. `xxxxxxxx` for attribute: `file_ref`. This can be the result of a merge and  the unknown UUID is being discarded. 
```
 
的提示，如图1所示。一直很困惑，后面 Google 在 `CocoaPods repo` 下看到一个类似的 `issue`，原因是由于修改了 `pbxproj` 文件，但是没有把它提交到 git 当中，当其他人更新 pod 的时候就会提示这个。

解决方案就是使用下面这段命令 `cat ProjectName.xcodeproj/project.pbxproj | grep SECOND_UDID_F34A6B992B28CA`，然后会输出对应的文件名，然后做对应的删除或添加操作即可。再执行 pod install 或 update 之后即可正常。

综合起来整个过程如图所示

![](https://github.com/iOS-Tips/iOS-tech-set/blob/master/images/2018/03/1-1.jpg?raw=true)


[参考链接](https://github.com/CocoaPods/CocoaPods/issues/1822)

