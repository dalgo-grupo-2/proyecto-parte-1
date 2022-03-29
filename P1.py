import sys
import math

def torreDeTeletransportacion(caminos:dict, pesos:dict)->int:
    '''
    Esta funcion toma el diccionario con los posibles caminos entre vertices y otro
    diccionario con los pesos de estos caminos e implementa el algoritmo de Dijkstra
    para dar la energía gastada en el camino más corto desde el punto de inicio hasta
    el punto final
    '''
    #Llaves: "nodo de Entrada"
    #Valores: "peso hasta el nodo"
    distancias = {}

    #Lista de los nodos que ya se han marcado: ["nodo","nodo"]
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
    masCorto = distancias[llaves[-1]]
    if masCorto == math.inf:
        masCorto = "NO EXISTE"
    return masCorto

numero_casos = int(sys.stdin.readline())
for __ in range(numero_casos):
    pesos = {}
    caminos = {}

    linea1 = sys.stdin.readline().split()
    pisos = int(linea1[0])
    cuartos = int(linea1[1])
    portales = int(linea1[2])
    energias =  sys.stdin.readline().split()

    for piso in range(1,pisos+1):
        for cuarto in range(1,cuartos):
            primerCuarto = str(piso)+str(cuarto)
            cuartoAdy = str(piso)+str(cuarto+1)
            pesos[(primerCuarto,cuartoAdy)] = int(energias[piso-1])
            pesos[(cuartoAdy,primerCuarto)] = int(energias[piso-1])
            listaCaminosPrimero = []
            listaCaminosPrimero.append(cuartoAdy)
            listaCaminosAdy = []
            listaCaminosAdy.append(primerCuarto)
            if primerCuarto not in caminos:
                caminos[primerCuarto] = listaCaminosPrimero
            else:
                caminos[primerCuarto].extend(listaCaminosPrimero)
            caminos[cuartoAdy] = listaCaminosAdy
            
    for p in range(portales):
        portales = sys.stdin.readline().split()
        inicioPortal = str(portales[0])+str(portales[1])
        finPortal = str(portales[2])+str(portales[3])
        pesos[(inicioPortal,finPortal)] = 0
        caminos[inicioPortal].append(finPortal)
    print(torreDeTeletransportacion(caminos,pesos))

