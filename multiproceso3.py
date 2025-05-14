"""
1.- los procesos se generan creando un objeto Process
2.- luego llamar a su metodo start().

Para mostrar las IDs individuales que participan en el proceso, modificamos el ejemplo:
"""

from multiprocessing import Process
import os

def informacion(titulo):
    print(titulo)
    print('Nombre del modulo:', __name__)
    print('Proceso padre:', os.getppid())
    print('Id del proceso:', os.getpid())
    
def unaFuncion(nombre1, nombre2, nombre3):
    informacion('Funcion unaFuncion')
    print('Hola', nombre1, nombre2,nombre3)