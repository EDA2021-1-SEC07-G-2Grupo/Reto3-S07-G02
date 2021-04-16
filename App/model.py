"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
def newCatalog():
   
    catalog = {'content': None,
               'sentiment_val': None,
               'hashtag_track': None,
              }
    catalog['content'] = lt.newList('ARRAY_LIST', compareIds)


    catalog['sentiment_val'] =  lt.newList('ARRAY_LIST', compareIds)
    catalog['hashtag_track'] =  lt.newList('ARRAY_LIST', compareIds)

    return catalog

# Construccion de modelos

# Funciones para agregar informacion al catalogo

def addcontent(catalog, content):
    lt.addLast(catalog['content'], content)

def addSentiment(catalog,valuesent):
    lt.addLast(catalog["sentiment_val"],valuesent)

def addHashtagtrack(catalog,hashtag):
    lt.addLast(catalog["hashtag_track"],hashtag)



# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

def compareIds(id1, id2):
    """
    Compara dos crimenes
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1