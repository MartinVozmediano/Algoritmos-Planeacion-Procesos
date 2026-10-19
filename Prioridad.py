procesos = []

num_procesos = int(input("¿Cuántos procesos vas a ingresar?: "))
if num_procesos <= 0:
    raise ValueError("Debes ingresar al menos un proceso.")

for i in range(num_procesos):
    print(f"\n--- Datos del Proceso {i + 1} ---")
    trabajo = input("Nombre del Trabajo (ej. A, B, P1): ")
    rafaga = int(input("Ráfaga de CPU: "))
    llegada = int(input("Tiempo de Llegada: "))
    prioridad = int(input("Prioridad (menor número = mayor prioridad): "))

    if rafaga <= 0 or llegada < 0:
        raise ValueError("La ráfaga debe ser positiva y la llegada no puede ser negativa.")

    procesos.append({
        "trabajo": trabajo,
        "rafaga": rafaga,
        "llegada": llegada,
        "prioridad": prioridad,
        "orden": i,
    })

tiempo_actual = 0
total_espera = 0
total_retorno = 0
pendientes = procesos.copy()
linea_tiempo = []

while pendientes:
    disponibles = [p for p in pendientes if p["llegada"] <= tiempo_actual]

    if not disponibles:
        tiempo_actual = min(p["llegada"] for p in pendientes)
        disponibles = [p for p in pendientes if p["llegada"] <= tiempo_actual]

    proceso = min(
        disponibles,
        key=lambda p: (p["prioridad"], p["llegada"], p["orden"]),
    )
    pendientes.remove(proceso)

    inicio = tiempo_actual
    proceso["tiempo_espera"] = inicio - proceso["llegada"]
    tiempo_actual += proceso["rafaga"]
    proceso["tiempo_retorno"] = tiempo_actual
    total_espera += proceso["tiempo_espera"]
    total_retorno += proceso["tiempo_retorno"]
    linea_tiempo.append((proceso["trabajo"], inicio, tiempo_actual))

n = len(procesos)

print("\nDiagrama de ejecución:")
for trabajo, inicio, fin in linea_tiempo:
    print(f"{trabajo} ({inicio}-{fin})", end="  ")

print("\n\n" + "=" * 50)
print(f"{'Trabajo':<10} | {'Espera':<10} | {'Retorno':<10}")
print("=" * 50)
for proceso in procesos:
    print(
        f"{proceso['trabajo']:<10} | "
        f"{proceso['tiempo_espera']:<10} | "
        f"{proceso['tiempo_retorno']:<10}"
    )

print("-" * 50)
print(f"Tiempo Medio de Espera (TEM): {total_espera / n:.2f} ut")
print(f"Tiempo de Retorno Medio (TRM): {total_retorno / n:.2f} ut")
