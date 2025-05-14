from multiprocessing import Process, Manager

def laFuncion(diccionario, lista):
    diccionario[1] = '1'
    diccionario['2'] = 2
    diccionario[0.45] = None
    diccionario[2] = 'Calor'
    diccionario[2.2] = 'Frio'
    lista.reverse()
    #El metodo reverse() modifica la secuencia internamente,
    #por motivos de eficiencia espacial para secuencias muy grandes.
    #Como recordatorio al usuario de que el metodo produce un efecto secundario,
    #no se retorna la secuencia invertida.
    
if __name__ == '__main__':
    with Manager() as manager:
        diccionario = manager.dict()
        lista = manager.list(range(20))
        
        proceso = Process(target=laFuncion, args=(diccionario, lista))
        proceso.start()
        proceso.join()
        
        print(diccionario)
        print(lista)
        
