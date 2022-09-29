from typing import List, Dict

#Lista de las rutas y precio de boleto (primera lista:
# incluye las rutas, precio base del boleto y el minimo,
# macimo de pasajes vendidos)
def main():
    ruta: List[Dict[str, str | float]] = [{
          {
            "code": "LIM-AYA",
            "name": "LIMA - AYACUCHO",
            "precio_base": 55.19,
            "min_sales":120,
            "max_sales":130
        },
            {
            "code": "LIM-CUS",
            "name": "LIMA - CUSCO",
            "precio_base": 136.51,
             "min_sales":130,
            "max_sales":144
        },
            {
            "code": "LIM-ARE",
            "name": "LIMA - AREQUIPA",
            "precio_base": 90.59,
             "min_sales":115,
            "max_sales":138
        },
            {
            "code": "LIM-TAR",
            "name": "LIMA - TARAPOTO",
            "precio_base": 71.80,
             "min_sales":100,
            "max_sales":120
        },
            {
            "code": "AYA-LIM",
            "name": "AYACUCHO - LIMA",
            "precio_base": 40.42,
             "min_sales":100,
            "max_sales":115
        },
            {
            "code": "CUS-LIM",
            "name": "CUSCO - LIMA",
            "precio_base": 124.32,
             "min_sales":105,
            "max_sales":120
        },
            {
            "code": "ARE-LIM",
            "name": "AREQUIPA - LIMA",
            "precio_base": 86.59,
             "min_sales":100,
            "max_sales":110
        },
             {
            "code": "TAR-LIM",
            "name": "TARAPOTO - LIMA",
            "precio_base": 68.42,
             "min_sales":90,
            "max_sales":105
        }
    }]
    #Precio de asientos economicos y premiun y el min y max de
    #pasajes eco y pre vendidos
    asientos: List[Dict[str | int, int]]=[{
        {
            "code": "LIM-AYA",
            "ast_eco": 8,
            "ast_pre": 16,
             "min_sales":10,
            "max_sales":20
        },
         {
            "code": "LIM-CUS",
            "ast_eco": 8,
            "ast_pre": 16,
             "min_sales":15,
            "max_sales":24
        },
         {
            "code": "LIM-ARE",
            "ast_eco": 8,
            "ast_pre": 16,
             "min_sales":22,
            "max_sales":16
        },
         {
            "code": "LIM-TAR",
            "ast_eco": 8,
            "ast_pre": 16,
             "min_sales":18,
            "max_sales":12
        },
         {
            "code": "AYA-LIM",
            "ast_eco": 7,
            "ast_pre": 16,
             "min_sales":10,
            "max_sales":15
        },
         {
            "code": "CUS-LIM",
            "ast_eco": 7,
            "ast_pre": 16,
             "min_sales":14,
            "max_sales":20
        },
         {
            "code": "ARE-LIM",
            "ast_eco": 7,
            "ast_pre": 16,
             "min_sales":13,
            "max_sales":18
        },
         {
            "code": "TAR-LIM",
            "ast_eco": 7,
            "ast_pre": 16,
             "min_sales":10,
            "max_sales":15
        }
    }]

    if __name__=="__main__":
        main()