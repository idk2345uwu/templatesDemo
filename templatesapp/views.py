from django.shortcuts import render

def renderTemplate(request):
    data = {"nombre": "Wola"}
    return render(request, 'templatesapp/pagina.html', data)

def renderTemplate(request):
    data = {"nombre": "Seb"}
    return render(request, 'templatesapp/pagina2.html', data )
