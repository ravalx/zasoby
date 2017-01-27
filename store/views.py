from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Nr_ST

class StoreListView(ListView):
    model = Nr_ST 
'''
class AuthorDetailView(DetailView):
    model = Author

# Create your views here.
'''
