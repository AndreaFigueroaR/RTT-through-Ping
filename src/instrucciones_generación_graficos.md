# Instrucciones 
El presente código fuente contiene el codgio necesario para:
- Generar los datos en tiempo real: con el script generate_data.sh 
    Pudiendo omitir esta parte (tardada) y reusar los datos ya generados y dejados en el repositorio
- Instalar las dependencias necesarias para generar los gráficos: 
    Ejecutar desde la terminal (dentro del directorio principal del repositorio en el subdirectorio src):
    ```
    pip install -r requirements.txt
    ```
    si no se tienen los permisos necesarios ejecutar como sudo.
- Procesar a data generando los gráficos con el programa process_ping_output.py:
    Ejecutar desde la terminal (dentro del directorio principal del repositorio en el subdirectorio src):
    ```
    python3 proccess_ping_output.py
    ```
Finalmente podrá visualizar los gráficos generados en el directorio principal del repositorio.