# -*- coding: utf-8 -*-
from flask import Flask,request,jsonify
from config import databaseconfig as dc

conn = dc.conn
cursor = conn.cursor()
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/funid2')
def funid2():
    resp = {'code': 200, 'msg': '操作成功', 'data': {}}
    t = {}
    t['courseId'] = 'IDfromback'
    t['courseTitle'] = 'titlefrom'
    t['coursePrice'] = '100000.00'
    t['time'] = '2019:00:12'
    t['courseContent'] = 'contenrrrrr'
    resp['data'] = t
    return jsonify(resp)

@app.route('/funid0')
def funid0():
    resp = {'code': 200,'msg': '操作成功', 'data': []}
    req = request.values
    openid = req['openid'] if 'openid' in req else None
    course = []
    c1 = {
        "pageImgUrls": "https://i.loli.net/2019/02/08/5c5d63058df87.png",
        "courseTitle": "course_title_2",
        "courseIntro": "course_intro_2",
        "courseLinks": "course_links_2",
        "Course_ID": "654321"
    }
    c2 = {
        "pageImgUrls": "https://i.loli.net/2019/02/08/5c5d63058df87.png",
        "courseTitle": "course_title_1",
        "courseIntro": "course_intro_1",
        "courseLinks": "course_links_1",
        "Course_ID": "123456"
    }
    course.append(c1)
    course.append(c2)
    resp['data'] = course
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
    resp['data'] = {
        "courseId": 20190223,
        "courseTitle": "标题示例",
        "coursePrice": 0,
        "time":"2019-02-23",
        "courseContent": "这是一段课程内容简介",
        "teacherIntro": "这是一段教师简介"
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


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

