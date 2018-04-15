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
import tec_time
import tec_year_catagoy
import datetime
import os

def update_readme_file():

    # README 文件
    readme_file_path = tec_constant.TEACHSET_DESPATH() + '/' + tec_constant.TEACHSET_README_FILE_NAME()
    readme_file = open(readme_file_path, 'r')

    temp_file_path = tec_constant.TEACHSET_DESPATH() + '/' + 'tempreadme.md'
    temp_file = open(temp_file_path, 'w')
    locked = False
    have_update = False

    for index, line in enumerate(readme_file):
        if line.startswith('## 感谢'):
            locked = False

        if line.startswith('## 最新内容'):
            locked = True
        else:
            if not locked:
                temp_file.write(line)

        if locked and not have_update:
            have_update = True
            month = tec_time.current_month()
            year = tec_time.current_year()

            temp_file.write('## 最新内容')
            temp_file.write('\n')
            temp_file.write('我们会定期整理微博上分享的内容，然后将最新的内容标题放在这里。更多内容可以查看每月的具体内容。\n\n')

            catalogs = tec_year_catagoy.catalog_from_month(year, month)
            if len(catalogs) > 0:
                temp_file.write('[%s 年 %s 月](https://github.com/southpeak/iOS-tech-set/blob/master/%s/%s)\n' % (year, month, year, month + tec_constant.TEACHSET_FILE_EXTENSION()))

            for line in catalogs:
                temp_file.write(line + '\n')

            if len(catalogs) < 8:
                # 如果小于 10 条，取上个月的
                month_int = datetime.datetime.now().month
                year_int = datetime.datetime.now().year

                if month_int == 1:
                    month_str = '12'
                    year_str = str(year_int - 1)

                else:
                    year_str = str(year_int)
                    if month_int > 9:
                        month_str = str(month_int - 1)
                    else:
                        month_str = '0' + str(month_int - 1)

                temp_file.write('\n')
                temp_file.write('[%s 年 %s 月](https://github.com/southpeak/iOS-tech-set/blob/master/%s/%s)\n' % (
                year_str, month_str, year_str, month_str + tec_constant.TEACHSET_FILE_EXTENSION()))
                catalogs = tec_year_catagoy.catalog_from_month(year_str, month_str)
                for line in catalogs:
                    temp_file.write(line + '\n')

            # 查看更多
            current_year = datetime.datetime.now().year
            year_path = tec_constant.TEACHSET_DESPATH() + '/' + str(
            current_year) + '/' + tec_constant.TEACHSET_MONTH_FILE_NAME()
            temp_file.write('\n')
            while (os.path.exists(year_path)):
                temp_file.write(
                    '[[%s]查看更多 [1] [2] [3] ... ➡️](https://github.com/southpeak/iOS-tech-set/blob/master/%s/%s)\n\n' %(current_year, current_year, tec_constant.TEACHSET_MONTH_FILE_NAME()))
                current_year -= 1
                year_path = tec_constant.TEACHSET_DESPATH() + '/' + str(
                    current_year) + '/' + tec_constant.TEACHSET_MONTH_FILE_NAME()

    readme_file.close()
    temp_file.close()

    # 重命名，并删除旧的 readme 文件
    os.remove(readme_file_path)
    os.rename(temp_file_path, readme_file_path)

# 脚本入口
if __name__ == '__main__':
    # 从小集的 temp 目录中读取文件
    update_readme_file()