from scapy.all import *
from scapy.layers.dot11 import Dot11, Dot11Beacon, Dot11ProbeResp
import threading
import os

# Diccionario para almacenar redes detectadas
networks = {}

def packet_handler(packet):
    """
    Función que maneja los paquetes capturados.
    Detecta tramas Beacon y Probe Response para listar redes.
    """
    if packet.haslayer(Dot11Beacon) or packet.haslayer(Dot11ProbeResp):
        ssid = packet.info.decode(errors="ignore") if packet.info else "<SSID Oculto>"
        bssid = packet.addr2

        if bssid not in networks:
            networks[bssid] = ssid
            print(f"Red detectada: BSSID={bssid}, SSID={ssid}")

def stop_sniffing():
    """
    Función para detener el escaneo después de un tiempo específico y guardar los resultados.
    """
    print("\n[+] Escaneo terminado. Aquí están las redes encontradas:")
    
    # Guardar resultados en un archivo
    with open("te_encontre.txt", "w") as file:
        file.write("Redes Wi-Fi detectadas:\n")
        file.write("="*30 + "\n")
        for bssid, ssid in networks.items():
            file.write(f"BSSID: {bssid}, SSID: {ssid}\n")
            print(f"BSSID: {bssid}, SSID: {ssid}")

    print("\n[+] Resultados guardados en el archivo 'te_encontre.txt'")
    os._exit(0)  # Detener todo el script

def main():
    """
    Función principal que inicia el escaneo.
    """
    interface = input("Introduce la interfaz en modo monitor (e.g., wlan0mon): ")

    # Límite de tiempo para el escaneo en segundos (4 minutos)
    scan_time = 240

    # Mostrar mensaje de inicio
    print(f"Escaneando redes Wi-Fi por {scan_time} segundos...\n")

    # Inicia el temporizador para detener el escaneo
    threading.Timer(scan_time, stop_sniffing).start()

    # Comenzar captura de paquetes
    try:
        sniff(iface=interface, prn=packet_handler, store=0)
    except KeyboardInterrupt:
        print("\n[-] Escaneo interrumpido por el usuario.")
        stop_sniffing()

if __name__ == "__main__":
    main()

