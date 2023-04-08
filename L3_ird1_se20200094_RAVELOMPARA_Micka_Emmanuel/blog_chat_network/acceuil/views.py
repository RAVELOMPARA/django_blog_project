from django.shortcuts import render
import mysql.connector
# Create your views here.
def page_acceuil (request): 
    return render(request, 'Acceuil.html')