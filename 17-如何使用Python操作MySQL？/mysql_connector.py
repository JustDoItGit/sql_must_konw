import json
import mysql.connector

with open('mysql.json', encoding='utf-8') as con_json:
    con_dict = json.load(con_json)

# 打开数据库链接
db = mysql.connector.connect(
    host=con_dict['host'],
    user=con_dict['user'],
    passwd=con_dict['passwd'],
    database=con_dict['database'],
    auth_plugin=con_dict['auth_plugin'],
)

# 获取操作游标
cursor = db.cursor()
# 执行 SQL 语句
cursor.execute('SELECT VERSION()')
# 获取一条数据
data = cursor.fetchone()
print('MySQL 版本: {}'.format(data))

# 关闭游标 & 数据库链接
cursor.close()
db.close()
