"""multiprocessing (multiprocesamiento) es un paquete que admite procesos
de generacion utilinzado una API similar al modulo de threading (subprocesamiento).
EL paquete de multiprocesamiento ofrece concurrencia tanto local como remota,
evitando efectivamente el bloqueo global del interprete
mediante el uso de subprocesos en ligar de hilos. Debido a esto,
el modulo de multiprocesamiento permite al programador aprovechar
al maximo varios procesadores en una maquina determinada.
Se ejecuta tanto en POSIX como en Windows.

El modulo multiprocessing ademas provee una API que no tienen
analogos en el modulo threading. Un ejemplo es el objeto Pool
que permite paralelizar la ejecucion de una funcion
usando multiples valores de entrada, distribuyendolos a
traves de procesos (paralelismo de datos).
El siguiente ejemplo muestra como definir tales
funciones en un modulo para que los procesos secundarios
importen satisfactoriamente ese modulo.
"""

from multiprocessing import Pool

def cualquierFuncion(dato):
    return dato*dato*2

if __name__  ==  '_main_':
    with Pool(7) as elPool:
        print(elPool.map(cualquierFuncion, [7, 2.8, 43, 9, 4.6]))
