#!/bin/bash

# Script: generate_data.sh
# Descripción: Ejecuta un ping prolongado a Google y guarda los resultados.
# Duración estimada: 2.5 horas (900 paquetes × 10 segundos)
# Requisitos:
#   - Conexión estable a internet
#   - No interrumpir el proceso (se cancelará la captura)
#   - 1 MB libre de espacio en disco (aproximado)

# Ruta del archivo de salida (directorio padre del actual)
ARCHIVO_SALIDA="../ping_output.txt"

echo " Iniciando captura de datos (900 paquetes)..."
echo " Este proceso tomará aproximadamente 2.5 horas"
echo " Puedes detenerlo con Ctrl+C, pero se perderán los datos"

# Ejecutar ping con:
#  -i 10 : intervalo de 10 segundos entre paquetes
#  -c 900: 900 paquetes en total
ping google.com -i 10 -c 900 > "$ARCHIVO_SALIDA"

# Verificar si se completó correctamente
if [ $? -eq 0 ]; then
    echo "Captura completada! Archivo guardado en: $ARCHIVO_SALIDA"
else
    echo "Error durante la ejecución! Verifica tu conexión"
fi