n = int(input("Cantidad de procesos: "))
procesos = []

print("Ingresa los datos (Nombre Ráfaga Llegada) separados por espacio:")
for _ in range(n):
    t, r, l = input("Proceso: ").split()
    procesos.append({'trabajo': t, 'rafaga': int(r), 'llegada': int(l)})

tiempo_actual = espera_total = retorno_total = 0

print(f"\n{'Trabajo':<8} | {'Espera':<8} | {'Retorno':<8}")
print("-" * 30)

while procesos:
    # 1. Filtrar los procesos que ya han llegado en el tiempo actual
    disponibles = [p for p in procesos if p['llegada'] <= tiempo_actual]
    
    if not disponibles:
        # Si no hay procesos disponibles, el procesador queda inactivo hasta que llegue el próximo
        tiempo_actual = min(p['llegada'] for p in procesos)
        continue
        
    # 2. SJF: Seleccionar el proceso disponible con la ráfaga más corta
    # Si hay empate, se desempata por orden de llegada
    siguiente = min(disponibles, key=lambda x: (x['rafaga'], x['llegada']))
    
    # 3. Calcular métricas y actualizar la línea de tiempo
    procesos.remove(siguiente)
    espera = tiempo_actual - siguiente['llegada']
    tiempo_actual += siguiente['rafaga']
    retorno = tiempo_actual  # En este formato, el retorno coincide con el tiempo de finalización
    
    espera_total += espera
    retorno_total += retorno
    
    print(f"{siguiente['trabajo']:<8} | {espera:<8} | {retorno:<8}")

print("-" * 30)
print(f"TEM: {espera_total/n:.2f} ut  |  TRM: {retorno_total/n:.2f} ut")