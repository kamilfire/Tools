import yt_dlp
import os
import re


def limpiar_nombre_archivo(nombre):
    """Limpia caracteres problemáticos para nombres de archivo."""
    return re.sub(r'[\\/*?:"<>|]', "", nombre)


def descargar_musica(url):
    try:
        # Configuración de opciones para yt-dlp
        opciones = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': '%(title)s.%(ext)s',
            'no_color': True,
            'ffmpeg_location': '/usr/bin/ffmpeg',  # Cambia esto a la ruta correcta
        }

        # Crear instancia de yt-dlp
        with yt_dlp.YoutubeDL(opciones) as ydl:
            # Obtener información del video
            info = ydl.extract_info(url, download=False)
            titulo_video = limpiar_nombre_archivo(info['title'])
            archivo_salida = f"{titulo_video}.mp3"

            # Verificar si ya existe el archivo
            if os.path.exists(archivo_salida):
                print(f"El archivo '{archivo_salida}' ya existe. Saltando descarga.")
                return

            # Descargar el audio
            print(f"Descargando: {titulo_video}")
            ydl.download([url])
            print("Descarga completada exitosamente.")

    except yt_dlp.utils.DownloadError as e:
        if "Video unavailable" in str(e):
            print("El video no está disponible. Puede que el canal haya sido eliminado o el video esté restringido.")
        else:
            print(f"Error al descargar el video: {e}")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")


def main():
    print("Descargador de música de YouTube")
    url = input("Por favor, introduce la URL del video de YouTube: ").strip()

    # Validar la URL básica
    if not re.match(r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+', url):
        print("La URL ingresada no es válida. Por favor, inténtalo de nuevo.")
        return

    descargar_musica(url)


if __name__ == "__main__":
    main()
