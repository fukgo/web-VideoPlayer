from waitress import serve

from videoPlayer.wsgi import application

serve(
    app=application,
    host='127.0.0.1',
    port=8000,
    threads=16,
)
'''channel_timeout：这个选项设置了服务器等待一个请求完成的最长时间（以秒为单位）。如果你的应用需要处理一些耗时的请求，或者你的网络连接不稳定，你可能需要增加这个值。否则，如果一个请求的处理时间超过了这个值，Waitress会关闭这个请求的连接。  
max_request_body_size：这个选项设置了服务器可以接受的请求体的最大大小（以字节为单位）。如果你需要处理大文件上传，你可能需要增加这个值。否则，如果一个请求的请求体大小超过了这个值,Waitress会拒绝这个请求'''
