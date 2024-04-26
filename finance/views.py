from django.shortcuts import render
from .models import Clientes, Transacciones

def clientes(request):
    clientes = Clientes.objects.all()
    return render(request, 'finance/clientes.html', {'clientes':clientes})

def transacciones(request):
    transacciones = Transacciones.objects.all()
    return render(request, 'finance/transacciones.html', {'transacciones':transacciones})