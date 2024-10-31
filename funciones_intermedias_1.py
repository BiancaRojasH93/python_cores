

### 1 ACTUALIZAR VALORES EN DICCIONARIOS Y LISTAS ###

# CAMBIA EL VALOR DE 3 POR UN 6 EN LA MATRIZ

matriz = [ [10, 15, 20], [3, 7, 14] ]

matriz[1][0] = 6

print(matriz)

# CAMBIA EL NOMBRE DEL PRIMER CANTANTE DE "RICKY MARTIN" A "ENRIQUE MARTIN MORALES"

cantantes = [

    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

    {"nombre": "Chayanne", "pais": "Puerto Rico"}

]

cantantes[0]["nombre"] = "Enrique Martin Morales"

print(cantantes)

# EN CIUDADES, CAMBIA "CANCÚN" POR "MONTERREY"

ciudades = {

    "México": ["Ciudad de México", "Guadalajara", "Cancún"],

    "Chile": ["Santiago", "Concepción", "Viña del Mar"]

}

ciudades["México"][2] = "Monterrey"

print(ciudades)

# EN LAS COORDENADAS, CAMBIA EL VALOR DE "LATITUD" POR 9.9355431

coordenadas = [

    {"latitud": 8.2588997, "longitud": -84.9399704}

]

coordenadas[0]["latitud"] = 9.9355431

print(coordenadas)


### ITERAR A TRAVÉS DE UNA LISTA DE DICCIONARIOS ###

cantantes = [

    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

    {"nombre": "Chayanne", "pais": "Puerto Rico"},

    {"nombre": "José José", "pais": "México"},

    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}

]

def iterarDiccionario(cantantes):
    for cantante in cantantes:
        print(f"Nombre - {cantante['nombre']}, País - {cantante['pais']}")


iterarDiccionario(cantantes)

### OBTENER VALORES DE UNA LISTA DE DICCIONARIOS ###

def iterarDiccionario2(nombre, cantantes):
    for cantante in cantantes:
        print(cantante[nombre])

iterarDiccionario2("nombre", cantantes)

def iterarDiccionario3(pais, cantantes):
    for cantante in cantantes:
        print(cantante[pais])

iterarDiccionario3("pais", cantantes)


### ITERAR A TRAVES DE UN DICCIONARIO CON VALORES DE LISTA ###

costa_rica = {

    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],

    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]

}

def imprimirInformacion(costa_rica):
    for keys in costa_rica:
        print(len(costa_rica[keys]), keys)
        for items in costa_rica[keys]:
            print(items)
        

imprimirInformacion(costa_rica)
