from multiprocessing import Pool, TimeoutError
import time
import os

def laMultiplicacion(valor):
    return valor*valor

if __name__ == '__main__':
    # iniciar 10 procesos de tabajo
    pool = Pool(processes=10)
        
        # imprime "[0, 1, 4,..., 361]"
    print(pool.map(laMultiplicacion, range(20)))
        
        # imrpimir los mismos numeros en roden arbitrario
    for contador in pool.imap_unordered(laMultiplicacion, range(20)):
            print(contador)
            
        # evaluar "laFuncion(20)" de forma asincrona
    resultado = pool.apply_async(laMultiplicacion, (50,)) # se ejecuta en *solo* un proceso
    print(resultado.get(timeout=1)) # imprime "2500"
        
        # evaluar "os.getpid()" de forma asincrona
    resultado = pool.apply_async(os.getpid, ()) # se ejecuta en *solo* un proceso
    print(resultado.get(timeout=1)) # imprime el PID de ese proceso
        
        # lanzar multiples evaluaciones de forma asincrona *puede* utilizar mas procesos
    multiplesResultados = [pool.apply_async(os.getpid, ()) for i in range(4)]
    print([resultado.get(timeout=1) for resultado in multiplesResultados])
        
        # hacer que un solo trabajador duerma durante 10 segundos
    resultado = pool.apply_async(time.sleep, (10,))
    try:
        print(resultado.get(timeout=1))
    except TimeoutError:
        print("Nos falto paciencia y obtuvimos un multiprocesamiento. Error de tiempo de espera")
            
    print("Por el momento el pool sigue disponible para mas trabajos")
    
    # cerrar el pool
    pool.close()
    pool.join()
    
    # salir deteniendo el pool
    print("Ahora el pool esta cerrado y ya no esta disponible")
    
"""
los metodos de una piscina (pool) solo deben ser utilizados por el proceso que lo creo.
"""