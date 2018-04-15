# coding=UTF-8

"""
# 2017目录

## 01

* [1. Swift中lazy作惰性求值【Vong_HUST】](https://github.com/southpeak/iOS-tech-set/blob/master/2017/01.md#Swift中lazy作惰性求值)
* [2. Swift的stride操作【Vong_HUST】](https://github.com/southpeak/iOS-tech-set/blob/master/2017/01.md#Swift的stride操作)

"""

import os
import tec_time
import tec_constant
import tec_teach_set
import re
from urllib import quote

def github_url_encode(url):
    encode_title = url
    encode_title = encode_title.replace(' ', '-')
    encode_title = encode_title.replace('?', '')
    encode_title = encode_title.lower()
    encode_title = quote(encode_title)

    return encode_title

def catalog_from_month(year, month):
    results = []

    # 某年对应的目录文件
    year_catalog_file_path = tec_constant.TEACHSET_DESPATH() + '/' + year + '/' + tec_constant.TEACHSET_MONTH_FILE_NAME()
    if not os.path.exists(year_catalog_file_path):
        return results

    year_catalog_file = open(year_catalog_file_path, 'r')
    is_find = False
    for index, line in enumerate(year_catalog_file):
        # * [1. Swift中lazy作惰性求值](https://github.com/southpeak/iOS-tech-set/blob/master/2017/01.md#Swift中lazy作惰性求值)
        line = line.strip('\n')
        if is_find == False:
            month_regex = r'^(?:##)\s+([0-9]+)'
            month_match = re.findall(month_regex, line)
            if month_match:
                # 是月标题
                if month_match[0] == month:
                    is_find = True
                    continue

        if not is_find:
            continue

        # 下个月的标题，结束
        if line.startswith('##'):
            break

        results.append(line)

    year_catalog_file.close()
    return results

# 根据年目录查找标题
def current_month_catalog_titles():
    results = set()

    # 某年对应的目录文件
    year_catalog_file_path = tec_constant.TEACHSET_DESPATH() + '/' + tec_time.current_year() + '/' + tec_constant.TEACHSET_MONTH_FILE_NAME()
    if not os.path.exists(year_catalog_file_path):
        return results

    month = tec_time.current_month()
    year_catalog_file = open(year_catalog_file_path, 'r')
    is_find = False
    for index, line in enumerate(year_catalog_file):
        # * [1. Swift中lazy作惰性求值](https://github.com/southpeak/iOS-tech-set/blob/master/2017/01.md#Swift中lazy作惰性求值)
        line = line.strip()
        if is_find == False:
            month_regex = r'^(?:##)\s+([0-9]+)'
            month_match = re.findall(month_regex, line)
            if month_match:
                # 是月标题
                if month_match[0] == month:
                    is_find = True
                    continue

        if not is_find:
            continue

        # 下个月的标题，结束
        if line.startswith('##'):
            break

        regex = r'^(?:\*)\s*\[(.{0,})\]'
        title_match = re.findall(regex, line)
        for item in title_match:
            results.add(item)

    year_catalog_file.close()
    return results


def save_catalog(catalog):
    month = tec_time.current_month()
    year = tec_time.current_year()

    # 如果年文件夹不存在需要创建
    year_file_path = tec_constant.TEACHSET_DESPATH() + '/' + year
    if not os.path.exists(year_file_path):
        os.mkdir(year_file_path)

    # 某年对应的目录文件
    year_catalog_file_path = year_file_path + '/' + tec_constant.TEACHSET_MONTH_FILE_NAME()

    # 年目录文件
    if not os.path.exists(year_catalog_file_path):
        year_catalog_file = open(year_catalog_file_path, 'w')
        year_catalog_file.write('# ' + year + '目录')
        year_catalog_file.write('\n')
    else:
        year_catalog_file = open(year_catalog_file_path, 'a+')

    catalog_titles = current_month_catalog_titles()
    techset_dic = tec_teach_set.tempfile_teachset_titles_authors()

    if len(catalog_titles) == 0:
        year_catalog_file.write('\n## ' + month + '\n')

    index = len(catalog_titles)
    for (key, teachset_title) in techset_dic.items():
        author = key.split('_')[0]
        is_find = False
        # 防止重复插入
        for catalog in catalog_titles:
            if teachset_title in catalog:
                is_find = True
                break

        if is_find:
            print('该标题已经插入目录中，不需要插入：' + teachset_title)
            continue

        index += 1

        header = '* [%s. %s 【%s】]'%(str(index), teachset_title,author)
        url_source = 'https://github.com/southpeak/iOS-tech-set/blob/master/%s/%s#'%(year,month+tec_constant.TEACHSET_FILE_EXTENSION())
        encode_title = github_url_encode(teachset_title)

        catalog_one = '%s(%s%s)'%(header,url_source,encode_title)

        year_catalog_file.write('\n' + catalog_one)


