### 功能：将一个文件夹中所有视频文件展示到web网页上，通过局域网（外网需要公网ip或者内网穿透等功能）可以观看该文件夹中的所有视频

##### 实现原理：django+nginx+Dplayer+waitress

实现效果：

![image](https://github.com/fukgo/web-VideoPlayer/tree/main/videoPlayer/readme_img/home.png)

![image](https://github.com/fukgo/web-VideoPlayer/tree/main/videoPlayer/readme_img/list.png)

![image](https://github.com/fukgo/web-VideoPlayer/tree/main/videoPlayer/readme_img/video.png)

##### 前提：

1. clone 本项目到一个文件夹中

2. 安装好nginx（也可以自己使用apache等等）

3. 更改videoPlayer.settings

   ```python
   # 包含所有视频的文件夹(需要更改为自己的视频文件夹)
   VIDEOS_DIR = 'D://dowload//'
   #改为自己想要安放视频的文件夹的路径
   ```


4. 按照项目中nginx.conf配置文件进行更改nginx配置文件

5. 在项目目录中开启waitress命令来开启django服务
   ```cmd
   python waitress-run.py
   ```

6. 开启nginx服务,在nginx文件夹的cmd中
   ```cmd
   nginx.exe 
   ```

浏览器访问`本机ip:888`即可看到页面。
*例如在手机端访问电脑ip+port`192.168.124.2：888`*
