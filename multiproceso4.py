import multiprocessing as multiproceso

def cualquiera(cola):
    cola.put('Ingenieria en computacion')

if __name__ == '__main__':
    multiproceso.set_start_method('spawn')
    cola = multiproceso.Queue()
    proceso = multiproceso.Process(target=cualquiera, args=(cola,))
    proceso.start()
    print(cola.get())
    proceso.join()
    
"""
set_start_method() no deberia ser usada mas de una vez en el programa.
"""
    