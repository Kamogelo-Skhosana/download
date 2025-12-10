from pytubefix import YouTube
from flask import Flask, request, send_file


@app.route('/hello')
def pp():
    link = request.get("https://music.youtube.com/watch?v=-iYZ_qWe8kc")
    yt = YouTube(link)
    ys = yt.streams.get_audio_only()
    return ys.download()