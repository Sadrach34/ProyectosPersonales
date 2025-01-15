#Sadrach Juan Diego Garcia Flores
#Fecha: 13/11/2024
#Descripcion: Programa que descarga videos de youtube utilizando la libreria de yt-dlp
#Esta version hare que funcione como un servidor api de pyhton para hacer peticiones de descarga de videos desde kotlin
#Para ello hare uso de la libreria flask.

# servidor_descargas.py
from flask import Flask, request, jsonify
import yt_dlp as yt

app = Flask(__name__)

@app.route('/descargar_video', methods=['POST'])
def descargar_video():
    url = request.json.get('url')
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': 'descargas/%(title)s.%(ext)s',
        'merge_output_format': 'mp4'
    }
    try:
        with yt.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return jsonify({"mensaje": "Descarga completada"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/descargar_audio', methods=['POST'])
def descargar_audio():
    url = request.json.get('url')
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'descargas/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        with yt.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return jsonify({"mensaje": "Descarga completada"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
