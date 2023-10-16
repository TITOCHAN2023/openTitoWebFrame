from flask import Flask,  render_template, request, jsonify
from app import app
import random
from config import music_list



@app.route('/bgm')
def bgm():

    # 随机切歌
    random_music = random.choice(music_list)

    # 拼接带有随机参数的图片路径
    if random_music=='static/music/**.mp3':
        pic = "static/pic/**.JPG"

    return render_template('bgm.html', music=random_music, pic=pic)


@app.route('/get_new_music', methods=['GET'])
def get_new_music():
    # 在这里编写获取新歌曲的逻辑
    random_music = random.choice(music_list)

    # 拼接带有随机参数的图片路径
    if random_music=='static/music/**.m4a':
        pic = "static/pic/**.png"

    # 返回JSON数据
    return jsonify(music=random_music, pic=pic)