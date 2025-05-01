class MetodosOrdenamiento:
    def sortByBubble(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arreglo[j] > arreglo[j + 1]:
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
        return arreglo
    
    def sort_seleccion(self, arreglo):
        arreglo = arreglo.copy()
        for i in range(len(arreglo) - 1):
            indice_minimo = i
            for j in range(i + 1, len(arreglo)):
                if arreglo[j] < arreglo[indice_minimo]:
                    indice_minimo = j
            arreglo[i], arreglo[indice_minimo] = arreglo[indice_minimo], arreglo[i]
        return arreglo


