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
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as m
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
def newCatalog():
   
    catalog = {'content': None,
               'sentiment_val': None,
               'hashtag_track': None,
               "artist": None,
               "track":None
              }
    catalog['content'] = lt.newList('ARRAY_LIST', compareIds)
    catalog['sentiment_val'] =  lt.newList('ARRAY_LIST', compareIds)
    catalog['hashtag_track'] =  lt.newList('ARRAY_LIST', compareIds)
    #trees
    catalog['artist'] = om.newMap(omaptype='BST',
                                      comparefunction=compareIds)
    catalog['track'] = om.newMap(omaptype='BST',
                                      comparefunction=compareIds)
    catalog['instrumentalness'] = om.newMap(omaptype='BST',
                                      comparefunction=compareIds)
    catalog['liveness'] = om.newMap(omaptype='BST',
                                      comparefunction=compareIds)
    catalog['speechiness'] = om.newMap(omaptype='BST',
                                      comparefunction=compareIds)
    catalog['danceability'] = om.newMap(omaptype='BST',
                                      comparefunction=compareIds)
    catalog['valence'] = om.newMap(omaptype='BST',
                                      comparefunction=compareIds)
    catalog['loudness'] = om.newMap(omaptype='BST',
                                      comparefunction=compareIds)
    catalog['tempo'] = om.newMap(omaptype='BST',
                                      comparefunction=compareIds)
    catalog['acousticness'] = om.newMap(omaptype='BST',
                                      comparefunction=compareIds)
    catalog['energy'] = om.newMap(omaptype='BST',
                                      comparefunction=compareIds)
    catalog['mode'] = om.newMap(omaptype='BST',
                                      comparefunction=compareIds)
    catalog['key'] = om.newMap(omaptype='BST',
                                      comparefunction=compareIds)

  


    return catalog

# Construccion de modelos

# Funciones para agregar informacion al catalogo

def addcontent(catalog, content):
    updateIndex(catalog['artist'], content,"artist_id","track_id")
    updateIndex(catalog["track"], content,"track_id","artist_id" )
    updateIndex(catalog['instrumentalness'], content,"instrumentalness","track_id")
    updateIndex(catalog["liveness"], content,"liveness","artist_id" )
    updateIndex(catalog['speechiness'], content,"speechiness","track_id")
    updateIndex(catalog["danceability"], content,"danceability","artist_id" )
    updateIndex(catalog['valence'], content,"valence","track_id")
    updateIndex(catalog["loudness"], content,"loudness","artist_id" )
    updateIndex(catalog['tempo'], content,"tempo","track_id")
    updateIndex(catalog["acousticness"], content,"acousticness","artist_id" )
    updateIndex(catalog['energy'], content,"energy","track_id")
    updateIndex(catalog["mode"], content,"mode","artist_id" )
    updateIndex(catalog['key'], content,"key","track_id")
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
    entry['index'] = m.newMap(numelements=30,
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
