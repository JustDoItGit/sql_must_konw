import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy import or_
from sqlalchemy import func

with open('mysql.json', encoding='utf-8') as con_json:
    con_dict = json.load(con_json)

engine = create_engine(
    'mysql+mysqlconnector://{}:{}@{}:3306/{}'.format(con_dict['user'], con_dict['passwd'], con_dict['host'],
                                                     con_dict['database']),
    connect_args={'auth_plugin': 'mysql_native_password'})

# 创建对象的基本类
Base = declarative_base()


# 定义 Player 对象
class Player(Base):
    # 标的名字
    __tablename__ = 'player'

    # 表的结构
    player_id = Column(Integer, primary_key=True, autoincrement=True)
    team_id = Column(Integer)
    player_name = Column(String(255))
    height = Column(Float(3, 2))


# 创建 DBSession 类型
DBSession = sessionmaker(bind=engine)
# 创建 session 对象
session = DBSession()


# 增加 to_dict() 方法到 Base 类中
def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


# 将对象可以转化为 dict 类型
Base.to_dict = to_dict
# 查询身高 >= 2.08 的球员有哪些
rows = session.query(Player).filter(Player.height >= 2.08).all()
print([[row.to_dict()] for row in rows])
# 查询身高 >= 2.08 且 <= 2.10的球员有哪些
rows = session.query(Player).filter(Player.height >= 2.08, Player.height <= 2.10).all()
print([[row.to_dict()] for row in rows])
# 查询身高 >= 2.08 或者 <= 2.10 的球员有哪些
rows = session.query(Player).filter(or_(Player.height >= 2.08, Player.height <= 2.10)).all()
print([[row.to_dict()] for row in rows])
"""
按照 team_id 进行分组，同时筛选分组后数据行数大于 5 的分组，
并且按照分组后数据行数递增的顺序进行排序，
显示 team_id 字段，以及每个分组的数据行数。
"""
rows = session.query(Player.team_id, func.count(Player.player_id)).group_by(Player.team_id).having(
    func.count(Player.player_id) > 5).order_by(func.count(Player.player_id).asc()).all()
print(rows)
# 关闭 session
session.close()
