from django.shortcuts import render

# Create your views here.
def Inicio (request):
    return render(request,'Usuario/Inicio.html')

def Formulario (request):
    return render(request,'Usuario/Formulario.html')
    
def RecetaTradicional (request):
    return render(request,'Usuario/RecetaTradicional.html')

def RecetaVegana  (request):
    return render(request,'Usuario/RecetaVegana.html')

def RecetaReposteria  (request):
    return render(request,'Usuario/RecetaReposteria.html')



