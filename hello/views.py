import time
from random import randint

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Greeting, SaborDeNieve, Cliente, Orden
from .flyweight import SaboresFlyweightFactory, ClientesFlyweightFactory, OrdenesFlyweightFactory

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def flyweight(request):
    menu = SaborDeNieve.objects.all()
    ordenes = Orden.objects.all()

    contexto = {}
    contexto['menu'] = menu
    contexto['ordenes'] = ordenes
    contexto['total_o'] = ordenes.count()
    
    return render(request, 'nieves.html', contexto)

def flyweight_num(request, num):
    num = int(num)
    sabores_fwf = SaboresFlyweightFactory()
    clientes_fwf = ClientesFlyweightFactory()
    ordenes = []

    start = time.time()
    for i in range(0, num):
        orden = Orden()
        cliente_pk = randint(1,100)
        orden.cliente = clientes_fwf.get_instance(cliente_pk)
        sabor_pk = randint(1,5)
        orden.sabor = sabores_fwf.get_instance(sabor_pk)
        cantidad = randint(1,5)
        orden.cantidad = cantidad
        orden.total = orden.sabor.precio * cantidad
        orden.save()
        ordenes.append(orden)
    end = time.time()

    contexto = {}
    contexto['ordenes'] = ordenes
    contexto['tiempo'] = end - start
    contexto['num_o'] = num
    
    return render(request, 'nieves.html', contexto)

def no_flyweight_num(request, num):
    num = int(num)
    ordenes = []

    start = time.time()
    for i in range(0, num):
        orden = Orden()
        orden.cliente = Cliente.objects.get(pk=randint(1,100))
        sabor_pk = randint(1,5)
        orden.sabor = SaborDeNieve.objects.get(pk=sabor_pk)
        cantidad = randint(1,5)
        orden.cantidad = cantidad
        orden.total = orden.sabor.precio * cantidad
        orden.save()
        ordenes.append(orden)
    end = time.time()

    contexto = {}
    contexto['ordenes'] = ordenes
    contexto['tiempo'] = end - start
    contexto['num_o'] = num
    
    return render(request, 'nieves.html', contexto)

def ordenes(request):
    ordenes = []
    ordenes_fwf = OrdenesFlyweightFactory()

    start = time.time()
    for i in range(0, 2000):
        num = randint(200, 1000)
        orden = ordenes_fwf.get_instance(num)
        ordenes.append(orden)
    end = time.time()
    
    contexto = {}
    contexto['ordenes'] = ordenes
    contexto['tiempo'] = end - start
    contexto['num_o'] = 2000
    contexto['con_fw'] = True
    
    return render(request, 'nieves.html', contexto)

def ordenes_no(request):
    ordenes = []
    ords = Orden.objects.all()

    start = time.time()
    for i in range(0, 2000):
        num = randint(200, 1000)
        #orden = Orden.objects.get(pk=num)
        orden = ords.get(pk=num)
        ordenes.append(orden)
    end = time.time()
    
    contexto = {}
    contexto['ordenes'] = ordenes
    contexto['tiempo'] = end - start
    contexto['num_o'] = 2000
    contexto['sin_fw'] = True
    
    return render(request, 'nieves.html', contexto)

def nueva_orden(request):
    menu = SaborDeNieve.objects.all()

    orden = Orden()
    orden.cliente = Cliente.objects.get(pk=randint(1,100))
    sabor = menu[randint(0,4)]
    orden.sabor = sabor
    cantidad = randint(1,5)
    orden.cantidad = cantidad
    orden.total = sabor.precio * cantidad
    orden.save()

    return redirect('flyweight')

def nueva_orden_num(request, num):
    num = int(num)
    sabores_fwf = SaboresFlyweightFactory()
    clientes_fwf = ClientesFlyweightFactory()

    for i in range(0, num):
        orden = Orden()
        cliente_pk = randint(1,100)
        orden.cliente = clientes_fwf.get_instance(cliente_pk)
        sabor_pk = randint(1,5)
        orden.sabor = sabores_fwf.get_instance(sabor_pk)
        cantidad = randint(1,5)
        orden.cantidad = cantidad
        orden.total = orden.sabor.precio * cantidad
        orden.save()

    return redirect('flyweight')
