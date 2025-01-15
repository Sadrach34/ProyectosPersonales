import yt_dlp as yt
from MisFunciones_2024 import *

class Descarga:
    @staticmethod
    def video(url):
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': 'descargas/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
        }
        try:
            print(f"Iniciando descarga de video: {url}")
            with yt.YoutubeDL(ydl_opts) as ytd:
                ytd.download([url])
            print("Descarga de video completada")
        except Exception as e:
            print(f"Error al descargar el video: {e}")

    @staticmethod
    def audio(url):
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'descargas/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        }
        try:
            print(f"Iniciando descarga de audio: {url}")
            with yt.YoutubeDL(ydl_opts) as ytd:
                ytd.download([url])
            print("Descarga de audio completada")
        except Exception as e:
            print(f"Error al descargar el audio: {e}")

while True:
    Cls()
    print("Descargar videos de youtube")
    print("1.- Descargar video")
    print("2.- Descargar audio")
    print("3.- Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        url = input("Ingrese la URL del video: ")
        Descarga.video(url)
        Cls()
        print("Descarga completada")
        pausa("Presione una tecla para continuar")
    elif opcion == '2':
        url = input("Ingrese la URL del video: ")
        Descarga.audio(url)
        Cls()
        print("Descarga completada")
        pausa("Presione una tecla para continuar")
    elif opcion == '3':
        break
    else:
        print("Opción no válida")

# Asegúrate de tener yt_dlp instalado
# pip install yt-dlp

# Asegúrate de que la carpeta 'descargas' exista
# mkdir descargas