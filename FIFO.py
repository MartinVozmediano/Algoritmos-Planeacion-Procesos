# 1. Definir la lista vacía de procesos
procesos = []

# Solicitar al usuario cuántos procesos desea registrar
num_procesos = int(input("¿Cuántos procesos vas a ingresar?: "))

# Recopilar los datos ingresados por el usuario
for i in range(num_procesos):
    print(f"\n--- Datos del Proceso {i+1} ---")
    trabajo = input("Nombre del Trabajo (ej. A, B, P1): ")
    rafaga = int(input("Ráfaga de CPU: "))
    llegada = int(input("Tiempo de Llegada: "))
    
    procesos.append({
        'trabajo': trabajo,
        'rafaga': rafaga,
        'llegada': llegada
    })

# 2. Ordenar los procesos según su Tiempo de Llegada de menor a mayor
procesos.sort(key=lambda x: x['llegada'])

tiempo_actual = 0
total_espera = 0
total_retorno = 0

# 3 y 4. Simular la línea de tiempo y calcular métricas
for p in procesos:
    # Si el procesador está inactivo esperando a que llegue el proceso
    if tiempo_actual < p['llegada']:
        tiempo_actual = p['llegada']
        
    p['tiempo_espera'] = tiempo_actual - p['llegada']
    
    tiempo_actual += p['rafaga']
    p['tiempo_retorno'] = tiempo_actual
    
    total_espera += p['tiempo_espera']
    total_retorno += p['tiempo_retorno']

# 5. Calcular los promedios
n = len(procesos)
tem = total_espera / n
trm = total_retorno / n

# Mostrar los resultados
print("\n" + "="*35)
print(f"{'Trabajo':<10} | {'Espera':<10} | {'Retorno':<10}")
print("="*35)
for p in procesos:
    print(f"{p['trabajo']:<10} | {p['tiempo_espera']:<10} | {p['tiempo_retorno']:<10}")

print("-" * 35)
print(f"Tiempo Medio de Espera (TEM): {tem:.2f} ut")
print(f"Tiempo de Retorno Medio (TRM): {trm:.2f} ut")