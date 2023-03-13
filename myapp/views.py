from django.shortcuts import render

# Create your views here.
def index(request):
    a = 2+2
    context = {"result": a}
    return render(request, "index.html", context)

def house(request):
    return render(request, "index.html")