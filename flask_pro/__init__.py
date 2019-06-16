# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, redirect
from config import databaseconfig as dc

conn = dc.conn
cursor = conn.cursor()
app = Flask(__name__)

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

@app.route('/funid3')
def funid3():
    resp = {'code': 200,'msg': '操作成功', 'data': {}}
    resp['data'] ={
        "courseId": 20190223,
        "classId": 1936,
        "classTitle": "标题示例",
        "classContent": "课程内容 关于本节课必要的文字说明",
        "classWorks": "作业描述 如作业要求等具体要求",
        "classEndTime": "2020-02-23",
        "classVideoUrl": "#",
        "worksSub": [],
        "worksObj": []
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
    resp = {'code': 200, 'msg': '操作成功', 'data': []}
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
            'pageImgUrls': 'https://i.loli.net/2019/02/08/5c5d63058df87.png'
        })
    resp['data'] = res
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


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

