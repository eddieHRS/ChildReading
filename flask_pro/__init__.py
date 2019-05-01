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

# @app.route('/funid0')
# def funid0():
#     resp = {'code': 200,'msg': '操作成功', 'data': []}
#     req = request.values
#     openid = req['openid'] if 'openid' in req else None
#     if openid is None:
#         resp['code'] = 400
#         resp['msg'] = 'openid 不存在或者没有获得openid'
#     else:
#         d = cursor.execute("select * from setclass_info").fetchall()
#         for i in d:
#             t = {}
#             t['Course_ID'] = i[0]
#             t['courseTitle'] = i[1]
#             t['pageImgUrls'] = i[2]
#             t['courseIntro'] = i[3]
#             t['courseLinks'] = i[4]
#             resp['data'].append(t)
#     return jsonify(resp)
#
# @app.route('/funid1')
# def funid1():
#     resp = {'code': 200,'msg': '操作成功', 'data': {}}
#     req = request.values
#     openid = req['openid'] if 'openid' in req else None
#     if openid is None:
#         resp['code'] = 400
#         resp['msg'] = 'openid 不存在或者没有获得openid'
#     else:
#         d = cursor.execute("select * from setclass_info limit 3").fetchall()
#         for i in d:
#             resp['data']['imgUrls'].append(i[2])
#             resp['data']['pageImgUrls'].append(i[2])
#             resp['data']['courseTitle'].append(i[1])
#             resp['data']['courseLinks'].append(i[4])
#     return jsonify(resp)


if __name__ == '__main__':
    app.run(host = "0.0.0.0",debug = True)

