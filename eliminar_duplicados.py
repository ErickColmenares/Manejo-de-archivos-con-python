"""
Elimina archivos duplicados
"""

import os
import re


def borrar_archivos_duplicados(directorio):  #función  para eliminar archivos
    archivos=os.listdir(directorio)  #obtenemos la lista de archivos
    
    for archivo in archivos:
        coincidencia = re.search(r'(.*)\s+\((\d+)\)\.(.*)', archivo) #revisamos si hay archivos duplicados
        if coincidencia:  #obtenemos el nombre original y la extensión
            nombre_base = coincidencia.group(1) 
            extension = coincidencia.group(3)
            archivo_original = nombre_base+ '.' + extension
            
            if archivo_original in archivos: #revisamos si ya exite en el directorio
                os.remove(os.path.join(directorio,archivo))

borrar_archivos_duplicados('/Users/Erick/Desktop/Nueva carpeta (2)')
                