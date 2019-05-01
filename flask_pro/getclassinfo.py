#-*- coding=utf-8 -*-
from config import databaseconfig as dc
import re
conn = dc.conn
cursor = conn.cursor()
def processtheme():
    file = open('theme.txt','r',encoding='utf-8')
    for l in file.readlines():
        if "theme" in l:
            theme = l.replace("theme","").replace("\n","")
            print (theme)
        else:
            l = l.replace("\n", "").replace(" ", "")
            pat = "[0-9]+-[0-9]+"
            name = re.sub(pat, "", l)
            id = l.replace(name, "")
            print (id)



def processclass():
    file = open('class.txt','r',encoding='utf-8')
    for l in file.readlines():
        l = l.replace("\n","").replace(" ","")
        pat = "[0-9]+-[0-9]+"
        name = re.sub(pat,"",l)
        id = l.replace(name,"")
        if id == "":
            continue
        url = r"vedio/"+id
        print (id)
        sql = "insert into percourse_info (pcourse_id,pcourse_name,vedio_url) values ('%s','%s','%s')" % (id,name,url)
        cursor.execute(sql)
        conn.commit()

processtheme()