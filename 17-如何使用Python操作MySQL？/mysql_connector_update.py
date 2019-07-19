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
# 修改球员 约翰-科林斯
sql = 'UPDATE player SET height = %s WHERE player_name = %s'
val = (2.09, '约翰-科林斯')
cursor.execute(sql, val)
db.commit()
print(cursor.rowcount, '记录被修改。')
cursor.close()
db.close()
