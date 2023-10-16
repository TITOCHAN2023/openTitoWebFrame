from flask import Flask, render_template, request, jsonify
import gpt 
import where
import mysql
from app import app


@app.route('/send', methods=['POST'])
def send():
    message = request.form['message']
    ip = request.remote_addr
    city = where.getWhere(ip)
    Where =f"{city['prov']}-{city['city']}"

    q=list(mysql.MR("AI"))
    
    jishu=0
    for i in q:
        if ip in i:
            jishu+=1
            print(jishu)

    if jishu<=5:
        

        mysql.MI("AI",Where,ip,message)

        print(f"form {ip}:{message}")
        response_message = gpt.gpt(message)
    else:
        response_message ="你已经提问五次了，下次再来吧"


    
    response_message+="\n 回答来自："+Where+"的问题"

    return jsonify(msg=response_message)