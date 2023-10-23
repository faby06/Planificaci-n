# Ejemplo de planificaci�n STRIPS
estado_inicial = {...}
estado_objetivo = {...}

def planificacion_strips(estado_inicial, estado_objetivo):
    acciones = []
    while estado_inicial != estado_objetivo:
        accion = seleccionar_accion(estado_inicial, estado_objetivo)
        estado_inicial = aplicar_accion(estado_inicial, accion)
        acciones.append(accion)
    return acciones

def seleccionar_accion(estado_actual, estado_objetivo):
    # L�gica para seleccionar la pr�xima acci�n
    accion = ...
    return accion

def aplicar_accion(estado, accion):
    # L�gica para aplicar una acci�n al estado actual
    nuevo_estado = ...
    return nuevo_estado

# Ejemplo de planificaci�n ADL
# Implementa la planificaci�n ADL de manera similar a STRIPS, pero con acciones m�s expresivas.

