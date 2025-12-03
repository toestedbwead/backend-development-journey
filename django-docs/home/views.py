from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("""
        <h1> Welcome to my Django First Site! </h1>
        <p><a href="/polls/">Go to polls app</a></p>
        <p><a href="/admin/">Admin Panel</a></p>
""")