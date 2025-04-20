import re

def parse_ping_file(file_path):
    rtt_values = []
    packet_loss = 0.0
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            
            # Expresión regular para extraer RTTs (ej: time=25.6 ms)
            rtt_pattern = re.compile(r"time=(\d+\.?\d*) ms")
            
            # Expresión regular para pérdida de paquetes (ej: 0.555% packet loss)
            stats_pattern = re.compile(r"(\d+\.?\d+)% packet loss")

            for line in lines:
                # Extraer valores de RTT
                rtt_match = rtt_pattern.search(line)
                if rtt_match:
                    rtt_values.append(float(rtt_match.group(1)))
                
                # Extraer porcentaje de pérdida
                stats_match = stats_pattern.search(line)
                if stats_match:
                    packet_loss = float(stats_match.group(1))

    except FileNotFoundError:
        print(f"Error: Archivo {file_path} no encontrado")
        return None, None

    return rtt_values, packet_loss