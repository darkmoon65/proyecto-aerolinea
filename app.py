from typing import List, Dict
import random
from config import IGV_PERCENT

#Lista de las rutas y precio de boleto 
#Boletos vendidos min y max, 
#precio de asientos economicos o premiun
def main():
    
    routes: List[Dict[str, str | int | float]] = [
          {
            "code_r": "LIM-AYA",
            "name": "LIMA - AYACUCHO",
            "precio_base": 55.19,
            "min_passages_eco":120,
            "max_passages_eco":130,
            "price_seating_eco": 8,
            "price_seating_pre": 16,
            "min_pass_pre":10,
            "max_pass_pre":20,
            "code_a": "A001"
        },
            {
            "code_r": "LIM-CUS",
            "name": "LIMA - CUSCO",
            "precio_base": 136.51,
            "min_passages_eco":130,
            "max_passages_eco":144,
            "price_seating_eco": 8,
            "price_seating_pre": 16,
            "min_pass_pre":15,
            "max_pass_pre":24,
            "code_a": "A002"
        },
            {
            "code_r": "LIM-ARE",
            "name": "LIMA - AREQUIPA",
            "precio_base": 90.59,
            "min_passages_eco":115,
            "max_passages_eco":138,
            "price_seating_eco": 8,
            "price_seating_pre": 16,
            "min_pass_pre":16,
            "max_pass_pre":22,
            "code_a": "A003"
        },
            {
            "code_r": "LIM-TAR",
            "name": "LIMA - TARAPOTO",
            "precio_base": 71.80,
            "min_passages_eco":100,
            "max_passages_eco":120,
            "price_seating_eco": 8,
            "price_seating_pre": 16,
            "min_pass_pre":12,
            "max_pass_pre":18,
            "code_a": "A004"
        },
            {
            "code_r": "AYA-LIM",
            "name": "AYACUCHO - LIMA",
            "precio_base": 40.42,
            "min_passages_eco":100,
            "max_passages_eco":115,
            "price_seating_eco": 7,
            "price_seating_pre": 16,
            "min_pass_pre":10,
            "max_pass_pre":15,
            "code_a": "A001"
        },
            {
            "code_r": "CUS-LIM",
            "name": "CUSCO - LIMA",
            "precio_base": 124.32,
            "min_passages_eco":105,
            "max_passages_eco":120,
            "price_seating_eco": 7,
            "price_seating_pre": 16,
            "min_pass_pre":14,
            "max_pass_pre":20,
            "code_a": "A002"
        },
            {
            "code_r": "ARE-LIM",
            "name": "AREQUIPA - LIMA",
            "precio_base": 86.59,
            "min_passages_eco":100,
            "max_passages_eco":110,
            "price_seating_eco": 7,
            "price_seating_pre": 16,
            "min_pass_pre":13,
            "max_pass_pre":18,
            "code_a": "A003"
        },
             {
            "code_r": "TAR-LIM",
            "name": "TARAPOTO - LIMA",
            "precio_base": 68.42,
            "min_passages_eco":90,
            "max_passages_eco":105,
            "price_seating_eco": 7,
            "price_seating_pre": 16,
            "min_pass_pre":10,
            "max_pass_pre":15,
            "code_a": "A004"
        }
    ]

    sales_passages:int = 0
    sales_income_eco: float = 0.0
    sales_income_pre: float = 0.0
    
    promedio_passage_eco: float = 0.0
    cantidad_vuelos: int = 0
    promedio_passage_pre: float = 0.0
    sales_table_fly: List[Dict[str, str]] = []
    sales_table_airplane: List[Dict[str, str]] = []
    sales_table_route: List[Dict[str, str]] = []

    for key, route in enumerate(routes):
        #Calculamos el total de pasajes vendidos y los vamos sumando
        #Calculamos el total de pasajes vendidos Economicos
        passages_sales_eco: int = random.randint(int(route["min_passages_eco"]), int(route["max_passages_eco"]))
        passages_sales_pre: int = random.randint(int(route["min_pass_pre"]), int(route["max_pass_pre"]))
        passages_sales_total: int = passages_sales_eco + passages_sales_pre
        sales_passages+= passages_sales_total

        #Calculamos Precio de venta del asiento economico
        passage_price_eco: float = float(route["precio_base"]) + float(route["price_seating_eco"])
        #Caclulamos el total de ingresos por ruta y lo sumamos a las ventas generales economicas.
        total_income_route_eco: float = float(passages_sales_eco) * passage_price_eco
        sales_income_eco += total_income_route_eco

        #Calculamos Precio de venta del asiento premium
        passage_price_pre: float = float(route["precio_base"]) + float(route["price_seating_pre"])
        #Caclulamos el total de ingresos por ruta y lo sumamos a las ventas generales premium.
        total_income_route_pre:float = float(passages_sales_pre) * passage_price_pre
        sales_income_pre += total_income_route_pre

        #Calculamos promedio de pasajes económicos
        promedio_passage_eco +=  passage_price_eco
        cantidad_vuelos +=1

        #Calculamos promedio de pasajes Premium
        promedio_passage_pre +=  passage_price_pre

        passage_price_total:int = round((int(total_income_route_eco) + int(total_income_route_pre)) , 2)
        sales_table_fly.append({
            "fly" : str(route["code_r"]),
            "sale": str(passage_price_total),
        })

        sales_table_route.append({
            "route" : str(route["code_r"]),
            "people": str(passages_sales_total)
        })   

        airplane_exits:bool = False
        airplane_pos:int = 0
        for i in range(0, len(sales_table_airplane)):
            if(route["code_a"] in sales_table_airplane[i].values()):
                airplane_exits = True
                airplane_pos = i

        if(airplane_exits):
            sales_table_airplane[airplane_pos]["people"] = str(int(sales_table_airplane[airplane_pos]["people"]) + passages_sales_total)
        else:
            sales_table_airplane.append({
                "airplane" : str(route["code_a"]),
                "people": str(passages_sales_total)
            })   
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
    print("Promedio de pasajes económicos: ", promedio_passage_eco/(cantidad_vuelos))

    #¿Cuál es el valor promedio de un pasaje premium?
    print("Promedio de pasajes Premium: ", promedio_passage_pre/(cantidad_vuelos))

    #¿Cuál fue el vuelo con la mayor cantidad de pasajeros?
    sales_table_route.sort(key=lambda x: x["people"], reverse=True)
    print("La ruta que llevó mas personas es: "+ str(sales_table_route[0]["route"])+" con "+ str(sales_table_route[0]["people"])+" personas")
   
    #¿Cuál fue el vuelo con la menor cantidad de pasajeros?
    print("La ruta que llevó menos personas es: "+ str(sales_table_route[len(sales_table_route)-1]["route"])+" con "+ str(sales_table_route[len(sales_table_route)-1]["people"])+" personas")
    
    #¿Cuáles son los tres primeros vuelos que obtuvieron los mayores ingresos por la
    #venta de asientos?
    #Ordenamos los elementos de la lista
    sales_table_fly.sort(key=lambda x: x["sale"], reverse=True)
    for i in range(0, 3):
        print("El Vuelo "+str(sales_table_fly[i]["fly"])+" tuvo: " + str(sales_table_fly[i]["sale"])+" ingresos")

    #¿Cuál fue el avión que transportó la mayor cantidad de pasajeros?
    sales_table_airplane.sort(key=lambda x: x["people"], reverse=True)
    print("El avion que transporto mas personas es: "+ str(sales_table_airplane[0]["airplane"])+" con "+ str(sales_table_airplane[0]["people"])+" personas")

if __name__=="__main__":
    main()