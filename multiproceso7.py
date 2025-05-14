from multiprocessing import Process, Pipe

def laFuncion(conexion):
    conexion.send((789, None, None, 'Hola ', 'ICOs de Teotihuacan'))
    conexion.close()

if __name__ == '__main__':
    conexion_padre, conexion_hijo = Pipe()
    proceso = Process(target=laFuncion, args=(conexion_hijo,))
    proceso.start()
    print(conexion_padre.recv()) #imprime "(789, None, None, 'Hola ', 'ICOs de Teotihuacan')
    proceso.join()