from django.shortcuts import render
from .models import Message

def home(request):
    Message.objects.get_or_create(text="My Django app is connected to PostgreSQL!")
    messages = Message.objects.all().order_by("-created_at")
    return render(request, "core/home.html", {"messages": messages})
