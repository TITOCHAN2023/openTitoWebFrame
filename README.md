1. 

   # 关于框架的选择

   >这是萌新博主的学习之路 代码中可能拿取其他大佬的开源代码进行装饰


   我定下的目标是搭建一个个人博客，所以打算用flask框架来搭建后端

   还有nginx与uwsgi

   至于前端就采用老三样css html js

   # 提前准备

   ## linux服务器 

   操作系统：Ubantu20

   阿里云默认安装mysql8.0版本，python3.8（本人的linux环境）

   博主的项目叫titoweb 根据个人项目名更改 后续所有titoweb皆是如此

   ## nginx

   ### 更新安装源

   ```sudo apt update```

   ### 安装nginx

   ```apt install nginx```

   ### nginx配置

   ```
   upstream titoweb {
       server unix:///srv/titoweb/titoweb.sock;
   }
   # 配置服务器
   server {
       # 监听的端口号
       listen      80;
       # 域名
       server_name titochan.top;
       charset     utf-8;
   
   
       # 静态文件访问的url
       location /static {
           # 静态文件地址
           alias /srv/titoweb/static; 
       }
   
       # 最后，发送所有非静态文件请求到uwsgi服务器
       location / {
           uwsgi_pass  titoweb;
           # uwsgi_params文件地址
           include     /etc/nginx/uwsgi_params;
       }
   }
   ```

   ### 测试nginx

   ```service nginx configtest```

   重启nginx

   service nginx restart
   nginx 常用命令

   启动：service nginx start
   关闭：service nginx stop
   重启：service nginx restart
   测试配置文件：service nginx configtest

   

   

   ## Mysql

   ### 换源安装MySQL5.7

   ```cp /etc/apt/sources.list /etc/apt/sources.list.bak```
   编辑
   ```vim /etc/apt/sources.list```

   镜像地址

   ```
   deb http://mirrors.ustc.edu.cn/ubuntu/ xenial main restricted universe multiverse
   deb http://mirrors.ustc.edu.cn/ubuntu/ xenial-security main restricted universe multiverse
   deb http://mirrors.ustc.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
   deb http://mirrors.ustc.edu.cn/ubuntu/ xenial-proposed main restricted universe multiverse
   deb http://mirrors.ustc.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
   deb-src http://mirrors.ustc.edu.cn/ubuntu/ xenial main restricted universe multiverse
   deb-src http://mirrors.ustc.edu.cn/ubuntu/ xenial-security main restricted universe multiverse
   deb-src http://mirrors.ustc.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
   deb-src http://mirrors.ustc.edu.cn/ubuntu/ xenial-proposed main restricted universe multiverse
   deb-src http://mirrors.ustc.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
   ```

   更新安装源

   ```sudo apt update```

   ### mysql 安装

   ```sudo apt install mysql-server mysql-client```


   ## 虚拟环境安装

   ### 更新pip

   ```pip3 install --upgrade pip```

   ### 安装虚拟环境管理包

   ```pip install virtualenvwrapper```

   ### 虚拟环境配置

   ```
   export WORKON_HOME=$HOME/.virtualenvs
   VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
   source /usr/local/bin/virtualenvwrapper.sh
   ```

   执行命令

   ```source ~/.bashrc```

   ### 创建虚拟环境

   ```mkvirtualenv --python=/usr/bin/python3 titoweb_env```


   ## uwsgi安装

   ### 安装uwsgi

   ```pip install uwsgi```

   路径：/srv/titoweb/uwsgi.ini

   ### 配置uwsgi

   ```
   [uwsgi]
   # 项目的路径
   chdir           = /srv/titoweb/
   # Flask的uwsgi文件
   wsgi-file       = /srv/titoweb/app.py
   # 回调的app对象
   callable        = app
   # Python虚拟环境的路径
   home            = /root/.virtualenvs/titoweb_env
   
   # 进程相关的设置
   # 主进程
   master          = true
   # 最大数量的工作进程
   processes       = 1
   
   http            = :80
   
   socket          = /srv/titoweb/titoweb.sock
   
   # 设置socket的权限
   chmod-socket    = 666
   # 退出的时候是否清理环境
   vacuum          = true
   
   ```

   ### 启动运行uwsgi

   ```uwsgi --ini uwsgi.ini```

   ## 提前准备注意事项

   以后更改后只需重启uwsgi即可

   # flask框架使用 

   在这里博主做了一个简单的随机音乐播放
   python这边学习一下flask框架就基本没啥问题
   为了保证切歌效果即不刷新网站 
   博主采用返回json
   让前端自动刷新音乐、专辑图片路径

   ```python
   from flask import Flask, render_template, request, jsonify
   import random
   
   app = Flask(__name__)
   
    # 音乐文件列表
   music_list = ['static/music/*.mp3'] 
   
   @app.route("/")
   def index():
       return render_template("index.html")
   
   
   @app.route('/bgm')
   def bgm():
      
       # 随机切歌
       random_music = random.choice(music_list)
   
       
        # 拼接带有随机参数的图片路径
       if random_music.startswith('static/music/*.mp3'):
           pic = "static/*.JPG"
           
   
       return render_template('bgm.html', music=random_music,pic=pic)
   
   
   @app.route('/get_new_music', methods=['GET'])
   def get_new_music():
       # 在这里编写获取新歌曲的逻辑
       random_music = random.choice(music_list)
       
        # 拼接带有随机参数的图片路径
       if random_music.startswith('static/music/*.mp3'):
           pic = "static/*.JPG"
           
       # 返回JSON数据
       return jsonify(music=random_music, pic=pic)
   
   if __name__ == '__main__':
       app.run()
   ```

   # 前端以及遇到的问题

   ## index.html

   为访问博主主页
   在其中增加了音乐按钮
   使其可以自动跳转至bgm.html

   ## bgm.html

   ### 按钮

   简单做了一个按钮 去切歌

   ```html
   <audio  autoplay loop id="background-music">
                 <source src="{{ music }}" >
   </audio>
   <button onclick="changeMusic()">RANDOM NEXT</button>
   ```

    专辑图片显示
    
    ```html
   <img   src="{{pic}}" id="myImage">
    ```

   ### 处理python返回的json文件

   创建一个XMLHttpRequest对象xhr，指定了在状态改变时触发的回调函数。

   在回调函数中，首先检查响应的状态和HTTP状态码，

   如果都符合要求，则解析响应文本中的新歌曲路径。然后，将新歌曲的路径赋值给audio.src。

   专辑图片同理

   在切换歌曲时，通过调用xhr.open方法向Flask服务器发送GET请求获取新歌曲，

   然后调用xhr.send方法发送请求。

   ```html
   <script>
           function changeMusic() {
               var audio = document.getElementById('background-music');
               var image = document.getElementById('myImage');
               var xhr = new XMLHttpRequest();
               xhr.onreadystatechange = function() {
                   if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                       var newMusic = JSON.parse(xhr.responseText).music;
                       var newSrc = JSON.parse(xhr.responseText).pic;
                       image.src = newSrc;
                       audio.src = newMusic;
                   } else {
                       console.log('Error: ' + xhr.status);
                   }
               };
               
               xhr.open('GET', '/get_new_music', true);
               xhr.send();
   
           }
   </script>
   ```

   ### 图片移动端和PC端的显示优化

   采用了一个阈值

   ```css
   img {
         width: 40%;
         height: auto;
   }
   @media (max-width: 600px) {
     /* 在窄屏设备上应用的样式 */
     img {
       width: 60%;
       height: auto;
     }
   }
   ```

  
