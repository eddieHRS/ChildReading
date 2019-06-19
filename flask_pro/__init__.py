# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, redirect, render_template, session, url_for
from config import databaseconfig as dc
from wechat_end import *
import os


conn = dc.conn
cursor = conn.cursor()
app = Flask(__name__)
app.config['SECRET_KEY']=os.urandom(24)
@app.route('/funid0')
def funid0():
    resp = {'code': 200,'msg': '操作成功', 'data': []}
    req = request.values
    type = req['type']
    print(req['type'])
    course_info = []
    sql = "select pcourse_pageimgurl,pcourse_name,pcourse_intro,vedio_url,pcourse_id from percourse_info where type='%s'" % type
    cursor.execute(sql)
    re = cursor.fetchmany(5)
    for i in re:
        course_info.append({
            "pageImgUrls": i[0] if i[0] else 'unknow',
            "courseTitle": i[1] if i[1] else 'unknow',
            "courseIntro": i[2] if i[2] else 'unknow_intro',
            "courseLinks": i[3] if i[3] else 'unknow_link',
            "Course_ID": i[4] if i[4] else 'unknow_id'
        })
    print(course_info)
    resp['data'] = course_info
    return jsonify(resp)

@app.route('/funid1')
def funid1():
    resp = {'code': 200,'msg': '操作成功', 'data': {}}
    resp['data'] = {
        "imgUrls": [
            "sample_scroll_1.png",
            "sample_scroll_2.png",
            "sample_scroll_3.png"
        ],
        "pageImgUrls": [
            "https://i.loli.net/2019/02/08/5c5d63058df87.png",
            "https://i.loli.net/2019/02/08/5c5d63058df87.png",
            "https://i.loli.net/2019/02/08/5c5d63058df87.png"
        ],
        "courseTitle": ["标题从数据库获取1", "标题从数据库获取2", "标题从数据库获取3"],
        "courseIntro": ["简介从数据库获取1", "简介从数据库获取2", "简介从数据库获取3"],
        "courseLinks": ["#", "#", "#"]
    }
    return jsonify(resp)

@app.route('/funid2')
def funid2():
    resp = {'code': 200,'msg': '操作成功', 'data': {}}
    req = request.values
    course_id = req['course_id']
    print(course_id)
    sql = "select pcourse_name,price,pcourse_intro from percourse_info where pcourse_id = '%s'" % course_id

    cursor.execute(sql)
    re = cursor.fetchone()
    resp['data'] = {
        "courseId": course_id,
        "courseTitle": re[0],
        "coursePrice": float(re[1]),
        "time": "2019-02-23",
        "courseContent": re[2],
        "teacherIntro": "上海市优秀教师，十大文明教师称号"
    }
    return jsonify(resp)

@app.route('/buyset')
def buyset():
    resp = {'code': 200, 'msg': '操作成功', 'data': {}}
    sid = request.values['sid']
    print('sid=', sid)
    #获取title的sql
    sql1 = "select scourse_title from setcourse_info where scourse_id=%s" % sid
    cursor.execute(sql1)
    re = cursor.fetchone()
    set_title = re[0]
    print(set_title)
    sql2 = "select pcourse_name from percourse_info where pcourse_id in (select pcourse_id from s_p_class_info where scourse_id=%s)" % sid
    cursor.execute(sql2)
    re = cursor.fetchall()
    set_classList = []
    for i in re:
        set_classList.append(i[0])
    print(set_classList)
    set_banji = []
    sql3 = "select class_id,scourse_title,tea_name,teacher_intro,start_time,end_time from tea_class where scourse_id=%s" % sid
    cursor.execute(sql3)
    re = cursor.fetchall()
    for i in re:
        set_banji.append(
            {
                'class_id': i[0],
                'scourse_title': i[1],
                'tea_name': i[2],
                'teacher_intro': i[3],
                'start_time': str(i[4]),
                'end_time': str(i[5])
            }
        )
    temp = {'set_classList': set_classList, 'set_title': set_title, 'set_banji': set_banji}
    print(temp)
    resp['data'] = temp
    return jsonify(resp)

@app.route('/user')
def user():
    resp = {'code': 200, 'msg': '操作成功', 'data': {}}
    resp['data'] = {
        'credits': 20,
        'ranks': 3000
    }
    return jsonify(resp)

