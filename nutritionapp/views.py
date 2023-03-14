from django.shortcuts import render
# from transformers import pipeline
# from pprint import pprint

# generator = pipeline('text-generation', model='distilgpt2')

# Create your views here.
def index(request):

    message = ""
    if request.method == "POST":
        message = "hello there"
        # prompt = request.POST.get("input", "")
        # message = generator(prompt, min_length=30, max_length=60)
    context = {"message": message}

    return render(request, "index.html", context)