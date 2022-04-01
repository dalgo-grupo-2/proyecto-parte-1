# Juan Diego Yepes - 202022391
# Juan Diego Calixto - 202020774
# Sergio Pardo Gutiérrez - 202025720

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
    recorridos= {}
    #Lista de los nodos que ya se han marcado: ["nodo","nodo"]
    posiblesCaminos = []
    #Lista de llaves: ["nodo","nodo"]
    llaves = list(caminos.keys())
    #Se llena el diccionario de distancias con infinitos
    for nodo in llaves:
        distancias[nodo] = math.inf
        recorridos[nodo] = False

    #Se relajan los pesos para los que se puede llegar en el inicio
    for adyacente in caminos["11"]:
        distancias[adyacente] = pesos[("11",adyacente)]
        posiblesCaminos.append(("11",adyacente))
    w = "11"
    recorridos[w]=True
    continuar = True
    anterior = None
    while (w!=llaves[-1] and continuar == True):
        minimo = math.inf
        for camino in posiblesCaminos:    
            if pesos[camino]<minimo:
                minimo = pesos[camino]
                w = camino[1]
                anterior = camino[0]
        recorridos[w]=True
        posiblesCaminos.pop(posiblesCaminos.index((anterior,w)))
            
        if minimo == math.inf:
            continuar = False

        #Se halla la mínima distancia acumulada hasta w
        for adyacente in caminos[w]:
            distancias[adyacente] = min(distancias[adyacente],distancias[w] + pesos[(w,adyacente)])
            if recorridos[adyacente] == False:
                posiblesCaminos.append((w,adyacente))
        if len(posiblesCaminos)==0:
            continuar = False
        #Se agrega el nodo de menor peso a los nodos recorridos
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