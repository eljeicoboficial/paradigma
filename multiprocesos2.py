"""
La clase Process
1.- Los procesos se generan cerrando un objeto Process
2.- luego llama a su estado start() .

Vea ejemplo clasico de un programa multiprogreso:
"""
from multiprocessing import Process

def unProcedimiento(nombre, nombre2, nombre3):
    print('hola', nombre, nombre2, nombre3)
    
if __name__ == '__main__':
    elPool = Process(target=unProcedimiento, args=('guapo', 'hermosos', 'listo',))
    elPool.start()
    elPool.join()