import time
import redis

# 创建 redis 连接
pool = redis.ConnectionPool(host='localhost', port=6379)
r = redis.StrictRedis(connection_pool=pool)
# 记录当前时间
time1 = time.time()
#  1 万次写
for i in range(10000):
    data = {'username': 'zhangfei', 'age': 28}
    r.hmset('users' + str(i), data)
# 统计写时间
delta_time = time.time() - time1
print(delta_time)
# 记录当前时间
time2 = time.time()
# 1 万次读
result = None
for i in range(10000):
    result = r.hmget('users' + str(i), ['username', 'age'])
# 统计读时间
delta_time = time.time() - time2
print(delta_time)
print(result)