@app.route('/myclass')
def myclass():
    resp = {'code': 200, 'msg': '操作成功', 'data': {}}
    stu_id = request.values['stu_id']
    sql = "select class_name, stage, class_id from stu_class where stu_id='%s'" % stu_id
    res = []
    cursor.execute(sql)
    d = cursor.fetchall()
    for i in d:
        res.append({
            'name': i[0],
            'stage': i[1],
            'class_id': i[2],

            # 'pageImgUrls': 'https://i.loli.net/2019/02/08/5c5d63058df87.png'
        })

    sql = "select A.pcourse_id, pcourse_name from takes_pcourse as A inner join percourse_info as B on A.pcourse_id=B.pcourse_id where stu_id='%s'" % stu_id
    res2 = []
    cursor.execute(sql)
    d = cursor.fetchall()
    for i in d:
        res2.append({
            'pcourse_id':i[0],
            'name': i[1]
        })
    resp['data']['classList'] = res
    resp['data']['pcourseList'] = res2
    return jsonify(resp)

@app.route('/openid')
def openid():
    resp = {'code': 200, 'msg': '操作成功', 'data': {}}
    print(request.values['code'])
    code = request.values['code']
    appid = 'wxec8d692eea1d84b9'
    appsecret = '15099b21f519c34e4d28f3005e65bff9'
    url = 'https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code' % (appid, appsecret, code)
    print(url)
    return redirect(url)

@app.route('/payandadd')
def payandadd():
    resp = {'code': 200, 'msg': '操作成功', 'data': {}}
    class_id = request.values['class_id']
    open_id = request.values['open_id']
    print(class_id, open_id)
    sql = "insert inclass values('%s','%s')" % (open_id, class_id)
    cursor.execute(sql)
    conn.commit()
    return jsonify(resp)

@app.route('/addpcourse')
def addpcourse():
    resp = {'code': 200, 'msg': '操作成功'}
    stu_id = request.values['stu_id']
    pcourse_id = request.values['pcourse_id']
    print("add_pcourse")
    print(stu_id)
    print(pcourse_id)
    sql = "insert into takes_pcourse values('%s', '%s')" % (stu_id, pcourse_id)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        resp['code'] = 500
    print(resp['code'])
    return jsonify(resp)

@app.route('/delpercourse')
def delpercourse():
    resp = {'code': 200, 'msg': '操作成功'}
    pcourse_id = request.values['pcourse_id']
    stu_id = request.values['stu_id']
    print(pcourse_id, stu_id)
    sql = "delete from takes_pcourse where stu_id='%s' and pcourse_id='%s'" % (stu_id, pcourse_id)
    cursor.execute(sql)
    conn.commit()
    return jsonify(resp)

@app.route('/delsetcourse')
def delsetcourse():
    resp = {'code': 200, 'msg': '操作成功'}
    class_id = request.values['class_id']
    stu_id = request.values['stu_id']
    print(class_id, stu_id)
    sql = "delete from inclass where stu_id='%s' and class_id='%s'" % (stu_id, class_id)
    cursor.execute(sql)
    conn.commit()
    return jsonify(resp)

@app.route('/studypage')
def studypage():
    resp = {'code': 200, 'msg': '操作成功', 'data': {}}
    type = request.values['type']
    pcourse_id = request.values['id']
    print(pcourse_id)
    if int(type) == 0:
        #根据class_id 获得stage对应的
        sql = "select pcourse_id from s_p_class_info as A join class_info as B on A.scourse_id=B.scourse_id where B.stage=thenumber and class_id='%s'" % request.values['id']
        cursor.execute(sql)
        pcourse_id = cursor.fetchone()[0]
    print(pcourse_id)
    d = {}
    sql = "select pcourse_name,vedio_url from percourse_info where pcourse_id='%s'" % pcourse_id
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        d['title'] = i[0]
        d['vedioUrl'] = i[1]
    sql = "select pro_id,pro_stem,choice,answer,flag,pro_num,pcourse_id from problems where pcourse_id='%s' order by pro_num" % pcourse_id
    cursor.execute(sql)
    result = cursor.fetchall()
    d['ques'] = []
    for i in result:
        d['ques'].append({
            'pro_id': i[0],
            'pro_stem': i[1],
            'choice' : i[2],
            'answer': i[3],
            'flag': i[4],
            'pro_num': i[5],
        })
    resp['data'] = d
    print(resp['data'])
    return jsonify(resp)


@app.route('/login')
def login():
    print('show login page')
    return render_template('login.html')

@app.route('/root_index')
def root_index():
    return render_template('root_index.html', Msg="您现在处于root用户界面")
@app.route('/index')
def index():
    return render_template('index.html', Msg="您现在处于教师界面")

