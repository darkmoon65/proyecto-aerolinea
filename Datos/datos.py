from typing import List, Dict
import random
from config import IGV_PERCENT

#Lista de las rutas y precio de boleto 
#Boletos vendidos min y max, 
#precio de asientos economicos o premiun
def main():
    
    routes: List[Dict[str, str | float | int]] = [
          {
            "code": "LIM-AYA",
            "name": "LIMA - AYACUCHO",
            "precio_base": 55.19,
            "min_passages_eco":120,
            "max_passages_eco":130,
            "price_seating_eco": 8,
            "price_seating_pre": 16,
            "min_pass_pre":10,
            "max_pass_pre":20
        },
            {
            "code": "LIM-CUS",
            "name": "LIMA - CUSCO",
            "precio_base": 136.51,
            "min_passages_eco":130,
            "max_passages_eco":144,
            "price_seating_eco": 8,
            "price_seating_pre": 16,
            "min_pass_pre":15,
            "max_pass_pre":24
        },
            {
            "code": "LIM-ARE",
            "name": "LIMA - AREQUIPA",
            "precio_base": 90.59,
            "min_passages_eco":115,
            "max_passages_eco":138,
            "price_seating_eco": 8,
            "price_seating_pre": 16,
            "min_pass_pre":16,
            "max_pass_pre":22
        },
            {
            "code": "LIM-TAR",
            "name": "LIMA - TARAPOTO",
            "precio_base": 71.80,
            "min_passages_eco":100,
            "max_passages_eco":120,
            "price_seating_eco": 8,
            "price_seating_pre": 16,
            "min_pass_pre":12,
            "max_pass_pre":18
        },
            {
            "code": "AYA-LIM",
            "name": "AYACUCHO - LIMA",
            "precio_base": 40.42,
            "min_passages_eco":100,
            "max_passages_eco":115,
            "price_seating_eco": 7,
            "price_seating_pre": 16,
            "min_pass_pre":10,
            "max_pass_pre":15
        },
            {
            "code": "CUS-LIM",
            "name": "CUSCO - LIMA",
            "precio_base": 124.32,
            "min_passages_eco":105,
            "max_passages_eco":120,
            "price_seating_eco": 7,
            "price_seating_pre": 16,
            "min_pass_pre":14,
            "max_pass_pre":20
        },
            {
            "code": "ARE-LIM",
            "name": "AREQUIPA - LIMA",
            "precio_base": 86.59,
            "min_passages_eco":100,
            "max_passages_eco":110,
            "price_seating_eco": 7,
            "price_seating_pre": 16,
            "min_pass_pre":13,
            "max_pass_pre":18
        },
             {
            "code": "TAR-LIM",
            "name": "TARAPOTO - LIMA",
            "precio_base": 68.42,
            "min_passages_eco":90,
            "max_passages_eco":105,
            "price_seating_eco": 7,
            "price_seating_pre": 16,
            "min_pass_pre":10,
            "max_pass_pre":15
        }
    ]

    sales_passages : int = 0
    sales_income_eco: float = 0.0
    sales_income_pre: float = 0.0

    for key, routes in enumerate(routes):
        #Calculamos el total de pasajes vendidos y los vamos sumando
        #Calculamos el total de pasajes vendidos Economicos
        passages_sales_eco: int = random.randint(int(routes["min_passages_eco"]), int(routes["max_passages_eco"]))
        passages_sales_pre: int = random.randint(int(routes["min_pass_pre"]), int(routes["max_pass_pre"]))
        passages_sales_total: int = passages_sales_eco + passages_sales_pre
        sales_passages+= passages_sales_total

        #Calculamos Precio de venta del asiento economico
        passage_price_eco: float = routes["precio_base"] + routes["price_seating_eco"]
        #Caclulamos el total de ingresos por ruta y lo sumamos a las ventas generales economicas.
        total_income_route_eco: float = passages_sales_eco * passage_price_eco
        sales_income_eco += total_income_route_eco

        #Calculamos Precio de venta del asiento premium
        passage_price_pre: float = routes["precio_base"] + routes["price_seating_pre"]
        #Caclulamos el total de ingresos por ruta y lo sumamos a las ventas generales premium.
        total_income_route_pre: float = passages_sales_pre * passage_price_pre
        sales_income_pre += total_income_route_pre

    #¿Cuál es el total de pasajes vendidos entre todos los vuelos?
    print("Se vendieron un total de :" + str(sales_passages) + " de pasajes")

    #¿Cuál es el total de ingresos por la venta de pasajes económicos?
    print("Se recaudó un total de :" + str(sales_income_eco)+ " en economico")

    #¿Cuál es el total de ingresos por la venta de pasajes premium?
    sales_income_pre = round(sales_income_pre, 2)
    print("Se recaudó un total de :" + str(sales_income_pre)+ " en premium")

    #¿Cuál es el importe total de IGV cobrado?
    total_import_IGV:float = round(((sales_income_eco + sales_income_pre) * IGV_PERCENT / 100) , 2)
    print("Se pago un total de : "+ str(total_import_IGV) +" en IGV")

    #¿Cuál es el valor promedio de un pasaje económico?
    

    #¿Cuál es el valor promedio de un pasaje premium?

    #¿Cuál fue el vuelo con la mayor cantidad de pasajeros?

    #¿Cuál fue el vuelo con la menor cantidad de pasajeros?

    #¿Cuáles son los tres primeros vuelos que obtuvieron los mayores ingresos por la
    #venta de asientos?

    #¿Cuál fue el avión que transportó la mayor cantidad de pasajeros?

if __name__=="__main__":
    main()