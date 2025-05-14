import multiprocessing as multiproceso

def cualquiera(cola):
    cola.put('Ingenieria en computacion')
    
if __name__ == '__main__':
    contexto = multiproceso.get_context('spawn')
    cola = contexto.Queue()
    proceso = contexto.Process(target=cualquiera, args=(cola,))
    proceso.start()
    print(cola.get())
    proceso.join()
    
