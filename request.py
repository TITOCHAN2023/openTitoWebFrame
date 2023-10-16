from flask import Flask,  render_template, request, jsonify
from app import app
import mysql as mysql


@app.route('/get_comments/<title>', methods=['GET'])
def get_comments(title):
    
    
    q=list(mysql.MR(f"{title}"))
    print(q)
    print(q[-1][0])
    num=q[-1][0]
    return jsonify(data=q,num=num)

@app.route('/ping/<title>', methods=['POST'])
def ping(title):
    table = title
    ip = request.remote_addr
    name = request.form['name']
    text = request.form['data']
    
    if text.strip() == '' or name.strip() == '':
        error_message = '''
<!DOCTYPE html>
<html lang="en">

<head>
    <link rel="icon" href="/static/pic/logo.png" href="/favicon.ico">
    <meta charset="UTF-8">
    <title>提交失败</title>
    <link rel="stylesheet" href="{{ url_for('static',filename='css/index.css')}}">
</head>

<body>

    <div align="center">
        <h1>名称或内容不能为空哦</h1>
        <h1>小老弟</h1>
        <img src="\static\pic\5623.JPG">
    </div>
</body>

</html>
        '''
        return error_message

    # 在这里你可以对数据进行处理
    mysql.MI(table, name, ip, text)
    
    return  render_template(f"/article/{title}.html")
    
