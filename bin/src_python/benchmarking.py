import random
import time
from metodos_ordenamiento import MetodosOrdenamiento

class Benchmarking:
    def __init__(self):
        print('Bench initialization')

    def ejemplo(self):
        self.mO = MetodosOrdenamiento()

        self.mOrdenamiento = MetodosOrdenamiento()
        array = self.buildArreglo(5000)

        task = lambda: self.mOrdenamiento.sortByBubble(array)
        timeMillis = self.count_with_current_time_milles(task)
        timeNanno = self.count_with_nanno_time(task)

        print(f'Time Millis: {timeMillis}')
        print(f'Time Nanno: {timeNanno}')

    def buildArreglo(self, size):
        return [random.randint(0, 99999) for _ in range(size)]

    def count_with_current_time_milles(self, task):
        start = time.time()
        task()
        end = time.time()
        return end - start

    def count_with_nanno_time(self, task):
        start = time.time_ns()
        task()
        end = time.time_ns()
        return end - start
    
    def medir_tiempo(self, tarea, array):
        inicio = time.perf_counter()
        tarea(array)
        fin = time.perf_counter()
        return end - start 

