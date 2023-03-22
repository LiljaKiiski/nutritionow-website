from django.shortcuts import render
from .utils import chat


# Create your views here.
def index(request):

    message = ""
    if request.method == "POST":
        message = chat(request.POST['input'])
    context = {"message": message}

    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")