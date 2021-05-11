"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as mp
assert cf
import random

import time
import tracemalloc


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory





























def print_separador():
    print("-----------------------------------------------(^(工)^)--------------------------------------------")
def print_separador_v2():
    print("***************************************************************************************************")
def print_separador_v3():
    print("_______________________________")
def printtitle(string):
    print("========================="+string+"===========================")
def printMenu():
    print("Bienvenido")
    print("1-  Cargar información en el catálogo")
    print("2-  Caracterizar las reproducciones")
    print("3-  Encontrar música para festejar")
    print("4-  Encontrar música para estudiar")
    print("5-  Estudiar los géneros musicales")
    print("6-  Indicar el género musical más escuchado en el tiempo")
catalog = None

def print_primeros_o_ultimos_n(first_last,n):
    if first_last=="first":
       i=1
       g=1
       while n>=i:
        print("Evento: "+str(i))
        mostrar=lt.getElement(catalog["content"],i)
        for char in mostrar:
             print(str(char)+": "+str(mostrar[char]))
        print_separador()
        i+=g
    elif first_last=="no":
       i=lt.size(catalog["content"])
       g=-1 
       n=lt.size(catalog["content"])-5
       while n<=i:
        print("Evento: "+str(i))
        mostrar=lt.getElement(catalog["content"],i)
        for char in mostrar:
             print(str(char)+": "+str(mostrar[char]))
        print_separador()
        i+=g

def print_req_2 (list):
    print("Se ha encontrado un total de "+str(lt.size(list)))
    i=1
    while i<=lt.size(list):
        char=lt.getElement(list,i)
          
        print("Track "+str(i)+": "+str(char)+" with energy of "+str(controller.get_someting_map(catalog["track"],char,"energy"))+" and danceability of "+str(controller.get_someting_map(catalog["track"],char,"danceability")))
        i+=1
   
def print_req_3 (list):
    i=1
    while i<=lt.size(list):
        char=lt.getElement(list,i)
        print("Track "+str(i)+": "+str(char)+" with intrumentalness of "+str(controller.get_someting_map(catalog["track"],char,"instrumentalness"))+" and tempo of "+str(controller.get_someting_map(catalog["track"],char,"tempo")))
        i+=1

def print_tabla_generos():
    print ("Genero| BMP_minimo|BMP_Maximo ")
    
    lista=mp.keySet(catalog["genero"])
    for char in lt.iterator(lista):
        coso=mp.get(catalog["genero"],char)
        elemento=lt.firstElement(coso["value"]["song"])
        print_separador_v3()
        print(str(elemento["Genero "]) +"| "+str(elemento["BPM_minimo"])+" | "+str(elemento["BPM_maximo"]))

   

    
def minimenu_req4():
    print("1- Crear un nuevo genero musical")
    print("2- Relizar busqueda")
    print("3- Salir")
def printreq4(titulos):
    titulos=titulos.split(",")
    
    for char in titulos:
        n=1
        i=1
        printtitle(str(char))
        print("Para "+str(char)+" el tempo está entre "+str(controller.get_someting_map(catalog["genero"],char,"BPM_minimo"))+" y "+str(controller.get_someting_map(catalog["genero"],char,"BPM_maximo"))+" BPM.")
        lista_total=controller.lista_por_genero(catalog,char)
        print("Reproducciones de "+str(char)+": "+str(controller.conteo_range_value(lista_total))+" con un total de "+str(controller.conteo_llaves_unicas(lista_total))+" Artistas diferentes")
        printtitle("Algunos artistas del genero "+str(char)+" son: ")
        while i<=10:
            h=random.randint(1,lt.size(lista_total))
            elemento=lt.getElement(lista_total,h)
            first=elemento["song"]["first"]
            
            print ("Artista "+str(i)+": "+str(first["info"]["artist_id"]))
            i+=1
        n+=1
               
               
def print_total_track_req5(list,hora_min,hora_max):
    print("Hay un total de "+str(controller.conteo_range_value(list))+" reproducciones entre las "+str(hora_min)+" y las "+str(hora_max))


