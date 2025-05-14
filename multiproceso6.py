from multiprocessing import Process, Queue

def unaFuncion(cola):
    cola.put((732, None, 'Ingenieria en computacion', None, "Otra cosa","Mas cosas"))
    
if __name__ == '__main__':
    cola = Queue()
    proceso = Process(target=unaFuncion, args=(cola,))
    proceso.start
    print(cola.get())  #imprime "(732, None, 'Ingenieria en computacion')"
    proceso.join()
    
"""
las colas Queue son hilos y procesos seguros.
"""