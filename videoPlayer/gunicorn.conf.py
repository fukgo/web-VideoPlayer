bind = '127.0.0.1:8080'  # 绑定的IP地址和端口
workers = 4  # 工作进程数
wsgi_app = 'videoPlayer.wsgi:application'
