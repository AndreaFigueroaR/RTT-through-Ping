import matplotlib.pyplot as plt
import pandas as pd
def generate_histograms(rtt_values, output_path, promedio):
    if not rtt_values:
        return
    data = pd.DataFrame({"RTT": rtt_values})
    successful_rtt = data["RTT"].dropna()
    rtt_filtrados = [x for x in successful_rtt if x < 3*promedio]  

    

    # lineal 20 subintervalos 
    plt.figure(figsize=(10, 6))
    plt.hist(
    rtt_filtrados,
    bins=20,
    edgecolor="black",
    alpha=0.7,
    color="blue"
    )
    plt.xlabel("RTT (ms)")
    plt.ylabel("Frecuencia")
    plt.title("Histograma de RTT (escala lineal)")
    plt.grid(True)
    filename = "histogram_linear_20_bins.png"
    plt.savefig(f"{output_path}/{filename}", dpi=300)
    plt.clf()

    # lineal 40 subintervalos 
    plt.figure(figsize=(10, 6))
    plt.hist(
    rtt_filtrados,
    bins=40,
    edgecolor="black",
    alpha=0.7,
    color="blue"
    )
    plt.xlabel("RTT (ms)")
    plt.ylabel("Frecuencia")
    plt.title("Histograma de RTT (escala lineal)")
    plt.grid(True)
    filename = "histogram_linear_40_bins.png"
    plt.savefig(f"{output_path}/{filename}", dpi=300)
    plt.clf()
    
    # log-log 20 subintervalos
    plt.figure(figsize=(10, 6))
    plt.hist(
    rtt_filtrados,
    bins=20,
    edgecolor="black",
    alpha=0.7,
    color="red"
    )
    plt.xlabel("RTT (ms)")
    plt.ylabel("Frecuencia")
    plt.title("Histograma de RTT (escala log-log)")
    plt.grid(True)
    plt.yscale("log")
    plt.xscale("log")
    filename = "histogram_log_log_20_bins.png"
    plt.savefig(f"{output_path}/{filename}", dpi=300)
    plt.clf()

    # log-log 40 subintervalos
    plt.figure(figsize=(10, 6))
    plt.hist(
    rtt_filtrados,
    bins=40,
    edgecolor="black",
    alpha=0.7,
    color="red"
    )
    plt.xlabel("RTT (ms)")
    plt.ylabel("Frecuencia")
    plt.title("Histograma de RTT (escala log-log)")
    plt.grid(True)
    plt.yscale("log")
    plt.xscale("log")
    filename = "histogram_log_log_40_bins.png"
    plt.savefig(f"{output_path}/{filename}", dpi=300)
    plt.clf()

    ##
    
