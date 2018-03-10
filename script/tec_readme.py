# coding=UTF-8

"""
【更新 readme 文件，readme 文件模版如下】

我们会定期整理微博上分享的内容，然后将最新的内容标题放在这里。更多内容可以查看每月的具体内容。
[2018 年 1 月](https://github.com/southpeak/iOS-tech-set/blob/master/2018/01.md)
* [动态加载Framework/Library【南峰子_老驴】](https://github.com/southpeak/iOS-tech-set/blob/master/2018/01.md)

[2018 年 2 月](https://github.com/southpeak/iOS-tech-set/blob/master/2018/02.md)
* [编译源文件的流程【南峰子_老驴】](https://github.com/southpeak/iOS-tech-set/blob/master/2018/02.md)

[[2017]查看更多 [1] [2] [3] ... ➡️](https://github.com/southpeak/iOS-tech-set/blob/master/2018/%E7%9B%AE%E5%BD%95.md)
[[2018]查看更多 [1] [2] [3] ... ➡️](https://github.com/southpeak/iOS-tech-set/blob/master/2018/%E7%9B%AE%E5%BD%95.md)

【模版说明】
1.第一行内容为：我们会定期整理微博上分享的内容，然后将最新的内容标题放在这里。更多内容可以查看每月的具体内容。
2.找出最新2个月的内容
3.最近两个月的内容可以跳转到对应的年目录
4.查看更多内容需要跳转到每年的具体年目录下

"""

import tec_constant

def update_readme_file():

    # README 文件
    readme_file_path = tec_constant.TEACHSET_DESPATH() + '/' + tec_constant.TEACHSET_README_FILE_NAME()
    readme_file = open(readme_file_path, 'w')