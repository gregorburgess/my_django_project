from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import TodoItem
import openai
from django.conf import settings

# Create your views here.

def home(request):
    #return HttpResponse(re"Hello, World!")
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def chat_with_gpt(request):
    openai.api_key = settings.OPENAI_API_KEY
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Hello, how can I assist you today?",
        max_tokens=50
    )
    return JsonResponse(response)