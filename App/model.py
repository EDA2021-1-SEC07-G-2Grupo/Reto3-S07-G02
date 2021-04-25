﻿"""
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
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as m
assert cf
import random

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
def newCatalog():
   
    catalog = {'content': None,
               'sentiment_val': None,
               'hashtag_track': None,
               "artist": None,
               "track":None,
               "instrumentalness_id_trak":None
              }
    catalog['content'] = lt.newList('ARRAY_LIST', compareIds)
    catalog['sentiment_val'] =  lt.newList('ARRAY_LIST', compareIds)
    catalog['hashtag_track'] =  lt.newList('ARRAY_LIST', compareIds)
    #maps
    catalog['artist'] = mp.newMap(70000,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   comparefunction=comparekeys)
    catalog['track'] = mp.newMap(70000,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   comparefunction=comparekeys)
    #trees
    catalog['instrumentalness'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareIds)
    catalog['liveness'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareIds)
    catalog['speechiness'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareIds)
    catalog['danceability'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareIds)
    catalog['valence'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareIds)
    catalog['tempo'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareIds)
    catalog['acousticness'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareIds)
    catalog['energy'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareIds)
    catalog['instrumentalness_id_trak'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareIds)
    catalog['tempo_id_track'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareIds)

  


    return catalog

# Construccion de modelos

# Funciones para agregar informacion al catalogo

def addcontent(catalog, content):
    #arbol
    updateIndex(catalog['instrumentalness'], content,"instrumentalness","artist_id")
    updateIndex(catalog["liveness"], content,"liveness","artist_id" )
    updateIndex(catalog['speechiness'], content,"speechiness","artist_id")
    updateIndex(catalog["danceability"], content,"danceability","artist_id" )
    updateIndex(catalog['valence'], content,"valence","artist_id")
    updateIndex(catalog['tempo'], content,"tempo","artist_id")
    updateIndex(catalog["acousticness"], content,"acousticness","artist_id")
    updateIndex(catalog['energy'], content,"energy","artist_id")
    updateIndex(catalog['instrumentalness_id_trak'], content,"instrumentalness","track_id")
    updateIndex(catalog['tempo_id_track'], content,"tempo","track_id")
    #map
    artist = content['artist_id'].split(",") 
    track_id = content['track_id'].split(",")  #obtener por categoría
    for artista in artist:
        addsongmap(catalog, artista, content,"artist")
    for track in track_id:
        addsongmap(catalog, track, content,"track")
    #array
    lt.addLast(catalog['content'], content)
    return catalog

def addSentiment(catalog,valuesent):
    lt.addLast(catalog["sentiment_val"],valuesent)
    return catalog

def addHashtagtrack(catalog,hashtag):
    lt.addLast(catalog["hashtag_track"],hashtag)
    return catalog


# Funciones para creacion de datos
def updateIndex(map, content, llave, indice):
    num = content[llave]
    
    num=float(num)
    entry = om.get(map, num )
    if entry is None:
        datentry = newdataentry(content)
        om.put(map, num, datentry)
    else:
        datentry = me.getValue(entry)
    addIndex(datentry,content,indice)
    return map

def newdataentry(content):
    entry = {'index': None, 'song': None}
    entry['index'] = m.newMap(numelements=100,
                                     maptype='PROBING',
                                     comparefunction=comparekeys)
    entry['song'] = lt.newList('SINGLE_LINKED', compareIds)
    return entry


def addIndex(datentry, contenido,indice):
    lst = datentry['song']
    lt.addLast(lst, contenido)
    indexs = datentry["index"]
    inxentry = m.get(indexs, contenido[indice])
    if (inxentry is None):
        entry = newinxentry(contenido[indice], contenido)
        lt.addLast(entry['ltssongs'], contenido)
        m.put(indexs, contenido[indice], entry)
    else:
        entry = me.getValue(inxentry)
        lt.addLast(entry['ltssongs'], contenido)
    return datentry

def newinxentry(trak_id, content):
    """
    Crea una entrada en el indice por tipo de crimen, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    entry = {'song': None, 'ltssongs': None}
    entry['song'] = trak_id
    entry['ltssongs'] = lt.newList('SINGLELINKED', comparekeys)
    return entry

#//////////////////////////////////////////////////////////////////mapa
def addsongmap(catalog, indexs, content,map_name):

    indices = catalog[map_name]
    existencia_indice = mp.contains(indices, indexs)
    if existencia_indice:
        entry = mp.get(indices, indexs)
        ind = me.getValue(entry)
    else:
        ind = estructure(indexs)
        mp.put(indices, indexs, ind)
    lt.addLast(ind['song'], content)
def estructure(name):

    struct = {'name': "",
              "song": None,
              "Size": 0,
              }
    struct['name'] = name
    struct['song'] = lt.newList('ARRAY_LIST', comparekeys )
    return struct
# Funciones de consulta

def size_trees(map):
    return om.size(map)
def lt_size(lista):
    return lt.size(lista)
def range_values(map,low,high):
    return om.values(map,low,high)
def conteo_range_value(lista):
    total = 0
    for char in lt.iterator(lista):
        total += lt.size(char['song'])
    return total
def conteo_llaves_unicas(lista):
    total = 0
    for char in lt.iterator(lista):
        total += 1
    return total


def list_only_id(lista):
     lista_nuea=lt.newList(datastructure="ARRAY_LIST")
     for char in lt.iterator(lista):
            elemento=lt.getElement(char["song"],1)
            lt.addLast(lista_nuea, elemento["track_id"])
     return lista_nuea





def min_tree(catalog):
    return om.minKey(catalog)
def max_tree(catalog):
    return om.maxKey(catalog)
    
def random_select(list):
    newlist=lt.newList(datastructure="ARRAY_LIST")
    if lt.size(list)<5:
        n=lt.size(list)
    else:
        n=5

    i=0
    while i<n:
        num1=random.randint(0,lt.size(list))
        elemento=lt.getElement(list,num1)

        while lt.isPresent(newlist,elemento)!=0:
            num1=random.randint(0,lt.size(list))
            elemento=lt.getElement(list,num1)
        lt.addLast(newlist,elemento)
        i+=1
    return newlist 

def get_caracteristic_by_id(catalog,id,caracteristica):
    lista=om.values(catalog,id,id)
    for char in lt.iterator(lista):
            elemento=lt.getElement(char["song"],1)
            return elemento[caracteristica]
def get_someting_map(catalog,id,dato):
    wow=mp.get(catalog,id)
   
    elemento=lt.firstElement(wow["value"]["song"])
    elemento=elemento["value"]
    return elemento[dato]
def len_map(catalog):
    return mp.size(catalog)


# Funciones utilizadas para comparar elementos dentro de una lista
def cmpare_two_list(list1,list2):
    new_list=lt.newList("ARRAY_LIST")
    for char in lt.iterator(list1):
        if lt.isPresent(list2,char)>0:
            lt.addLast(new_list,char)
    return new_list
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
def comparekeys(key1, key2):
    """
    Compara dos tipos de crimenes
    """
    key = me.getKey(key2)
    if (key1 == key):
        return 0
    elif (key1 > key):
        return 1
    else:
        return -1
