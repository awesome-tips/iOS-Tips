# coding=UTF-8

 # 小集项目所在的目录
def TEACHSET_DESPATH():
    return ".."

# 小集 TEMP 目录，存放每周上传的小集
def TEACHSET_DESPATH_TEMP():
    return TEACHSET_DESPATH() + '/temp'

# 分格线
def TEACHSET_LINE_CONSTANT():
    return "  *******************"


# 文件扩展名
def TEACHSET_FILE_EXTENSION():
    return ".md"

# 月目录名称
def TEACHSET_MONTH_FILE_NAME():
    return "目录" + TEACHSET_FILE_EXTENSION()

# README 名称
def TEACHSET_README_FILE_NAME():
    return "README" + TEACHSET_FILE_EXTENSION()

# 小集成员
def TEACHSET_MEMBERS():
    return  set(['nanfengzi.md','Lefe_x.md','Vong_HUST.md','高老师很忙.md','halohily.md','KANGZUBIN.md'])