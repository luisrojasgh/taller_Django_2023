from django.shortcuts import render

def inicio(request):
    titulo = "inicio"
    nombre = "Luis Villegas"
    context={
        "titulo": titulo,
        "nombre": nombre,
    }
    return render(request, 'index.html', context)


