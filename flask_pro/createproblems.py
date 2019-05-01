import pandas as pd
import pymysql
conn = pymysql.connect(host = "127.0.0.1",user='root',password='mysql',database='university')
cursor = conn.cursor()

df = pd.read_excel('classintroandpro.xlsx')

def getPerintro():
    data = df.loc[:,['编号','简介']].values
    for i in data:
        sql = "update percourse_info set pcourse_intro='%s' where pcourse_id='%s'" %(i[1],i[0])
        print (sql)
        cursor.execute(sql)
        conn.commit()