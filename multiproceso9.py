from multiprocessing import Process, Value, Array

def laFuncion(elNumero, elArreglo):
    elNumero.value = 92.83664365672
    for contador in range(len(elArrglo)):
        elArreglo(contador) = -elArreglo(contador)
        
if __name__ == '__main__':
    numero = Value('d', 0.0)
    arreglo = Array('i', range(100))
    
    proceso = Process(target=laFuncion, args=(numero, arreglo))
    proceso.start()
    proceso.join()
    
    print(numero.value)
    print(arreglo(:))
    
"""
los argumentos 'd' y 'i' utilizados al crear numero y arreglo
son codigo de tipo del tipo utilizado por array module:
'd' indica un flotante de doble precision
'i' indica un entero con signo
Estos objetos compartidos seran seguros para procesos y subprocesos.

para una mayor flexibilidad en el uso de la memoria compartida,
se puede usar el modulo multiprocessing.sharedctypes que admite la
creacion arbitraria de objetos ctypes asignados desde la memoria compartida.
"""