# Estado inicial y objetivo
estado_inicial = {"ubicacion": "almacen", "paquetes": ["paquete1", "paquete2"]}
estado_objetivo = {"ubicacion": "entrega", "paquetes": []}

# Acciones disponibles
acciones = [
    {
        "nombre": "recoger",
        "precondiciones": {"ubicacion": "almacen", "paquetes": ["paquete1"]},
        "efectos": {"ubicacion": "almacen", "paquetes": []}
    },
    {
        "nombre": "cargar",
        "precondiciones": {"ubicacion": "almacen", "paquetes": ["paquete2"]},
        "efectos": {"ubicacion": "almacen", "paquetes": []}
    },
    {
        "nombre": "entregar",
        "precondiciones": {"ubicacion": "entrega", "paquetes": []},
        "efectos": {"ubicacion": "entrega", "paquetes": ["paquete1", "paquete2"]}
    }
]

def planificacion_condicional(estado_inicial, estado_objetivo, acciones):
    plan = []
    estado_actual = estado_inicial

    while estado_actual != estado_objetivo:
        accion_valida = None
        for accion in acciones:
            if all(estado_actual[k] == v for k, v in accion["precondiciones"].items()):
                accion_valida = accion
                break

        if accion_valida:
            plan.append(accion_valida["nombre"])
            estado_actual = {**estado_actual, **accion_valida["efectos"]}
        else:
            print("No se puede encontrar una solución.")
            return None

    return plan

plan = planificacion_condicional(estado_inicial, estado_objetivo, acciones)
if plan:
    print("Plan encontrado:", plan)
