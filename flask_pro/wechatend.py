# -*- coding: utf-8 -*-
from flask import Flask,request,jsonify
from config import databaseconfig as dc

conn = dc.conn
cursor = conn.cursor()
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"


@app.route('/getcourses')
def funid2():
    resp = {'code': 200,'msg': '操作成功', 'data': []}
    sql = "select pcourse_id,pcourse_intro,pcourse_name,pcourse_intro,vedio_url from percourse_info"
    cursor.execute(sql)
    d = cursor.fetchall()
    for i in d:
        t = {}
        t['pcourse_id'] = i[0]
        t['percourse_info'] = i[1]
        t['pcourse_name'] = i[2]
        t['pcourse_intro'] = i[3]
        t['vedio_url'] = i[4]
        resp['data'].append(t)
    return jsonify(resp)






if __name__ == '__main__':
    app.run(host = "0.0.0.0",debug = True)

