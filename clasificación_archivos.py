"""
Clasifica archivos según su extensión
"""

import os
import time

directorio='/Users/Erick/Desktop/clasi'  #directorio objetivo

categorias= {'Imagenes': ['jpg', 'jpeg', 'png'],  #categorías a clasificar
             'PDF': ['pdf'],
             'Videos': ['mp4']}

for categoria in ['Imagenes', 'PDF', 'Videos']:
    os.makedirs(os.path.join(directorio,categoria), exist_ok=True)   #se crean las carpetas 


def clasifica_archivos(nombre_archivo):        #clasifica los archivos
    extension=nombre_archivo.split('.')[-1]
    for categoria, extensiones in categorias.items():
        if extension in extensiones:
            directorio_fuente=os.path.join(directorio,nombre_archivo)
            directorio_destino=os.path.join(directorio, categoria, nombre_archivo)
            
            os.rename(directorio_fuente, directorio_destino)
            print(f'se movió {nombre_archivo} a {categoria}')   #imprime un mensaje de que los archivos fueron movidos
            break
    
    

for nombre_archivo in os.listdir(directorio):      #Clasifica los archivos que ya están dentro de la carpeta ojetivo
    clasifica_archivos(nombre_archivo)
    
    

archivos_iniciales=os.listdir(directorio)   
    
    
while True:           #ejecuta un ciclo para archivos que se añadan dentro de la carpeta
    time.sleep(5)
    archivo_actual=os.listdir(directorio)
        
    nuevo_archivo=list(set(archivo_actual)-set(archivos_iniciales))
        
    for nombre_archivo in nuevo_archivo:
        clasifica_archivos(nombre_archivo)
    
    archivos_iniciales=archivo_actual
            
