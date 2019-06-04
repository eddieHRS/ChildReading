# -*- coding: utf-8 -*-
from flask import Flask,request,jsonify
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
@app.route('/buyset')
def buyset():
    resp = {'code': 200, 'msg': '操作成功', 'data': {}}
    set_classList = ['《七只瞎老鼠》','《拼拼凑凑的变色龙》','《你很特别》','《黎明》','《迟到大王》']
    set_teacher = '叶凤春老师'
    temp = {'set_classList': set_classList, 'set_teacher': set_teacher}
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

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

