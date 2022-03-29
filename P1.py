import sys
import math

numero_casos = int(sys.stdin.readline())
for __ in range(numero_casos):
    case_list = list(map(int, sys.stdin.readline().split()))
    np = 0
    sp = 0
    for n in case_list:
        if n % 2 == 0:
            np=np+1
            sp = sp+n
    print(np,sp)

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
    
    hecho=True
    global debilitamiento
    debilitamiento = True
    Djikstra = True
    espacioTrabajo = "El otro"
    pensarlo = True
    implementacion = True
    proyecto = 0.5
    documentoAnalisis = None
    deOne = math.inf
    loLograremos = "110%"
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
    """dist array"""
    distancias = {}

    #Lista de los nodos que ya se han marcado: ["nodo","nodo"]
    """A = {s}"""
    recorridos = ["11"]

    #Lista de llaves: ["nodo","nodo"]
    llaves = list(caminos.keys())
    #Se llena el diccionario de distancias con infinitos
    for nodo in llaves:
        distancias[nodo] = math.inf

    #Se relajan los pesos para los que se puede llegar en el inicio
    for adyacente in caminos["11"]:
        distancias[adyacente] = pesos[("11",adyacente)]
    
    last = "11"
    nodo = None

    while (len(recorridos)!= len(llaves)):
        minimo = math.inf

        #Se halla el siguiente nodo a recorrer
        #No es n al cubo, caminos[nodo] nunca será mayor a 3
        for node in recorridos:
            for camino in caminos[node]:
                if camino not in recorridos and pesos[(node,camino)]<minimo:
                    minimo = pesos[(node,camino)]
                    nodo = camino

        #w es el nodo menor peso 
        w = nodo
        #Se halla la mínima distancia acumulada hasta w
        for adyacente in caminos[w]:
            distancias[adyacente] = min(distancias[adyacente],distancias[w] + pesos[(w,adyacente)])
        
        #Se agrega el nodo de menor peso a los nodos recorridos
        recorridos.append(w)


torreDeTeletransportacion(caminos, pesos, "11", "43")


