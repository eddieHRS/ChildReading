# -*- coding:utf-8 -*-
import pymysql

conn = pymysql.connect(host = "127.0.0.1",user='root',password='mysql',database='university')
cursor = conn.cursor()

def insert_student_info(data):
    sql = "insert into student_info (stu_id,credit,qresult,rec_result) values(%s,%s,%s,%s)"#第三个为什么是%s 不是%d
    cursor.executemany(sql,data)
    conn.commit()

def insert_teacher_info(data):
    sql = "insert into teacher_info (tea_id,tea_email,tea_name,password,teacher_intro) values(%s,%s,%s,%s,%s)"
    cursor.executemany(sql,data)
    conn.commit()

def insert_setcourse_info(data):
    sql = "insert into setcourse_info (scourse_id,scourse_title,scourse_theme,scourse_stage,pageimg_urls,scourse_intro,buylink,scourse_credit) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.executemany(sql, data)
    conn.commit()

def insert_percourse_info(data):
    sql = "insert into percourse_info (pcourse_id,vedio_url,pcourse_intro) values(%s,%s,%s)"
    cursor.executemany(sql, data)
    conn.commit()

def insert_s_p_class_info(data):
    sql = "insert into s_p_class_info (id,scourse_id,pcourse_id,thenumber) values(%s,%s,%s,%s)"
    cursor.executemany(sql, data)
    conn.commit()

def insert_problems(data):
    sql = "insert into problems (pro_id,pro_stem,choice,answer,flag,scourse_id,pcourse_id,pro_num) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.executemany(sql, data)
    conn.commit()

def insert_class_info(data):
    sql = "insert into class_info (class_id,tea_id,scourse_id,start_time,end_time) values(%s,%s,%s,%s,%s)"
    cursor.executemany(sql, data)
    conn.commit()

def insert_takes_table(data):
    sql = "insert into takes_table (stu_id,scourse_id,stage) values(%s,%s,%s)"
    cursor.executemany(sql, data)
    conn.commit()

def insert_inclass_info(data):
    sql = "insert into inclass (stu_id,class_id) values(%s,%s)"
    cursor.executemany(sql,data)
    conn.commit()

def insert_homework_info(data):
    sql = "insert into homework_info (homework_id,class_id,stu_id,pcourse_id,done) values(%s,%s,%s,%s,%s)"
    cursor.executemany(sql, data)
    conn.commit()


    
    
    
    
    
s_data = [
    ('stuid0001', 10, 'qresult0001', 'recresult0001'),
    ('stuid0002', 15, 'qresult0002', 'recresult0002'),
    ('stuid0003', 20, 'qresult0003', 'recresult0003')
]
t_data = [
    ('teaid0001','first@123.com','teaname0001','passwors0001','intro of first teacher'),
    ('teaid0002','second@123.com','teaname0002','passwors0002','intro of second teacher'),
    ('teaid0003','third@123.com','teaname0003','passwors0003','intro of third teacher')
]

setclassdata = [
    ('setclassid0001','setclassTitle0001','theme1','stage1','pageurl0001','Setintro0001','buylink0001',4),
    ('setclassid0002','setclassTitle0002','theme2','stage2','pageurl0002','Setintro0002','buylink0002',4),
    ('setclassid0003','setclassTitle0003','theme3','stage3','pageurl0003','Setintro0003','buylink0003',4),
    ('setclassid0004','setclassTitle0004','theme4','stage4','pageurl0004','Setintro0004','buylink0004',4)
]

perclassdata = [
    ('perclassid0001','perclassurl','perclassIntro'),
    ('perclassid0002','perclassurl','perclassIntro'),
    ('perclassid0003','perclassurl','perclassIntro'),
    ('perclassid0004','perclassurl','perclassIntro'),
    ('perclassid0005','perclassurl','perclassIntro')
]

spclassdata = [
    ('s_pclass0001','setclassid0001','perclassid0001',1),
    ('s_pclass0002','setclassid0001','perclassid0002',2),
    ('s_pclass0003','setclassid0002','perclassid0003',1),
    ('s_pclass0004','setclassid0002','perclassid0004',2),
    ('s_pclass0005','setclassid0002','perclassid0005',3)
]

problemdata = [
    ('proid0001','prostem0001','choice0001','A',0,'setclassid0001','perclassid0001',1),
    ('proid0002','prostem0002','choice0002','B',0,'setclassid0001','perclassid0002',2),
    ('proid0003','prostem0003','choice0003','C',0,'setclassid0001','perclassid0003',3)
]

classdata = [
    ('classid0001','teaid0001','setclassid0001','2019-01-02','2019-03-04')
]


takesdata = [
    ('stuid0001','setclassid0001',1),
    ('stuid0002','setclassid0001',1),
    ('stuid0003','setclassid0001',1)
]

inclassdata = [
    ('stuid0001','classid0001')
]


homeworkdata = [
    ('homeworkid0001','classid0001','stuid0001','perclassid0001',0),
    ('homeworkid0002','classid0001','stuid0002','perclassid0001',1)

]


# insert_student_info(s_data)
# insert_teacher_info(t_data)
# insert_setcourse_info(setclassdata)
# insert_percourse_info(perclassdata)
# insert_s_p_class_info(spclassdata)
# insert_problems(problemdata)
# insert_class_info(classdata)
# insert_takes_table(takesdata)
# insert_inclass_info(inclassdata)
# insert_homework_info(homeworkdata)

sql = "select pcourse_id,pcourse_intro,pcourse_name,pcourse_intro,vedio_url from percourse_info"
cursor.execute(sql)
d = cursor.fetchall()
print (d)