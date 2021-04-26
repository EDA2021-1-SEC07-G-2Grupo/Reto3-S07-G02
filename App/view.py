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


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def print_separador():
    print("-----------------------------------------------(^(工)^)--------------------------------------------")
def print_separador_v2():
    print("***************************************************************************************************")
def print_separador_v3():
    print("_______________________________")
def printtitle(string):
    print("========================="+string+"=====================")
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
def printreq4(lista,titulos):
    titulos=titulos.split(",")
    n=1
    for char in titulos:
        printtitle(str(char))
        print("Para "+str(char)+" el tempo está entre "+str(controller.get_someting_map(catalog["genero"],char,"BPM_minimo"))+" y "+str(controller.get_someting_map(catalog["genero"],char,"BPM_maximo"))+" BPM.")
        print("Reproducciones de "+str(char)+": "+str(controller.conteo_range_value(lt.getElement(lista,n)))+" con un total de "+str(controller.conteo_llaves_unicas(lista))+" Artistas diferentes")
        printtitle("Algunos artistas del "+str(char))
        o=1
        elemento=lt.getElement(lista,n)

        n+=1




    

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
        espacio_tiempo=controller.loadData(catalog)
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
        total=controller.range_values(catalog[caracteristica],valor_min,valor_max)
        print_separador_v2()
        print(caracteristica+" entre "+str(valor_min)+" hasta "+str(valor_max))
        print ("El total de reproducción entre este rango es de "+str(controller.conteo_range_value(total)))
        print ("El total de artistas unicos dentro de este rango es de: "+str(controller.conteo_llaves_unicas(total)))


    elif int(inputs[0]) == 3:
        pass

    elif int(inputs[0]) == 4:
        
        valor_min_inst=float(input("Escriba el valor minimo de la carecteristica instrumentalness\n"))
        valor_max_inst=float(input("Escriba el valor maximo de la caracteristica instrumentalness\n"))
        vid_instrumentalness= controller.range_values(catalog["instrumentalness_id_trak"],valor_min_inst,valor_max_inst)
        valor_min_tem=float(input("Escriba el valor minimo de la carecteristica tempo\n"))
        valor_max_tem=float(input("Escriba el valor maximo de la caracteristica tempo\n"))
        vid_temp= controller.range_values(catalog["tempo_id_track"],valor_min_tem,valor_max_tem)
        vid_temp_rango=controller.list_only_id(vid_temp)
        vid_instrumentalness_rango=controller.list_only_id(vid_instrumentalness)
        print("Encontrando videos con las caracteristicas solicitadas...")
        one_list=controller.cmpare_two_list(vid_instrumentalness_rango,vid_temp_rango)
        print("Eligiendo videos al azar ")
        random_election_list=controller.random_select(one_list)
        print_separador_v2()
        if lt.size==0:
            print("No se ha encontrado ningún disco con ese rango de datos")
        else:
            print_req_3(random_election_list)
        print_separador_v2()
   
    
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
                generos_a_buscar=str(input("Escriba los generos que desea buscar separado por comas como se muestra en este ejemplo:Reggae, Hip-hop, Pop\n"))
                lista_by_genero=controller.lista_por_genero(generos_a_buscar,catalog)
                printreq4(lista_by_genero,generos_a_buscar)
                print("Buscando...")
                n=False
            else:
                n=False



    elif int(inputs[0]) == 6:
        hora_min= input ("Escriba el valor minimo de la hora del día")
        hora_max=input("Escriba el valor maximo de la hora del día ")
        

    else:
        sys.exit(0)
sys.exit(0)
