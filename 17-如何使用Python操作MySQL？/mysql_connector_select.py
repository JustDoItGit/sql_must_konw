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
# 查询身高大于等于 2.08 的球员
sql = 'SELECT player_id, player_name, height FROM player WHERE height >= 2.08'
cursor.execute(sql)
data = cursor.fetchall()
for each_player in data:
    print(each_player)
