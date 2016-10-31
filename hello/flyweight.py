from .models import SaborDeNieve, Cliente, Orden

class SaboresFlyweightFactory(object):
    def __init__(self):
        self.__instances = dict()

    def get_instance(self, pk):
        if pk not in self.__instances:
            self.__instances[pk] = SaborDeNieve.objects.get(pk=pk)
        return self.__instances[pk]

class ClientesFlyweightFactory(object):
    def __init__(self):
        self.__instances = dict()

    def get_instance(self, pk):
        if pk not in self.__instances:
            self.__instances[pk] = Cliente.objects.get(pk=pk)
        return self.__instances[pk]

class OrdenesFlyweightFactory(object):
    def __init__(self):
        self.__instances = dict()

    def get_instance(self, pk):
        if pk not in self.__instances:
            self.__instances[pk] = Orden.objects.get(pk=pk)
        return self.__instances[pk]
