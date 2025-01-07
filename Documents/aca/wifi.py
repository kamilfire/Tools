import subprocess
import re


def run_arp_scan(ip_range):
    """Ejecuta arp-scan para buscar dispositivos en el rango."""
    try:
        # Ejecuta arp-scan
        result = subprocess.run(['sudo', 'arp-scan', ip_range], capture_output=True, text=True)
        if result.returncode != 0:
            print("Error al ejecutar arp-scan. Asegúrate de que esté instalado y de tener permisos de administrador.")
            return []

        # Procesa la salida de arp-scan
        devices = []
        for line in result.stdout.split("\n"):
            match = re.search(r'(\d+\.\d+\.\d+\.\d+)\s+([\da-fA-F:]+)\s+(.+)', line)
            if match:
                ip, mac, manufacturer = match.groups()
                devices.append({'IP': ip, 'MAC': mac, 'Fabricante': manufacturer.strip()})
        return devices

    except FileNotFoundError:
        print("arp-scan no está instalado. Instálalo con 'sudo apt-get install arp-scan'.")
        return []
    except Exception as e:
        print(f"Error al ejecutar arp-scan: {e}")
        return []


def run_nmap(ip_range):
    """Ejecuta nmap para buscar dispositivos en el rango."""
    try:
        # Ejecuta nmap con escaneo de ping
        result = subprocess.run(['nmap', '-sn', ip_range], capture_output=True, text=True)
        if result.returncode != 0:
            print("Error al ejecutar Nmap. Asegúrate de que esté instalado.")
            return []

        # Procesa la salida de nmap
        devices = []
        current_ip = None
        for line in result.stdout.split("\n"):
            # Busca líneas con la IP
            ip_match = re.search(r'Nmap scan report for (\d+\.\d+\.\d+\.\d+)', line)
            if ip_match:
                current_ip = ip_match.group(1)
            # Busca líneas con la MAC y fabricante
            mac_match = re.search(r'MAC Address: ([\da-fA-F:]+) \((.+)\)', line)
            if mac_match and current_ip:
                mac, manufacturer = mac_match.groups()
                devices.append({'IP': current_ip, 'MAC': mac, 'Fabricante': manufacturer.strip()})
        return devices

    except FileNotFoundError:
        print("Nmap no está instalado. Instálalo con 'sudo apt-get install nmap'.")
        return []
    except Exception as e:
        print(f"Error al ejecutar Nmap: {e}")
        return []


def merge_results(arp_devices, nmap_devices):
    """Fusiona los resultados de arp-scan y nmap, eliminando duplicados."""
    combined_devices = arp_devices.copy()

    for nmap_device in nmap_devices:
        if not any(nmap_device['IP'] == d['IP'] for d in combined_devices):
            combined_devices.append(nmap_device)

    return combined_devices


if __name__ == "__main__":
    # Define el rango de IPs a escanear (ajusta a tu red local)
    ip_range = "192.168.100.0/24"  # Cambia esto según tu configuración de red

    print("Ejecutando escaneo con arp-scan...")
    arp_devices = run_arp_scan(ip_range)

    print("Ejecutando escaneo con Nmap...")
    nmap_devices = run_nmap(ip_range)

    print("Fusionando resultados...")
    all_devices = merge_results(arp_devices, nmap_devices)

    # Muestra los dispositivos encontrados
    if all_devices:
        print("\nDispositivos conectados a tu red:")
        for device in all_devices:
            print(f"IP: {device['IP']}, MAC: {device['MAC']}, Fabricante: {device['Fabricante']}")
    else:
        print("No se encontraron dispositivos conectados.")

