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
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """

    loaduser_track_hastag(catalog)
    Loadcontext_content_fratures(catalog)
    loadSentiment_value(catalog)


def Loadcontext_content_fratures(catalog):
    """
    
    """
    Contentfile = cf.data_dir + 'context_content_features-small.csv'
    input_file = csv.DictReader(open(Contentfile, encoding='utf-8'), delimiter=",")
    for content in input_file:
        model.addcontent(catalog,content)
        


def loadSentiment_value(catalog):
    """
    Carga la información que asocia tags con libros.
    """
    valueSentimentFile = cf.data_dir + 'sentiment_values.csv'
    input_file = csv.DictReader(open(valueSentimentFile, encoding='utf-8'), delimiter=",")
    for valuesent in input_file:
        model.addSentiment(catalog, valuesent)


def loaduser_track_hastag(catalog):
    """
    Carga la información que asocia tags con libros.
    """
    HastagFile = cf.data_dir + 'user_track_hashtag_timestamp-small.csv'
    input_file = csv.DictReader(open(HastagFile, encoding='utf-8'), delimiter=",")
    for hashtagtrack in input_file:
        model.addHashtagtrack(catalog, hashtagtrack)


# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
