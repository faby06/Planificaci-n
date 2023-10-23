# Ejemplo de planificaci�n de orden parcial
acciones = [...]
prioridades = [1, 2, 3, ...]  # Prioridades de las acciones

def planificacion_orden_parcial(acciones, prioridades):
    plan = []
    while acciones:
        accion_seleccionada = seleccionar_accion_prioritaria(acciones, prioridades)
        plan.append(accion_seleccionada)
        acciones.remove(accion_seleccionada)
    return plan

def seleccionar_accion_prioritaria(acciones, prioridades):
    # L�gica para seleccionar la acci�n con la prioridad m�s alta
    accion = ...
    return accion

