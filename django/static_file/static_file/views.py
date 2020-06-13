#static_file/views.py
from django.shortcuts import render
#localhost:8000
def index(request):
    return render(request,"index.html")