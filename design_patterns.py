# patron strategy clasico a-la design patterns

# vamos con clases que implementan los 3 algoritmos clásicos de O(n log n)

class MergeSorter:

    def sort(self, s):
        if len(s) > 1:
            mid = len(s) // 2
            l = s[:mid]
            r = s[mid:]
            self.sort(l)
            self.sort(r)

            i = j = k = 0
            while i < len(l) and j < len(r):
                if l[i] <= r[j]:
                    s[k] = l[i]
                    i = i + 1
                else:
                    s[k] = r[j]
                    j = j + 1
                k = k + 1

            while i < len(l):
                s[k] = l[i]
                i = i + 1
                k = k + 1

            while j < len(r):
                s[k] = r[j]
                j = j + 1
                k = k + 1

class HeapSorter:

    def _heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self._heapify(arr, n, largest)

    def sort(self, s):
        ls = len(s)
        for k in range(ls // 2 - 1, -1, -1):
            self._heapify(s, ls, k)

        for k in range(ls - 1, 0, -1):
            s[k], s[0] = s[0], s[k]
            self._heapify(s, k, 0)


class QuickSorter:

    def sort(self, s):
        n = len(s)
        self._quick(s, 0, n - 1)

    def _partition(self, arr, low, high):
        i = (low - 1)
        pivot = arr[high]  # arbitrario, podría ser otro

        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def _quick(self, arr, low, high):
        if low < high:
            pi = self._partition(arr, low, high)
            self._quick(arr, low, pi - 1)
            self._quick(arr, pi + 1, high)


quick = QuickSorter()  # instanciamos nuestros felices ordenadores
heap = HeapSorter()
merge = MergeSorter()


def alguna_cosa_re_random():
    pass


def otra_cosa_re_random():
    pass


def alguna_funcion_que_por_alguna_razon_necesita_ordenar_listas(s, sorter):
    sorter.sort(s)
    alguna_cosa_re_random()
    otra_cosa_re_random()


lista_loca = [1, 3, 6, 4, 6, 2, 576, 6, 2, 13, 456, 32, 41, 64, 567, 44, 87, 5, 2, 4, 7, 65, 2, 4, 57, 6, 43, 5, 7, 45,
              2, 43, 7, 87]
alguna_funcion_que_por_alguna_razon_necesita_ordenar_listas(lista_loca.copy(), quick)
alguna_funcion_que_por_alguna_razon_necesita_ordenar_listas(lista_loca.copy(), merge)
alguna_funcion_que_por_alguna_razon_necesita_ordenar_listas(lista_loca.copy(), heap)

# pero momento, esto se parece mucho a lo que hice en sorters.py pero usando clases
# esto es lo que el design patterns te sugeriría hacer, y digamos tiene cierto sentido
# esto así como está es muuuuy parecido a lo que podrías hacer en PHP o Java
# PERO ESTO ES PYTHON BEIBE
# por eso en sorters.py hice lo que hice, usé el feature de que las funciones sean de alto orden en python
# desde la práctica es lo mismo, porque de todas formas inyecto comportamiento intercambiable en aquello que necesite ese comportamiento


# critiquemos el observer de pluralsight!

# más allá de si el patrón observer es bueno o malo por lo que sea, veamos la implementación de
# pluralsight en particular


# hagamoslo como si fuera mas a lo mixin que con abstract classes

class Notifier:
    _observers = set()

    def attach(self, observer):
        self._observers.add(observer)  # TIPADO DINAMICO LOCO

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, value=None):
        for observer in self._observers:
            observer.update(value)


class TicketCounting:
    def __init__(self):
        _open_tickets = -1
        _closed_tickets = -1
        _new_tickets = -1


class KPISystem(TicketCounting, Notifier):
    @property
    def open_tickets(self):
        return self._open_tickets

    @property
    def closed_tickets(self):
        return self._closed_tickets

    @property
    def new_tickets(self):
        return self._new_tickets

    def set_kpis(self, open_tickets, closed_tickets, new_tickets):
        self._open_tickets = open_tickets
        self._closed_tickets = closed_tickets
        self._new_tickets = new_tickets
        self.notify()


class CurrentKPIs(TicketCounting):
    def __init__(self, ticket_system):
        super().__init__()
        self._kpis = ticket_system
        ticket_system.attach(self)

    def update(self):
        self._open_tickets = self._kpis.open_tickets
        self._closed_tickets = self._kpis.closed_tickets
        self._new_tickets = self._kpis.new_tickets
        self.display()

    def display(self):
        print('Current open tickets: {}'.format(self._open_tickets))
        print('New tickets in last hour: {}'.format(self._closed_tickets))
        print('Tickets closed in last hour: {}'.format(self._new_tickets))
        print('*****\n')


class ForecastKPIs(TicketCounting):

    def __init__(self, ticket_system):
        super().__init__()
        self._kpis = ticket_system
        ticket_system.attach(self)

    def update(self):
        self._open_tickets = self._kpis.open_tickets
        self._closed_tickets = self._kpis.closed_tickets
        self._new_tickets = self._kpis.new_tickets
        self.display()

    def display(self):
        print('Forecast open tickets: {}'.format(self._open_tickets))
        print('New tickets expected in next hour: {}'.format(self._closed_tickets))
        print('Tickets expected to be closed in next hour: {}'.format(self._new_tickets))
        print('*****\n')


class AlgoConlosKPIs(TicketCounting):

    def __init__(self, ticket_system):
        super().__init__()
        self._kpis = ticket_system
        ticket_system.attach(self)

    def display(self):
        print('algo ocn los abiertnos: {}'.format(self._open_tickets))
        print('algo con los esperados: {}'.format(self._closed_tickets))
        print('algo con los cerrados: {}'.format(self._new_tickets))
        print('*****\n')


kpis = KPISystem()
currentKPIs = CurrentKPIs(kpis)
forecastKPIs = ForecastKPIs(kpis)
algoKPIs = AlgoConlosKPIs(kpis)
kpis.set_kpis(25, 10, 5)
kpis.set_kpis(100, 50, 30)
kpis.set_kpis(50, 10, 20)
