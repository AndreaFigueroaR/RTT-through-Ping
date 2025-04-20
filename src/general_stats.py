import numpy as np

def calculate_gen_stats(rtt_values):
    if not rtt_values:
        return None
    
    stats = {
        'min': np.min(rtt_values),
        'max': np.max(rtt_values),
        'mean': np.mean(rtt_values),
        'std': np.std(rtt_values)
    }
    return stats

def save_general_statics(output_path, packet_loss, stats):
    try:
        with open(f"{output_path}/general_statics.txt", "w") as f:
            f.write("Estadisticas de la conexion:\n")
            f.write(f"- Paquetes perdidos: {packet_loss:.3f}%\n")
            f.write(f"- RTT minimo: {stats['min']:.2f} ms\n")
            f.write(f"- RTT maximo: {stats['max']:.2f} ms\n")
            f.write(f"- RTT promedio: {stats['mean']:.2f} ms\n")
            f.write(f"- Desviacion estandar: {stats['std']:.2f} ms\n")
        print("\n - Estadísticas guardadas en general_statics.txt")
    except Exception as e:
        print(f"\n Error escribiendo archivo: {str(e)}")
