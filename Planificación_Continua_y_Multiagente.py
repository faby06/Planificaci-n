import simpy
import random

# Función para simular el comportamiento de un camión
def camion_entrega(env, nombre, ubicacion_actual, destino, velocidad):
    print(f"{nombre} salió de {ubicacion_actual} hacia {destino} a las {env.now}")
    tiempo_viaje = (destino - ubicacion_actual) / velocidad
    yield env.timeout(tiempo_viaje)
    print(f"{nombre} llegó a {destino} a las {env.now}")

# Función para simular el sistema de planificación multiagente
def planificacion_multiagente(env):
    ubicaciones = {
        'Almacén': 0,
        'Cliente A': 4,
        'Cliente B': 7,
        'Cliente C': 10
    }
    
    camiones = ['Camión 1', 'Camión 2', 'Camión 3']
    
    while True:
        destino = random.choice(list(ubicaciones.keys()))
        ubicacion_actual = random.choice(list(ubicaciones.keys()))
        camion = random.choice(camiones)
        
        if destino != ubicacion_actual:
            velocidad_camion = random.uniform(1, 3)  # Velocidad aleatoria
            
            yield env.process(camion_entrega(env, camion, ubicaciones[ubicacion_actual], ubicaciones[destino], velocidad_camion))

# Configuración de la simulación
env = simpy.Environment()
env.process(planificacion_multiagente(env))

# Iniciar la simulación
env.run(until=20)

