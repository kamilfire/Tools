import speedtest

def medir_velocidad():
    try:
        print("Iniciando prueba de velocidad...")

        # Crear un objeto Speedtest
        prueba = speedtest.Speedtest()

        # Obtener el mejor servidor
        mejor_servidor = prueba.get_best_server()

        # Obtener información del ISP
        isp = mejor_servidor['sponsor']  # Nombre del proveedor de Internet

        print(f"Proveedor de Internet (ISP): {isp}")

        print("Midiendo velocidad de descarga...")
        velocidad_descarga = prueba.download() / 1_000_000  # Convertir a Mbps

        print("Midiendo velocidad de subida...")
        velocidad_subida = prueba.upload() / 1_000_000  # Convertir a Mbps

        print("Midiendo latencia (ping)...")
        ping = mejor_servidor['latency']  # Latencia en ms desde el servidor seleccionado

        print("\nResultados:")
        print(f"Proveedor de Internet (ISP): {isp}")
        print(f"Velocidad de descarga: {velocidad_descarga:.2f} Mbps")
        print(f"Velocidad de subida: {velocidad_subida:.2f} Mbps")
        print(f"Ping: {ping:.2f} ms")

    except Exception as e:
        print(f"Error al medir la velocidad: {e}")

if __name__ == "__main__":
    medir_velocidad()
