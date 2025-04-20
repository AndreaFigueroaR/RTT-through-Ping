from parser import parse_ping_file
from general_stats import calculate_gen_stats
from general_stats import save_general_statics
from histograms import generate_histograms

if __name__ == "__main__":
    input_file = "../ping_output.txt"
    output_path = "../"
    rtt_data, packet_loss = parse_ping_file(input_file)
    
    
    if rtt_data is None:
        exit(-1)

    stats = calculate_gen_stats(rtt_data)
    save_general_statics(output_path, packet_loss, stats)
    generate_histograms(rtt_data, output_path, stats['mean'])
    print(" - Histogramas guardados en el path relativo:", output_path)


