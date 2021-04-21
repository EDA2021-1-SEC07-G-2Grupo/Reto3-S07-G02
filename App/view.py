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
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def print_separador():
    print("-----------------------------------------------(°(工)°)--------------------------------------------")
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
    elif first_last=="no":
       i=lt.size(catalog["content"])
       g=-1 
       n=lt.size(catalog["content"])-5
    print_separador()
    while n<=i:
        print("Evento: "+str(i))
        mostrar=lt.getElement(catalog["content"],i)
        for char in mostrar:
             print(str(char)+": "+str(mostrar[char]))
        print_separador()
        i+=g


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
        
        print_separador()    
        print("Cargando información de los archivos ....")
        catalog = controller.initCatalog()
        espacio_tiempo=controller.loadData(catalog)
        print_separador()
        print ("El total de registros cargados es de: "+str(lt.size(catalog["content"])))
        print("Total de artistas (sin repeticiones): " +str(om.size(catalog['artist'])))
        print("Total de pistas cargadas: "+str(om.size(catalog["track"])))
        print_separador()
        print("los primeros 5 eventos:")
        print_primeros_o_ultimos_n("first",5)
        print("Los ultimos 5 eventos: ")
        print_primeros_o_ultimos_n("no",5)


    elif int(inputs[0]) == 2:
        caracteristica=str(input("Escriba la caracteristica que desea consultar\n"))
        valor_min=(input("Escriba el valor minimo de la carecteristica que desea consultar\n"))
        valor_max=(input("Escriba el valor maximo de la caracteristica que desea consultar\n"))
        total=om.values(catalog[caracteristica],valor_min,valor_max)
        print_separador()
        print(caracteristica+" entre "+str(valor_min)+" hasta "+str(valor_max))
        print ("El total de videos entre este rango es de "+str(om.size(catalog[caracteristica])))


    elif int(inputs[0]) == 3:
        pass

    elif int(inputs[0]) == 4:
        pass

    elif int(inputs[0]) == 5:
        pass

    elif int(inputs[0]) == 6:
        pass

    else:
        sys.exit(0)
sys.exit(0)
