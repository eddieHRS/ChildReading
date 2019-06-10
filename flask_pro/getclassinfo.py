#-*- coding=utf-8 -*-
from config import databaseconfig as dc
import re
import re
conn = dc.conn
cursor = conn.cursor()
#首先插入所有的书名
# with open('class.txt', 'r', encoding='utf-8') as f:
#     for line in f.readlines():
#         line = line.split()
#         sql = "insert into percourse_info (pcourse_id, pcourse_name) values ('%s','%s')" % (line[0], line[1])
#         print(sql)
#         cursor.execute(sql)
# conn.commit()
#
#s_p_class_info 套课单课信息表
with open('class.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.split()
        t = line[0].split('-')
        # print(t, line[1])
        sql = "insert into s_p_class_info (scourse_id, pcourse_id, thenumber) values ('%s','%s','%s')" % (t[0], line[0],t[1])
        # print(sql)
        cursor.execute(sql)
conn.commit()


#处理主题
# with open('classtheme.txt', 'r', encoding='utf-8') as f:
#     theme = ''
#     for line in f.readlines():
#         if 'theme' in line:
#             theme = line.replace("theme", '').replace('\n', '')
#             print(theme)
#         else:
#             line = re.sub(r'《.*》', '', line)
#             print(line.replace('\n',''))
#             pcourse_id = line.replace('\n','')
#             sql = "update percourse_info set theme='%s' where pcourse_id='%s'" % (theme, pcourse_id)
#             print(sql)
#             cursor.execute(sql)
# conn.commit()
#

#从classintro中得到简介和题目
# import pandas as pd
# data_xls = pd.read_excel('classintroandpro.xlsx')
# d = data_xls.values
# print(d[0])
# for i in d:
#     id = i[0]
#     intro = i[2]
#     sql = "update percourse_info set pcourse_intro = '%s' where pcourse_id = '%s'" % (intro, id)
# #     print(sql)
#     cursor.execute(sql)
# conn.commit()
# # sql = "select pcourse_pageimgurl,pcourse_name,pcourse_intro,vedio_url,pcourse_id from percourse_info where type='%s'" % "0"
# cursor.execute(sql)
# re = cursor.fetchall()
# print(sql)
# print(re[0])
