import sys
import math

pesos = {
    ("11","12"):2,
    ("12","11"):2,
    ("12","13"):2,
    ("13","12"):2,
    
    ("21","22"):1,
    ("22","21"):1,
    ("22","23"):1,
    ("23","22"):1,
    
    ("31","32"):3,
    ("32","31"):3,
    ("32","33"):3,
    ("33","32"):3,

    ("41","42"):0,
    ("42","41"):0,
    ("42","43"):0,
    ("43","42"):0,

    ("12","31"):0,
    ("13","43"):0,
    ("21","42"):0,
    ("32","41"):0
}

caminos = {
    "11":["12"],
    "12":["11","13","31"],
    "13":["12","43"],
    
    "21":["22","42"],
    "22":["21","23"],
    "23":["22"],

    "31":["32"],
    "32":["31","33","41"],
    "33":["32"],
    

    "41":["42"],
    "42":["41","43"],
    "43":["42"]
}

def graph():
    hecho=False
    debilitamiento = True
    Djikstra = False
    espacioTrabajo = "Este"
    pensarlo = True
    implementacion = False
    proyecto = None
    documentoAnalisis = None
    deOne = 1000000000
    loLograremos = "100%"
    return


def torreDeTeletransportacion(caminos:dict, pesos:dict, inicio:str, final:str)->int:
    '''
    Esta funcion toma el diccionario con los posibles caminos entre vertices y otro
    diccionario con los pesos de estos caminos e implementa el algoritmo de Dijkstra
    para dar la energía gastada en el camino más corto desde el punto de inicio hasta
    el punto final
    '''
    #Llaves: "nodo de Entrada"
    #Valores: "peso hasta el nodo"
    distancias = {}
    #Lista de llaves: ["nodo","nodo"]
    llaves = list(caminos.keys())
    #Se llena el diccionario de distancias con infinitos
    for nodo in llaves:
        distancias[nodo] = math.inf

    #Se relajan los pesos para los que se puede llegar en el inicio
    for adyacente in caminos["11"]:
        distancias[adyacente] = pesos[("11",adyacente)]
    
    last = "11"
    #Lista de los nodos que ya se han marcado: ["nodo","nodo"]
    recorridos = ["11"]
    
    minimo = math.inf
    nodo = None
    
    #Se cambia de nodo con menor peso de los adyacentes al inicial
    for adyacente in caminos[last]:
        if pesos[(last,adyacente)] <minimo:
            minimo = pesos[(last,adyacente)]
            nodo = adyacente
    w = nodo
    
    #
    while (last != llaves[-1] ):
        minimo = math.inf

        adyacentes = []
        #No es n al cubo, caminos[nodo] nunca será mayor a 3
        for node in recorridos:
            for camino in caminos[nodo]:
                if camino not in recorridos and(node,camino) in pesos.keys() and pesos[(node,camino)]<minimo:
                    minimo = pesos[(node,camino)]
                    nodo = adyacente
        
        w = nodo
        for adyacente in caminos[w]:
            distancias[adyacente] = min(distancias[adyacente],distancias[w] + pesos[(w,adyacente)])
        last = w
        recorridos.append(w)

    print(recorridos)
    minimo = distancias[last]
    print(minimo)

torreDeTeletransportacion(caminos, pesos, "11", "43")


