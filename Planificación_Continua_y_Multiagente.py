import simpy
import random

# Funci�n para simular el comportamiento de un cami�n
def camion_entrega(env, nombre, ubicacion_actual, destino, velocidad):
    print(f"{nombre} sali� de {ubicacion_actual} hacia {destino} a las {env.now}")
    tiempo_viaje = (destino - ubicacion_actual) / velocidad
    yield env.timeout(tiempo_viaje)
    print(f"{nombre} lleg� a {destino} a las {env.now}")

# Funci�n para simular el sistema de planificaci�n multiagente
def planificacion_multiagente(env):
    ubicaciones = {
        'Almac�n': 0,
        'Cliente A': 4,
        'Cliente B': 7,
        'Cliente C': 10
    }
    
    camiones = ['Cami�n 1', 'Cami�n 2', 'Cami�n 3']
    
    while True:
        destino = random.choice(list(ubicaciones.keys()))
        ubicacion_actual = random.choice(list(ubicaciones.keys()))
        camion = random.choice(camiones)
        
        if destino != ubicacion_actual:
            velocidad_camion = random.uniform(1, 3)  # Velocidad aleatoria
            
            yield env.process(camion_entrega(env, camion, ubicaciones[ubicacion_actual], ubicaciones[destino], velocidad_camion))

# Configuraci�n de la simulaci�n
env = simpy.Environment()
env.process(planificacion_multiagente(env))

# Iniciar la simulaci�n
env.run(until=20)

