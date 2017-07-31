#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql,time

ISOTIMEFORMAT = "%Y-%m-%d %X" #设置默认时间格式

def SelInfo(cursor):
	cursor.execute("select * from data_info")
	return cursor.fetchall()

conn = pymysql.connect(host='127.0.0.1',port= 3306,user = 'root',passwd='root',db='test',charset='utf8') #db：库名  charset 建议查询的时候均添加，要不然会出现字符集无法解析的情况
cursor = conn.cursor()
# cursor.execute("select * from data_info")
effect_row  = SelInfo(cursor)
print("the first select")
print(effect_row)
# print("the second select")
# print(effect_row)
times = 0
while effect_row == None or effect_row == 0:
	times += 1
	d_list = []
	for x in range(1,3):  #从1开始，循环到3（不包括3）
		d_list.append([("n"+str(x)),int(x+10),time.strftime(ISOTIMEFORMAT, time.localtime())])
	effect_row = cursor.executemany(" insert into data_info(d_name,d_age,d_createtime) values (%s,%s,%s)",d_list)

	# 提交，不然无法保存新建或者修改的数据
	conn.commit()

	print(times)
	print("第%d插入，当前%d行"%(times,effect_row))

print(SelInfo(cursor))


# 关闭游标
cursor.close()
# 关闭连接
conn.close()

input()
