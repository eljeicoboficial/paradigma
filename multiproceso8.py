from multiprocessing import Process, Lock

def laFuncion(control, conteo):
    control.acquire() #bloquear
    try:
        print('Hola ICOs mios', conteo)
    finally:
        control.release() #liberar si esta disponible
    
if __name__ == '__main__':
    candado = Lock()
    
    for contador in range(100):
        Process(target=laFuncion, args=(candado, contador)).start()
    
"""
sin usar el candado (Lock) de salida de los diferentes procesos,
es probable que todo se mezcle.
"""