@app.route('/dologin')
def dologin():
    print('dologin')
    print(request.args)
    id = request.args['id']
    password = request.args['password']
    print(id, password)
    sql = "select count(*) from teacher_info where tea_id='%s' and password='%s'" %(id, password)
    cursor.execute(sql)
    #不存在
    if cursor.fetchone()[0] == 0:
        return render_template('login.html', errMsg="登陆失败，检查账号和密码")
    else:
        session['tea_id'] = id
        if id == '00001':
            return render_template('root_index.html', Msg="您现在处于root用户界面")
        else:
            return render_template('index.html', Msg="您现在处于教师界面")

@app.route('/logout')
def logout():
    session['tea_id'] = ''
    return render_template('login.html', errMsg="你已注销，请重新登陆")

@app.route('/showclass')
def showclass():
    print("sssion", session['tea_id'])
    sql = "select class_id,class_name, start_time, end_time, stage from class_info where tea_id='%s'" % session['tea_id']
    cursor.execute(sql)
    classinfo = []
    for i in cursor.fetchall():
        classinfo.append({
            'class_id': i[0],
            'class_name': i[1],
            'start_time': str(i[2]),
            'end_time': str(i[3]),
            'stage': str(i[4])
        })
    return render_template('showclass.html', classinfo=classinfo, tea_id=session['tea_id'])

@app.route('/nextPercourse/<class_id>')
def nextPercourse(class_id):
    print(class_id)
    sql = "update class_info set stage = stage+1 where class_id='%s'" % class_id
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        pass
    return redirect(url_for('showclass'))

@app.route('/showStuByClassid/<class_id>')
def showStuByClassid(class_id):
    print(class_id)
    stu_info = []
    sql = "select A.stu_id,credit from student_info as A inner join inclass as B on A.stu_id=B.stu_id where class_id='%s'" % class_id
    cursor.execute(sql)
    for i in cursor.fetchall():
        stu_info.append({
            'stu_id': i[0],
            'credit': i[1]
        })
    return render_template('showstudent.html', stu_info=stu_info)

@app.route('/showteacher')
def showteacher():
    sql = "select tea_id, tea_email, tea_name, teacher_intro, password from teacher_info where tea_id != '00001' order by tea_id"
    cursor.execute(sql)
    teacherinfo = []
    for i in cursor.fetchall():
        teacherinfo.append({
            'tea_id':i[0],
            'tea_email': i[1],
            "tea_name" : i[2],
            "tea_intro": i[3],
            'password': i[4]
        })
    return render_template('showteacher.html', teacherinfo=teacherinfo)

@app.route('/modifyteacher/<tea_id>')
def modifyteacher(tea_id):
    print(tea_id)
    return render_template('modifyteacher.html', tea_id=tea_id)

@app.route('/demodifyteacher/<tea_id>')
def domodifyteacher(tea_id):
    print(request.args)
    newpassword = "'"+request.args['newpassword']+"'" if request.args['newpassword'] else 'password'
    newemail = "'" + request.args['newemail'] + "'"if request.args['newemail'] else 'tea_email'
    newname = "'"+ request.args['newname'] + "'"if request.args['newname'] else 'tea_name'
    newintro = "'" + request.args['newintro'] + "'" if request.args['newintro'] else 'teacher_intro'
    sql = "update teacher_info set password=%s,tea_email=%s, tea_name=%s, teacher_intro=%s where tea_id='%s'" % (newpassword,newemail,newname,newintro,tea_id)
    print(sql)
    try:
        cursor.execute(sql)
        conn.commit()
        return redirect(url_for('showteacher'))
    except:
        return render_template('modifyteacher.html', tea_id=tea_id, msg="修改失败")

@app.route('/addteacher')
def addteacher():
    print('add teacher')
    return render_template('addteacher.html')
@app.route('/doaddteacher')
def doaddteacher():
    print('doaddteacher')
    id = request.args['id']
    if id == '':
        return render_template('addteacher.html', msg='添加失败，id为空')
    password = request.args['password']
    email = request.args['email']
    name = request.args['name']
    intro = request.args['intro']
    sql = "insert into teacher_info(tea_id,tea_email,tea_name,password,teacher_intro) values('%s','%s','%s','%s','%s')" %(id,email,name,password,intro)
    try:
        cursor.execute(sql)
        conn.commit()
        return redirect(url_for('showteacher'))
    except:
        return render_template('addteacher.html', msg='添加失败，id重复')

