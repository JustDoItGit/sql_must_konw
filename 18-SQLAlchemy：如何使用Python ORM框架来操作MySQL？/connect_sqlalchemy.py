import json
from sqlalchemy import create_engine

with open('mysql.json', encoding='utf-8') as con_json:
    con_dict = json.load(con_json)

engine = create_engine(
    'mysql+mysqlconnector://{}:{}@{}:3306/{}'.format(con_dict['user'], con_dict['passwd'], con_dict['host'],
                                                     con_dict['database']),
    connect_args={'auth_plugin': 'mysql_native_password'})
