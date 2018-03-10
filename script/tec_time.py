# coding=UTF-8

import datetime

# 当前年，用来定位年文件
def current_year():
    return str(datetime.datetime.now().year)

# 当前月，用来定位月文件
def current_month():
    month = datetime.datetime.now().month
    if month >= 10:
        return str(month)
    else:
        return '0' + str(month)