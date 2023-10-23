import random
import time

# Función para ejecutar una acción en el entorno simulado
def ejecutar_accion(accion):
    print(f"Ejecutando acción: {accion}")
    time.sleep(2)  # Simula la duración de la acción
    return random.choice([True, False])  # Simula si la acción fue exitosa o no

# Plan inicial
plan = ["A", "B", "C", "D"]

# Ciclo de vigilancia y replanificación
for accion in plan:
    exito = ejecutar_accion(accion)
    if not exito:
        print(f"Error en la ejecución de la acción: {accion}")
        print("Replanificando...")
        
        # Aquí iría la lógica de replanificación en tiempo real
        # Podrías modificar el plan actual o incluso generar uno completamente nuevo
        nuevo_plan = ["B", "C", "D"]  # Ejemplo de un nuevo plan
        
        print(f"Nuevo plan: {nuevo_plan}")
        print("Continuando con la ejecución del nuevo plan.\n")
        
        plan = nuevo_plan

print("Plan ejecutado exitosamente.")

