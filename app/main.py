# IMPORTS al inicio (antes de definir rutas)
from datetime import datetime
import logging

# Configurar logging (después de imports, antes de rutas)
logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 1. Definir rutas
input_file="app/tasks.txt"
output_file="output/report.txt"

# Log de inicio
logging.info('Inicio del proceso')

# 2. Leer archivo (CON TRY/EXCEPT)
try:
    with open(input_file, 'r') as file:
        data = file.read()
    logging.info(f'Archivo {input_file} leído correctamente')
except FileNotFoundError:
    logging.error(f'Error: No se encuentra {input_file}')
    print(f'Error: No se encuentra {input_file}')
    exit(1)
except Exception as e:
    logging.error(f'Error inesperado: {e}')
    print(f'Error inesperado: {e}')
    exit(1)

# 3. Procesar datos
pendientes = 0
terminadas = 0
canceladas = 0

lineas = data.split('\n')

for linea in lineas:
    if linea.startswith('Estado:'):
        estado = linea.split(': ')[1]
        
        if estado == 'Pendiente':
            pendientes += 1
        elif estado == 'Terminado':
            terminadas += 1
        elif estado == 'Cancelado':
            canceladas += 1

# Calcular total y porcentaje
total = pendientes + terminadas + canceladas
logging.info(f'Procesadas {total} tareas')

porcentaje_completado = 0
if total > 0:
    porcentaje_completado = (terminadas / total) * 100

# 4. Escribir resultados
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open(output_file, 'w') as salida:
    salida.write(f'Reporte generado: {timestamp}\n')
    salida.write('=== REPORTE DE TAREAS ===\n')
    salida.write(f'Pendientes: {pendientes}\n')
    salida.write(f'Terminadas: {terminadas}\n')
    salida.write(f'Canceladas: {canceladas}\n')
    salida.write(f'Total: {total}\n')
    salida.write(f'Progreso: {porcentaje_completado:.1f}%\n')

logging.info('Reporte generado exitosamente')

# 5. Mensaje de confirmación
print('✓ Reporte generado exitosamente en output/report.txt')
print(f'Total de tareas procesadas: {total}')