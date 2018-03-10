# coding=UTF-8

import os
import tec_year_catagoy
import tec_teach_set
import tec_constant
import tec_readme

# 小集零时目录的标题
valid_file_names = set()


# 1. 检查小集的模版是否正确
def check_teachsets_valid(root_path):
    paths = os.listdir(root_path)

    is_all_valid = True

    for compent in paths:
        # 过滤掉隐藏文件
        if compent.startswith('.'):
            continue

        # 每个人的小集目录
        teach_set_path = os.path.join(root_path, compent)
        ext = os.path.splitext(teach_set_path)[1]
        if ext == '.md':
            valid_file_names.add(compent)
            # 检查小集内容是否合法
            if not tec_teach_set.is_valid_teachset_template(teach_set_path):
                if is_all_valid:
                    is_all_valid = False
                print(compent + ' : 的小集模版不正确')
        else:
            print('❌ : file must have extension')

    return is_all_valid


# 2.检查所有成员是否都提交了小集
def check_members_valid(root_path):
    subs = tec_constant.TEACHSET_MEMBERS() - valid_file_names
    if len(subs) > 0:
        for member_name in subs:
            print("检查到这些成员没有上传本周小集：" + member_name)
    return len(subs) > 0


# 查找小集目录下的文件
def parse_teach_set_file(path):

    if not check_teachsets_valid(path):
        return

    check_members_valid(path)

    # 3.所有小集检查成功，开始解析
    print('\n文件合法行检查成功，正在写入' + tec_constant.TEACHSET_LINE_CONSTANT() + '\n')
    for file_name in valid_file_names:
        aPath = os.path.join(path, file_name)
        print('开始处理 ' + file_name + tec_constant.TEACHSET_LINE_CONSTANT())
        tec_teach_set.write_teach_set_to_file(aPath)
        print('处理完成 ' + file_name + tec_constant.TEACHSET_LINE_CONSTANT())
        print('\n')

    # 保存小集年目录
    print('开始写入目录中 ' + tec_constant.TEACHSET_LINE_CONSTANT())
    tec_year_catagoy.save_catalog(valid_file_names)
    print('目录写入成功 ' + tec_constant.TEACHSET_LINE_CONSTANT())
    print('\n')

    # 更新 readme 文件
    print('开始写入 readme 文件中 ' + tec_constant.TEACHSET_LINE_CONSTANT())
    tec_readme.update_readme_file()
    print('readme 文件写入成功 ' + tec_constant.TEACHSET_LINE_CONSTANT())
    print('\n')

    print('本次小集已整理完成，提交前检查一遍')

# 脚本入口
if __name__ == '__main__':
    # 从小集的 temp 目录中读取文件
    parse_teach_set_file(tec_constant.TEACHSET_DESPATH_TEMP())