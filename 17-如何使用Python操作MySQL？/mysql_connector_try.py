import json
import traceback
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
try:
    sql = 'INSERT INTO player (team_id, player_name, height) VALUE (%s, %s, %s)'
    val = (1003, '约翰-科林斯', 2.08)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, '插入记录成功。')
except Exception as e:
    # 打印异常信息
    traceback.print_exc()
    db.rollback()
finally:
    cursor.close()
    db.close()
