from django.shortcuts import render
# from .utils import chat
from .utils import alpaca

# Create your views here.
def index(request):

    message = ""
    if request.method == "POST":
        message = alpaca(request.POST['input'])
    context = {"message": message}

    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")