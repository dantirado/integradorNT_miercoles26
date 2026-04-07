#función para generar N pagos de Gilgal Tours
#En springboot el modelo de un cliente es:
#id_pago(Integer)
#id_reserva(Integer)
#fecha_pago(LocalDate)
#monto(Float)
#metodo_pago(String)
#estado_pago(String)


import random
from datetime import datetime, timedelta
def simular_pagos_gilgal(numeroPagos):

    #defino atributos base, todos los string
    metodo_pago=["Efectivo", "PSE", "Transferencia"]
    estado_pago=["Pendiente", "Aprobado", "Cancelado"]
    

    #Para simular un rango de fechas, debo introducir una fecha inicial
    fechaInicial=datetime(2026,1,1)
    fechaBase=fechaInicial+timedelta(days=random.randint(0,20))
    
    #Ciclo para generar N registros de la tabla clientes
    pagos=[]
    for _ in range(numeroPagos):
        pago={
            "id_pago":random.randint(1,1000),
            "id_reserva":random.randint(1,1000),
            "fecha_pago":fechaBase.strftime("%Y-%m-%d"),
            "monto":random.uniform(150000, 900000),
            "metodo_pago":random.choice(metodo_pago),
            "estado_pago":random.choice(estado_pago),
        }
        pagos.append(pago)
    return pagos
