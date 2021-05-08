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
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as m
assert cf
import random
from datetime import time
import time
import datetime


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
def newCatalog():
   
    catalog = {'content': None,
               "artist": None,
               "track":None,
               "instrumentalness_id_trak":None,
               "genero":None
              }
    catalog['content'] = lt.newList('ARRAY_LIST', compareIds)
   
    catalog['artist'] = mp.newMap(70000,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   comparefunction=comparekeys)
    catalog['track'] = mp.newMap(70000,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   comparefunction=comparekeys)
    catalog['genero'] = mp.newMap(20,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   comparefunction=comparekeys)
    catalog['value_sent'] = mp.newMap(70000,
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
    catalog['created_at'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareIds)


  


    return catalog

# Construccion de modelos

# Funciones para agregar informacion al catalogo

def addcontent(catalog, content):
    #arbol
    updateIndex(catalog['instrumentalness'], content,"instrumentalness","artist_id",False)
    updateIndex(catalog["liveness"], content,"liveness","artist_id",False )
    updateIndex(catalog['speechiness'], content,"speechiness","artist_id",False)
    updateIndex(catalog["danceability"], content,"danceability","artist_id",False )
    updateIndex(catalog['valence'], content,"valence","artist_id",False)
    updateIndex(catalog['tempo'], content,"tempo","artist_id",False)
    updateIndex(catalog["acousticness"], content,"acousticness","artist_id",False)
    updateIndex(catalog['energy'], content,"energy","artist_id",False)
    updateIndex(catalog['instrumentalness_id_trak'], content,"instrumentalness","track_id",False)
    updateIndex(catalog['tempo_id_track'], content,"tempo","track_id",False)
   
    #map
    artist = content['artist_id'].split(",") 
    track_id = content['track_id'].split(",")  #obtener por categoría
    for artista in artist:
        addsongmap(catalog, artista, content,"artist")
    for track in track_id:
        addsongmap(catalog, track, content,"track")
   
    #array
    lt.addLast(catalog['content'], content)
    

def addSentiment(catalog,valuesent):
    valuesents = valuesent['hashtag'].split(";") 
     
    for hastag in valuesents:
        addsongmap(catalog, hastag, valuesent,"value_sent")
     
    

def addHashtagtrack(catalog,hashtag):
    updateIndex(catalog['created_at'], hashtag,"created_at","track_id",True)


def addgenero(catalog,genero):

     generos = genero['Genero '].split(";") 
     
     for genero_Especifico in generos:
        addsongmap(catalog, genero_Especifico, genero,"genero")


# Funciones para creacion de datos
def updateIndex(map, content, llave, indice,date):
    num = content[llave]
    if date==True:
        num = datetime.datetime.strptime(num, '%Y-%m-%d %H:%M:%S')
        entry = om.get(map, num.time())
        num=num.time()
    elif date==False:
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
def add_new_genero(catalog,genero,min,max):
    elemento={"Genero ":genero ,"BPM_minimo":min,"BPM_maximo":max}
    addsongmap(catalog,genero,elemento,"genero")

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


def list_only_id(lista,coso):
     lista_nuea=lt.newList(datastructure="ARRAY_LIST")
     for char in lt.iterator(lista):
            elemento=lt.getElement(char["song"],1)
            lt.addLast(lista_nuea, elemento[coso])
     return lista_nuea
def lista_1_elemento(lista,coso,i,k):
    print(lt.size(lt.getElement(lista,i)))
    




def min_tree(catalog):
    return om.minKey(catalog)
def max_tree(catalog):
    return om.maxKey(catalog)
    
def random_select(list,n):
    newlist=lt.newList(datastructure="ARRAY_LIST")
    if lt.size(list)<n:
        n=lt.size(list)
    else:
        n=n

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
def get_someting_map(catalog, id,dato):
    wow=mp.get(catalog,id)
    elemento=lt.firstElement(wow["value"]["song"])
    return elemento[dato]
def len_map(catalog):
    return mp.size(catalog)

def transform_hora(hora):
        time=hora.split(":")
      
        result = datetime.time(int(time[0]),int(time[1]))
    
        return result

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpare_two_list(list1,list2):
    new_list=lt.newList("ARRAY_LIST")
    if lt.size(list1)>lt.size(list2):
        lista_pequenia=list2
        lista_grande=list1
    else:
        lista_pequenia=list1
        lista_grande=list2
    for char in lt.iterator(lista_pequenia):
        if lt.isPresent(lista_grande,char)>0:
            lt.addLast(new_list,char)
    return new_list



def lista_por_genero(catalog,n):
    minimo=float(get_someting_map(catalog["genero"],n,"BPM_minimo"))
    maximo=float(get_someting_map(catalog["genero"],n,"BPM_maximo"))
    tudo=(om.values(catalog["tempo"],minimo,maximo)) 
       
    return tudo
def cantidad_por_genero(lista,catalog):
    lista_but_ID=list_only_id(lista,"track_id")
    generso_musicales=values_maps(catalog["genero"])
    lista_que_se_imprime=lt.newList(datastructure="ARRAY_LIST")
    for char in lt.iterator(generso_musicales):
        lista_total=lista_por_genero(catalog,char)
        tempo_genero=list_only_id(lista_total,"track_id")
        one_list=cmpare_two_list(tempo_genero,lista_but_ID)
        dato={"Genero Musica":str(char),"Reproducciones totales":float(lt_size(one_list))}
        lt.addLast(lista_que_se_imprime,dato)
    lista_organizada=organizacion(lista_que_se_imprime,lt.size(lista_que_se_imprime))

    return lista_organizada



def values_maps(map):
    titulos_map=mp.keySet(map)
    return titulos_map
# Funciones de ordenamiento
def cmpfuncition_merge(video1, video2):

    return (float(video1["Reproducciones totales"]) > float(video2["Reproducciones totales"]))
def organizacion(catalog,size):
    sub_list = lt.subList(catalog,0, size)
    sub_list = catalog.copy()
    sorted_list=merg.sort(sub_list, cmpfuncition_merge)
    return  sorted_list

def compareIds(id1, id2):
    
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1
def comparekeys(key1, key2):
    
    key = me.getKey(key2)
    if (key1 == key):
        return 0
    elif (key1 > key):
        return 1
    else:
        return -1
