from unittest import loader
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

class Application():
        
    @staticmethod
    def attente(request):
        template = loader.get_template('main.html')
        return HttpResponse(template.render())