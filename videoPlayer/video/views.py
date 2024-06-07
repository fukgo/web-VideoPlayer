import mimetypes
import os
import re
from wsgiref.util import FileWrapper

import cv2
from django.conf import settings
from django.http import StreamingHttpResponse
from django.shortcuts import render

dir_path = settings.VIDEOS_DIR


def index(request):
    return render(request, 'index.html')


def get_video_list(directory):
    """获取视频文件列表"""
    video_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            mimetype = mimetypes.guess_type(file)[0]
            if mimetype and mimetype.startswith('video'):
                new_li = {}
                file_path = os.path.abspath(os.path.join(root, file))
                file_name = str(file)
                img_name = 'media/pre-img/{}.png'.format(file_name)
                if os.path.exists(img_name):
                    img_exist = True
                else:
                    cap = cv2.VideoCapture(file_path)
                    ret, frame = cap.read()
                    if not ret:
                        img_exist = False
                        img_name = None
                    else:
                        img_exist = cv2.imwrite(img_name, frame)
                new_li['file_name'] = file_name
                new_li['img_exist'] = img_exist
                new_li['img_path'] = img_name
                new_li['file_path'] = file_path
                video_list.append(new_li)
    return video_list


def get_video_list_no_img(directory):
    video_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            mimetype = mimetypes.guess_type(file)[0]
            if mimetype and mimetype.startswith('video'):
                new_li = {}
                file_path = os.path.abspath(os.path.join(root, file))
                file_name = str(file)
                new_li['file_name'] = file_name
                new_li['file_path'] = file_path
                video_list.append(new_li)
    return video_list


def video_list_2(request):
    videos = get_video_list_no_img(dir_path)
    length = len(videos)
    return render(request, 'video_list_2.html', {'videos': videos, 'length': length})


def video_list(request):
    videos = get_video_list(dir_path)
    length = len(videos)
    return render(request, 'video_list.html', {'videos': videos, 'length': length})


def file_iterator(file_name, chunk_size=8192, offset=0, length=None):
    with open(file_name, "rb") as f:
        f.seek(offset, os.SEEK_SET)
        remaining = length
        while True:
            bytes_length = chunk_size if remaining is None else min(remaining, chunk_size)
            data = f.read(bytes_length)
            if not data:
                break
            if remaining:
                remaining -= len(data)
            yield data


def stream_video(request, file_path):
    """将视频文件以流媒体的方式响应"""
    range_header = request.META.get('HTTP_RANGE', '').strip()
    range_re = re.compile(r'bytes\s*=\s*(\d+)\s*-\s*(\d*)', re.I)
    range_match = range_re.match(range_header)
    size = os.path.getsize(file_path)
    content_type, encoding = mimetypes.guess_type(file_path)
    content_type = content_type or 'application/octet-stream'
    if range_match:
        first_byte, last_byte = range_match.groups()
        first_byte = int(first_byte) if first_byte else 0
        last_byte = first_byte + 1024 * 1024 * 10
        if last_byte >= size:
            last_byte = size - 1
        length = last_byte - first_byte + 1
        resp = StreamingHttpResponse(file_iterator(file_path, offset=first_byte, length=length), status=206,
                                     content_type=content_type)
        resp['Content-Length'] = str(length)
        resp['Content-Range'] = 'bytes %s-%s/%s' % (first_byte, last_byte, size)
    else:
        resp = StreamingHttpResponse(FileWrapper(open(file_path, 'rb')), content_type=content_type)
        resp['Content-Length'] = str(size)
    resp['Accept-Ranges'] = 'bytes'
    return resp


def dplayer(request, file_path):
    return render(request, 'dplayer.html', {'file_path': file_path})
