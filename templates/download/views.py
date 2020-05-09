from __future__ import unicode_literals
from flask import (
    render_template, Blueprint, request,
    send_file, make_response
)
import youtube_dl
import os

download_blueprint = Blueprint('download',__name__)

DOWNLOAD_PATH = '/home/gabrielslotti/Downloads/YoutubeDownloads/'

@download_blueprint.route('/download')
def download():
    url = request.args.get('url')
    type_ = request.args.get('type')

    if type_ == 'video':
        ydl_opts = {
            'outtmpl': DOWNLOAD_PATH+'%(title)s.%(ext)s',
            'format': 'bestvideo[ext=mp4]+bestaudio',
            'merge_output_format': 'mkv'
        }
    if type_ == 'audio':
        ydl_opts = {
            'outtmpl': DOWNLOAD_PATH+'%(title)s.%(ext)s',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
            }],
            'prefer_ffmpeg': True,
        }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        video_file = ydl.download([url])

    _file = os.listdir(DOWNLOAD_PATH)[0]

    return make_response(send_file(DOWNLOAD_PATH+_file, as_attachment=True, attachment_filename=_file), os.remove(DOWNLOAD_PATH+_file))