@app.route('/delteacher/<tea_id>')
def delteacher(tea_id):
    print(tea_id)
    sql = "delete from teacher_info where tea_id='%s'" % tea_id
    cursor.execute(sql)
    conn.commit()
    return redirect(url_for('showteacher'))




@app.route('/showsetcourse')
def showsetcourse():
    sql = "select scourse_id,scourse_title,scourse_theme,scourse_intro,scourse_credit,scourse_price from setcourse_info"
    info = []
    cursor.execute(sql)
    for i in cursor.fetchall():
        info.append({
            'id': i[0],
            'title': i[1],
            'theme': i[2],
            'intro': i[3],
            'credit': i[4],
            'price': i[5]
        })
    return render_template('showsetcourse.html', setcourse_info=info)

@app.route('/modifysetcourse/<scourse_id>')
def modifysetcourse(scourse_id):
    return render_template('modifysetcourse.html', scourse_id=scourse_id)

@app.route('/demodifysetcourse/<scourse_id>')
def domodifysetcourse(scourse_id):
    print(request.args)
    newtitle = "'" + request.args['newtitle'] + "'" if request.args['newtitle'] else 'scourse_title'
    newtheme = "'" + request.args['newtheme'] + "'" if request.args['newtheme'] else 'scourse_theme'
    newprice = "'" + request.args['newprice'] + "'" if request.args['newprice'] else 'scourse_price'
    newcredit = "'" + request.args['newcredit'] + "'" if request.args['newcredit'] else 'scourse_credit'
    newintro = "'" + request.args['newintro'] + "'" if request.args['newintro'] else 'scourse_intro'
    sql = "update setcourse_info set scourse_title=%s,scourse_theme=%s,scourse_price=%s, scourse_credit=%s ,scourse_intro=%s where scourse_id='%s'" % (
    newtitle, newtheme, newprice, newcredit, newintro, scourse_id)
    print(sql)
    try:
        cursor.execute(sql)
        conn.commit()
        return redirect(url_for('showsetcourse'))
    except:
        return render_template('modifysetcourse.html', scourse_id=scourse_id, msg="修改失败")

@app.route('/addsetcourse')
def addsetcourse():
    print('add setcourse')
    return render_template('addsetcourse.html')

@app.route('/doaddsetcourse')
def doaddsetcourse():
    print('doaddsetcourse')
    id = request.args['id']
    if id == '':
        return render_template('addsetcourse.html', msg='添加失败，id为空')
    title = request.args['title']
    theme = request.args['theme']
    credit = request.args['credit']
    price = request.args['price']
    intro = request.args['intro']
    sql = "insert into setcourse_info(scourse_id,scourse_title,scourse_theme,scourse_intro,scourse_credit,scourse_price)"\
          +" values('%s','%s','%s','%s','%s','%s')" % (id,title,theme,intro,credit,price)
    try:
        cursor.execute(sql)
        conn.commit()
        return redirect(url_for('showsetcourse'))
    except:
        return render_template('addsetcourse.html', msg='添加失败，id重复')

@app.route('/delscourse/<scourse_id>')
def delscourse(scourse_id):
    print(scourse_id)
    sql = "delete from setcourse_info where scourse_id='%s'" % scourse_id
    cursor.execute(sql)
    conn.commit()
    return redirect(url_for('showsetcourse'))

@app.route('/showques')
def showques():
    print('题库管理')
    if 'pcourse_id' in request.args:
        pid = request.args['pcourse_id']
    else:
        pid = ''
    print('&&&'+pid+'pid')
    pat = '%'+pid+'%'
    ques = []
    sql = "select pro_id, pro_stem,choice,answer,flag,pcourse_id,pro_num from problems where pcourse_id like '%s'" % pat
    print(sql)
    cursor.execute(sql)
    for i in cursor.fetchall():
        ques.append({
            'pro_id':i[0],
            'pro_stem':i[1],
            'choice':i[2],
            'answer':i[3],
            'flag':i[4],
            'pcourse_id': i[5],
            # 'pcourse_id':i[5].replace(pid, '<span style="color:#F00">'+pid+'</span>') if pid != '' else i[5],
            'pro_num':i[6]
        })

    return render_template('showques.html', ques = ques)

@app.route('/delques')
def delques():
    pro_id = request.args['pro_id']
    print(pro_id)
    sql = "delete from  problems where pro_id='%s'" % pro_id
    cursor.execute(sql)
    conn.commit()
    return redirect(url_for('showques'))

@app.route('/addques')
def addques():
    print("add questions")
    return render_template('addques.html')

@app.route('/doaddques')
def doaddques():
    pass



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

