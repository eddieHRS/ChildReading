import pymysql
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='mysql',
    database='childreading',
    charset='utf8mb4'
)