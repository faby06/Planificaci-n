# Ejemplo de planificación de orden parcial
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
    # Lógica para seleccionar la acción con la prioridad más alta
    accion = ...
    return accion

