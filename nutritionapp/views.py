from django.shortcuts import render
# from transformers import pipeline
# from pprint import pprint

# Create your views here.
def index(request):

    message = ""
    if request.method == "POST":
        message = "hello there"
    context = {"message": message}

    return render(request, "index.html", context)