# 根据年月录查找标题
def year_month_catalog_titles(year, month):
    results = []

    # 某年对应的目录文件
    year_catalog_file_path = tec_constant.TEACHSET_DESPATH() + '/' + year + '/' + tec_constant.TEACHSET_MONTH_FILE_NAME()
    if not os.path.exists(year_catalog_file_path):
        return results

    year_catalog_file = open(year_catalog_file_path, 'r')
    is_find = False
    for index, line in enumerate(year_catalog_file):
        print(line)
        # * [1. Swift中lazy作惰性求值](https://github.com/southpeak/iOS-tech-set/blob/master/2017/01.md#Swift中lazy作惰性求值)
        line = line.strip()
        if is_find == False:
            month_regex = r'^(?:##)\s+([0-9]+)'
            month_match = re.findall(month_regex, line)
            if month_match:
                # 是月标题
                if month_match[0] == month:
                    is_find = True
                    continue

        if not is_find:
            continue

        # 下个月的标题，结束
        if line.startswith('##'):
            break

        regex = r'^(?:\*)\s*\[(.{0,})\]'
        title_match = re.findall(regex, line)
        for item in title_match:
            results.append(item)

    year_catalog_file.close()
    return results

# 脚本入口
if __name__ == '__main__':
    template = '* [1. Lefe_x teach_test3 【Lefe_x】](https://github.com/southpeak/iOS-tech-set/blob/master/2018/03.md#Lefe_x teach_test3)'
    regex = r'^(?:\*)\s*\[(.{0,})\]'
    spaceMatch = re.findall(regex, template)
    for item in spaceMatch:
        print('space: ' + item)

    title = "## 12"
    title_regex = r'^(?:##)\s+([0-9]+)'
    titleMatch = re.findall(title_regex, title)
    for item in titleMatch:
        print(item)

    author = '**作者**: [Lefe_x](https://weibo.com/u/5953150140)'
    author_regx = '\[(.{0,})\]'
    authorMatch = re.findall(author_regx, author)
    for item in authorMatch:
        print(item)



    encode_title = 'iOS 你的APP中能藏的住秘密吗?'
    encode_result = 'ios-%E4%BD%A0%E7%9A%84app%E4%B8%AD%E8%83%BD%E8%97%8F%E7%9A%84%E4%BD%8F%E7%A7%98%E5%AF%86%E5%90%97'
                    #'ios-%E4%BD%A0%E7%9A%84app%E4%B8%AD%E8%83%BD%E8%97%8F%E7%9A%84%E4%BD%8F%E7%A7%98%E5%AF%86%E5%90%97'
                    #'ios-%E4%BD%A0%E7%9A%84app%E4%B8%AD%E8%83%BD%E8%97%8F%E7%9A%84%E4%BD%8F%E7%A7%98%E5%AF%86%E5%90%97%EF%BC%9F'
    encode_title = encode_title.replace(' ', '-')
    encode_title = encode_title.replace('?', '')
    encode_title = encode_title.lower()
    encode_title = quote(encode_title)
    if encode_result == encode_title:
        print('successful')
    else:
        print('falied')
    print('=======')
    print(encode_title)

    titles = year_month_catalog_titles('2018', '01')
    print(titles)