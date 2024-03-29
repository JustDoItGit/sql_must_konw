import json
import traceback
import mysql.connector

# 读取链接配置文件
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
    sql = 'SELECT id, name, hp_max FROM heros WHERE hp_max>6000'
    cursor.execute(sql)
    data = cursor.fetchall()
    print(cursor.rowcount, '查询成功。')
    for each_hero in data:
        print(each_hero)
except Exception as e:
    # 打印异常信息
    traceback.print_exc()
finally:
    cursor.close()
    db.close()
