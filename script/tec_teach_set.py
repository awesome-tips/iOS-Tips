# coding=UTF-8


"""
【每条小集的模版】
iOS 关于音频播放调研
--------
**作者**: [Lefe_x](https://weibo.com/u/5953150140)

正文

【规则】
1. 第一行为标题
2. 第二行为： --------
3. 第三行为：**作者**: [微博名](微博链接)
4. 第四行为：空行
5. 第五行之后为正文
"""

import re
import os
import tec_time
import tec_constant

# 临时文件夹下小集标题的集合
def tempfile_teachset_titles_authors():
    root_path = tec_constant.TEACHSET_DESPATH_TEMP()
    paths = os.listdir(root_path)
    results = dict()
    # 区分作者
    index = 0
    for compent in paths:
        # 过滤掉隐藏文件
        if compent.startswith('.'):
            continue
        index += 1
        # 每个人的小集目录
        teach_set_path = os.path.join(root_path, compent)
        ext = os.path.splitext(teach_set_path)[1]
        if ext == '.md':
            teach_set_file = open(teach_set_path)
            lines = teach_set_file.readlines()
            if len(lines) > 0:
                # 作者 **作者**: [Lefe_x](https://weibo.com/u/5953150140)
                regx = '\[(.{0,})\]'
                matchs_author = re.findall(regx, lines[2])
                if matchs_author:
                    author = matchs_author[0]
                    results[author + '_' + str(index)] = lines[0].replace('\n','')

    return results


# 判断小集的内容模版是否正确
def is_valid_teachset_template(path):
    teach_set_file = open(path)
    lines = teach_set_file.readlines()
    if len(lines) < 3:
        teach_set_file.close()
        return False
    line1 = lines[1]
    line1 = line1.strip()
    regx = '^-{4,}'
    matchs_line1 = re.findall(regx, line1)

    author_line = lines[2]
    author_line = author_line.strip()
    regx = '^(\*\*作者\*\*)(:|：)'
    matchs_line2 = re.findall(regx, author_line)

    teach_set_file.close()

    return len(matchs_line1) > 0 and len(matchs_line2) > 0


# 每个文件中的标题集合
def all_teachset_titles(path):
    teach_set_file = open(path)
    lines = teach_set_file.readlines()
    titles = []

    if len(lines) == 0:
        teach_set_file.close()
        return titles

    for index, line in enumerate(lines):
        line = line.strip()
        regx = '^-{4,}'
        match_lines = re.findall(regx, line)
        if len(match_lines) > 0:
            if index != 0:
                title = lines[index - 1]
                titles.append(title)
    teach_set_file.close()
    return titles


# 把小集写入到当前月的内容中
def write_teach_set_to_file(path):
    year = tec_time.current_year()
    month = tec_time.current_month()
    year_file_path = tec_constant.TEACHSET_DESPATH() + '/' + year
    month_file_path = year_file_path + '/' + month + tec_constant.TEACHSET_FILE_EXTENSION()

    # 如果年文件夹不存在需要创建
    if not os.path.exists(year_file_path):
        os.mkdir(year_file_path)

    # 月文件，如果文件已经存在，文件需要写入空行
    if os.path.exists(month_file_path):
        # 检查是否已经写入过小集，需要用标题判断
        titles = all_teachset_titles(month_file_path)
        if len(titles) > 0:
            month_temp_file = open(path, 'r')
            lines = month_temp_file.readlines()
            if len(lines) > 0:
                f_line = lines[0]
                if f_line in titles:
                    print("该小集已经添加：" + f_line.strip('\n'))
                    month_temp_file.close()
                    return
            month_temp_file.close()

        month_file = open(month_file_path, 'a+')
        month_file.write('\n\n')

    else:
        # 月文件不存在需要，开头写入年月和空行
        month_file = open(month_file_path, 'a+')
        month_file.write('# ' + year + '.' + month)
        month_file.write('\n')

    # 遍历小集内容，写入小集中
    teactset_file = open(path)
    for index, line in enumerate(teactset_file):
        month_file.write(line)

    month_file.close()
    teactset_file.close()


# 脚本入口
if __name__ == '__main__':
    # 从小集的 temp 目录中读取文件
    path = '/Users/wangsuyan/Desktop/project/iOS-tech-set/TEMP/Lefe_x.md'
    titles =  all_teachset_titles(path)
    print('===============================')
    print(titles)

    month_file = open(path, 'r')
    llines = month_file.readlines()
    print('===============================')
    if len(llines):
        title = llines[0]
        if title in titles:
            print('Hello I am in')