def print_total_genero_musical_req5(lista,catalog):
    lista_imprimier=controller.cantidad_por_genero(lista,catalog)

  
    genero_top_1=lt.firstElement(lista_imprimier[0])
    print("El genero musical más referenciado es: "+str(genero_top_1["Genero Musica"])+" con "+str(genero_top_1["Reproducciones totales"])+" reproducciones.")
    print("Encontrando los mejores videos")
    n=1
    for char in lt.iterator(lista_imprimier[0]):
       
        print("Top "+str(n)+": "+char["Genero Musica"]+" con "+str(char["Reproducciones totales"])+" reproducciones.")
        n+=1
    printtitle("Analisis de sentimiento en el "+str(genero_top_1["Genero Musica"]))
    new_list=controller.Top_tracks_hashtag(lista_imprimier[1],catalog)
    v=1
    for element in lt.iterator(new_list):
        print ("Top "+str(v)+" track: "+str(element["track_id"])+" con "+str(element["num_hastags"])+" hashtags y VADER de "+str(element["Vader"]))
        v+=1


  


    
    
        

    

def initCatalog():
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga los videos en la estructura de datos
    """
    controller.loadData(catalog)
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
       
        print_separador_v2()
        print("Cargando información de los archivos ....")
        catalog = controller.initCatalog()
        controller.loadData(catalog)
        
        print_separador_v2()
        print ("El total de registros cargados es de: "+str(controller.lt_size(catalog["content"])))
        print("Total de artistas (sin repeticiones): " +str(controller.len_map(catalog['artist'])))
        print("Total de pistas cargadas: "+str(controller.len_map(catalog["track"])))
        print_separador_v2()
        print("los primeros 5 eventos:")
        print_primeros_o_ultimos_n("first",5)
        print_separador_v2()
        print("Los ultimos 5 eventos: ")
        print_primeros_o_ultimos_n("no",5)
        

    elif int(inputs[0]) == 2:
        caracteristica=str(input("Escriba la caracteristica que desea consultar\n"))
       
        valor_min=float(input("Escriba el valor minimo de la carecteristica que desea consultar\n"))
        valor_max=float(input("Escriba el valor maximo de la caracteristica que desea consultar\n"))
        
        start_time = time.process_time()
    
        delta_time = -1.0
        delta_memory = -1.0

    # inicializa el processo para medir memoria
        tracemalloc.start()

    # toma de tiempo y memoria al inicio del proceso
        start_time = getTime()
        start_memory = getMemory()





        total=controller.range_values(catalog[caracteristica],valor_min,valor_max)
        print_separador_v2()
        print(caracteristica+" entre "+str(valor_min)+" hasta "+str(valor_max))

        print ("El total de reproducción entre este rango es de "+str(controller.conteo_range_value(total)))
        print ("El total de artistas unicos dentro de este rango es de: "+str(controller.conteo_llaves_unicas(total)))
        
        
        
        stop_memory = getMemory()
        stop_time = getTime()

    # finaliza el procesos para medir memoria
        tracemalloc.stop()

    # calculando la diferencia de tiempo y memoria
        delta_time = stop_time - start_time
        delta_memory = deltaMemory(start_memory, stop_memory)
        print(delta_memory)





    elif int(inputs[0]) == 3:
        TODO:print("req2")
        #Inputs del usuario
        valor_min_ener=float(input("Escriba el valor MINIMO de la carecteristica energy: \n"))
        valor_max_ener=float(input("Escriba el valor MAXIMO de la caracteristica energy: \n"))
        
        valor_min_dance=float(input("Escriba el valor MINIMO de la carecteristica danceability: \n"))
        valor_max_tem=float(input("Escriba el valor MAXIMO de la caracteristica danceability: \n"))

        #Funcionamiento del req2
        start_time = time.process_time()
        vid_energy= controller.values(catalog["energy_id_trak"],valor_min_ener,valor_max_ener)
        vid_dance= controller.range_values(catalog["danceability_id_track"],valor_min_dance,valor_max_dance)
        vid_dance_rango=controller.list_only_id(vid_dance,"track_id")
        vid_energy_rango=controller.list_only_id(vid_energy,"track_id")
        print("Encontrando videos con las caracteristicas solicitadas... ")
        one_list=controller.cmpare_two_list(vid_energy_rango,vid_dance_rango)
        print("Eligiendo videos al azar... ")
        random_election_list=controller.random_select(one_list,5)
        print_separador_v2()
        if lt.size==0:
            print("No se ha encontrado ningún disco con ese rango de datos")
        else:
            print_req_2(random_election_list)
        print_separador_v2()
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print(elapsed_time_mseg)
        pass

    elif int(inputs[0]) == 4:
        
        valor_min_inst=float(input("Escriba el valor minimo de la carecteristica instrumentalness\n"))
        valor_max_inst=float(input("Escriba el valor maximo de la caracteristica instrumentalness\n"))
        valor_min_tem=float(input("Escriba el valor minimo de la carecteristica tempo\n"))
        valor_max_tem=float(input("Escriba el valor maximo de la caracteristica tempo\n"))
        
        start_time = time.process_time()
    
  
        delta_memory = -1.0
        tracemalloc.start()
        start_memory = getMemory()





        vid_instrumentalness= controller.range_values(catalog["instrumentalness_id_trak"],valor_min_inst,valor_max_inst)
        vid_temp= controller.range_values(catalog["tempo_id_track"],valor_min_tem,valor_max_tem)
        vid_temp_rango=controller.list_only_id_listnorm(vid_temp,"track_id")
        
        print("Encontrando videos con las caracteristicas solicitadas...")
        vid_instrumentalness_rango=controller.list_only_id_listnorm(vid_instrumentalness,"track_id")
       
        one_list=controller.normalcmpare_two_list(vid_instrumentalness_rango,vid_temp_rango)
        print("Eligiendo videos al azar ")
        random_election_list=controller.random_select(one_list,5)
        print("Se ha encontrado un total de "+str(lt.size(one_list))+ " tracks unicos. " )
        print_separador_v2()
        if lt.size(random_election_list)==0:
            print("No se ha encontrado ningún disco con ese rango de datos")
        else:
            print_req_3(random_election_list)
        
        
        print_separador_v2()
        stop_memory = getMemory()
        tracemalloc.stop()
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print(elapsed_time_mseg)
        delta_memory = deltaMemory(start_memory, stop_memory)
        print(delta_memory)
    
    
    
    
    elif int(inputs[0]) == 5:
        
        print_separador_v2()
        n=True
        minimenu_req4()
        print_separador_v2()
        a=(input("\nSeleccione una opción para continuar \n"))
        while n == True:
            if int(a[0])== 1:
                nombre_genero_musical=str(input("Escriba en nombre del genero que desea crear: \n"))
                bpm_min=int(input("Escriba el BPM minimo: \n"))
                bpm_max=int(input ("escriba el BPM maximo: \n"))
                controller.add_new_genero(catalog,nombre_genero_musical,bpm_min,bpm_max)
                print_separador_v2()
                print("Se ha creado el nuevo genero Musical")
                print_tabla_generos()
                n=False
            elif int(a[0])==2:
                print_tabla_generos()
                generos_a_buscar=str(input("Escriba los generos que desea buscar separado por comas como se muestra en este ejemplo:Reggae,Hip-hop,Pop\n"))
                print("Buscando...")
                
                start_time = time.process_time()
    
  
                delta_memory = -1.0
                tracemalloc.start()
                start_memory = getMemory()




                printreq4(generos_a_buscar)



                stop_memory = getMemory()
                tracemalloc.stop()
                stop_time = time.process_time()
                elapsed_time_mseg = (stop_time - start_time)*1000
                print(elapsed_time_mseg)
                delta_memory = deltaMemory(start_memory, stop_memory)
                print(delta_memory)
                
                n=False
            else:
                n=False



    elif int(inputs[0]) == 6:
        hora_min= input ("Escriba el valor minimo de la hora del día como se muestra en el siguiente ejemplo:07:00\n")
        hora_max=input("Escriba el valor maximo de la hora del día \n")
        start_time = time.process_time()
    
  
        delta_memory = -1.0
        tracemalloc.start()
        start_memory = getMemory()

        hora_min=controller.transform_hora(hora_min)
        hora_max=controller.transform_hora(hora_max)
        total=controller.range_values(catalog["created_at"],hora_min, hora_max)
        print_total_track_req5(total,hora_min,hora_max)
        print_total_genero_musical_req5(total,catalog)



        stop_memory = getMemory()
        tracemalloc.stop()
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print(elapsed_time_mseg)
        delta_memory = deltaMemory(start_memory, stop_memory)
        print(delta_memory)
        

    else:
        sys.exit(0)
sys.exit(0)


