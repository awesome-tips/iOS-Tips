数组去重的新姿势
--------
**作者**: [NotFound--](https://weibo.com/3951595216)

当我们需要对一个数组进行去重操作时，通过会初始化一个新数组，遍历旧数组，在遍历过程中，如果新数组中不包含当前的元素，便将元素加入到新数组中去，但其实KVC集合运算符可以valueForKeyPath:方法中使用keyPath符号来执行方法，最简单的就是@distinctUnionOfArrays，他会返回了一个去除重复元素的数组。在图一中，uniqueArray便是oldArray去重后的结果，因为oldArray是一个字符串数组，所以@distinctUnionOfObjects.self里面用到是.self,代表元素本身作为是否重复的key。
![](https://user-gold-cdn.xitu.io/2019/4/24/16a4f8818caf876a?w=1936&h=1114&f=jpeg&s=242251)

