from benchmarking import Benchmarking

if __name__ == "__main__":
    print("Funciona")
    Benchmarking()

    # .copy() sirve para que solo una instancia cambie
    # variables primitivas 
    #tuplas: () y no se pueden cambiar las variables internas
    #push: [] se pueden cambiar los valores. posiciones de adentro
    #Diccionarios: {} mapas, claves (casi siempre son strings)

    #Instancias
    metodos = MetodosOrdenamiento()
    benchmark = Benchmarking()
    size = 10000
    array_base = benchmark.build_array(size)

    #diccionario llamado metodos
    # tener 2 elementos
    # 1 - clave = burbuja valor de la funcion sin ()
    # 2 - clave = seleccion valor de la funcion sin()
    
    metodos = {
        "burbuja": metodos.sort_bubble,
        #si se pone parentesis se ejecuta la funcion sort_bubble()
        #self: instancia de toda la clase
        "seleccion": metodos.sort_seleccion,
    }

    resultados = []
    for nombre, metodo in metodos.items():
        #devuelve el arreglo de tuplas
        tiempo = benchmark.medir_tiempo(metodo, array_base)
        #aqui lo toma con los parentesis y lo ejecuta como funcion
        tuplaResultado = (size, nombre, tiempo)
        resultados.append(tuplaResultado)

    for resultado in resultados:
        #resultado tiplo tupla, recupera
        size, nombre, tiempo = resultado
        print(f'Tamaño:  {size}, Metodo: {nombre}, Tiempo: {tiempo:6f} segundos' )