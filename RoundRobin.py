from collections import deque

procesos = []

num_procesos = int(input("¿Cuántos procesos vas a ingresar?: "))
if num_procesos <= 0:
    raise ValueError("Debes ingresar al menos un proceso.")

for i in range(num_procesos):
    print(f"\n--- Datos del Proceso {i + 1} ---")
    trabajo = input("Nombre del Trabajo (ej. A, B, P1): ")
    rafaga = int(input("Ráfaga de CPU: "))
    llegada = int(input("Tiempo de Llegada: "))

    if rafaga <= 0 or llegada < 0:
        raise ValueError("La ráfaga debe ser positiva y la llegada no puede ser negativa.")

    procesos.append({
        "trabajo": trabajo,
        "rafaga": rafaga,
        "restante": rafaga,
        "llegada": llegada,
        "orden": i,
    })

quantum = int(input("\nQuantum (q): "))
if quantum <= 0:
    raise ValueError("El quantum debe ser positivo.")

procesos_por_llegada = sorted(
    procesos,
    key=lambda proceso: (proceso["llegada"], proceso["orden"]),
)
cola = deque()
linea_tiempo = []
tiempo_actual = 0
indice_siguiente = 0
total_espera = 0
total_retorno = 0

while indice_siguiente < len(procesos) or cola:
    if not cola:
        tiempo_actual = max(
            tiempo_actual,
            procesos_por_llegada[indice_siguiente]["llegada"],
        )

        while (
            indice_siguiente < len(procesos)
            and procesos_por_llegada[indice_siguiente]["llegada"] <= tiempo_actual
        ):
            cola.append(procesos_por_llegada[indice_siguiente])
            indice_siguiente += 1

    proceso = cola.popleft()
    inicio = tiempo_actual
    duracion = min(quantum, proceso["restante"])
    tiempo_actual += duracion
    proceso["restante"] -= duracion
    linea_tiempo.append((proceso["trabajo"], inicio, tiempo_actual))

    while (
        indice_siguiente < len(procesos)
        and procesos_por_llegada[indice_siguiente]["llegada"] <= tiempo_actual
    ):
        cola.append(procesos_por_llegada[indice_siguiente])
        indice_siguiente += 1

    if proceso["restante"] > 0:
        cola.append(proceso)
    else:
        proceso["tiempo_retorno"] = tiempo_actual
        proceso["tiempo_espera"] = (
            proceso["tiempo_retorno"] - proceso["llegada"] - proceso["rafaga"]
        )
        total_espera += proceso["tiempo_espera"]
        total_retorno += proceso["tiempo_retorno"]

n = len(procesos)

print(f"\nQuantum: {quantum} ut")
print("Diagrama de ejecución:")
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
