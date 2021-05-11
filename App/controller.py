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
 """

import time
import tracemalloc
import config as cf
import model
import csv



"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

def loadData(catalog):
    start_time = time.process_time()
    
    

    loaduser_track_hastag(catalog)
    print("Se ha cargado user_track_hashtag...")
    Loadcontext_content_fratures(catalog)
    print("Se ha cargado context_content...")
    loadSentiment_value(catalog)
    print("Se ha cargado sentiment_value...")
    load_genero_musical(catalog)
    print("Se ha cargado los generos musicales...")
   
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    print(elapsed_time_mseg)
def Loadcontext_content_fratures(catalog):
    """
    
    """
    Contentfile = cf.data_dir + 'context_content_features-5pct.csv'
    input_file = csv.DictReader(open(Contentfile, encoding='utf-8'), delimiter=",")
    for content in input_file:
        model.addcontent(catalog,content)
        


def loadSentiment_value(catalog):
   
    valueSentimentFile = cf.data_dir + 'sentiment_values.csv'
    input_file = csv.DictReader(open(valueSentimentFile, encoding='utf-8'), delimiter=",")
    for valuesent in input_file:
        model.addSentiment(catalog, valuesent)


def loaduser_track_hastag(catalog):


    HastagFile = cf.data_dir + 'user_track_hashtag_timestamp-5pct.csv'
    input_file = csv.DictReader(open(HastagFile, encoding='utf-8'), delimiter=",")
    for hashtagtrack in input_file:
        model.addHashtagtrack(catalog, hashtagtrack)

        
def load_genero_musical(catalog):
    genero_file=cf.data_dir+"tabla_generos.csv"
    input_file = csv.DictReader(open(genero_file, encoding='utf-8'), delimiter=";")
    for genero in input_file:
        model.addgenero(catalog,genero)


# Funciones para la carga de datos


# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def size_trees(map):
    return model.size_trees(map)
def lt_size(lista):
    return model.lt_size(lista)
def range_values(map,low,high):
    return model.range_values(map,low,high)
def conteo_llaves_unicas(lst):
    return model.conteo_llaves_unicas(lst)
def conteo_range_value(lista):
    return model.conteo_range_value(lista)
def cmpare_two_list(list1,list2):
    return model.cmpare_two_list(list1,list2)
def list_only_id(list,coso):
    return model.list_only_id(list,coso)
def min_tree(catalog):
    return model.min_tree(catalog)
def max_tree(catalog):
    return model.max_tree(catalog)
def random_select(list,n):    
    return model.random_select(list,n)
def get_caracteristic_by_id(catalog,id,caracteristica):
    return model.get_caracteristic_by_id(catalog,id,caracteristica)
def get_someting_map(catalog,id,dato):
    return model.get_someting_map(catalog,id,dato)
def len_map(catalog):
    return model.len_map(catalog)
def add_new_genero():
    return model.add_new_genero()
def lista_por_genero(generos,catalog):
    return model.lista_por_genero(generos,catalog)
def add_new_genero(catalog,genero,min,max):
    return model.add_new_genero(catalog,genero,min,max)
def transform_hora(hora):
    return model.transform_hora(hora)
def lista_1_elemento(lista,coso,i,k):
    return lista_1_elemento(lista,coso,i,k)
def zise_list_map(list,n):
    return zise_list_map(list,n)
def num_keys_list(list,n):
    return num_keys_list(list,n)
def values_maps(map):
    return model.values_maps(map)
def cantidad_por_genero(lista,catalog):
    return model.cantidad_por_genero(lista,catalog)
def Top_tracks_hashtag(lista,catalog):
    return model.Top_tracks_hashtag(lista,catalog)




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