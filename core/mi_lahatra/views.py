from unittest import loader
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from mi_lahatra.models import Guichet
from mi_lahatra.models import Personne


class Application():
        
    @staticmethod
    def attente(request):
        template = loader.get_template('main.html')
        guichet = Guichet.objects.all().values()
        pers = Personne.objects.all().values()
        context = {
            'g': guichet,
            'p': pers,
        }
        return HttpResponse(template.render(context, request))
    
    @staticmethod
    def base(request):
        template = loader.get_template('base.html')
        guichet = Guichet.objects.all().values()
        pers = Personne.objects.all().values()
        context = {
            'g': guichet,
            'p': pers,
        }
        return HttpResponse(template.render(context, request))
    
    @staticmethod
    def ajout_pers(request):
        x = request.POST['input_nom']
        y = request.POST['input_guichet']
        pers = Personne(nom=x, guichet=y)
        pers.save()
        
        template = loader.get_template('base.html')
        guichet = Guichet.objects.all().values()
        pers = Personne.objects.all().values()
        context = {
            'g': guichet,
            'p': pers,
        }
        return HttpResponse(template.render(context, request))
    
    @staticmethod
    def ajout_guichet(request):
        template = loader.get_template('ajout_guichet.html')
        guichet = Guichet.objects.all().values()
        pers = Personne.objects.all().values()
        context = {
            'g': guichet,
            'p': pers,
        }
        return HttpResponse(template.render(context, request))
    
    @staticmethod
    def ajout_guichet_ajout(request):
        x = request.POST['input_nom']
        gui = Guichet(nom=x)
        gui.save()
        
        template = loader.get_template('base.html')
        guichet = Guichet.objects.all().values()
        pers = Personne.objects.all().values()
        context = {
            'g': guichet,
            'p': pers,
        }
        return HttpResponse(template.render(context, request))
    
    @staticmethod
    def suppr_personne(request, id):
        pers = Personne.objects.get(id=id)
        pers.delete()
        
        template = loader.get_template('base.html')
        guichet = Guichet.objects.all().values()
        pers = Personne.objects.all().values()
        context = {
            'g': guichet,
            'p': pers,
        }
        return HttpResponse(template.render(context, request))
    
    @staticmethod
    def suppr_guichet(request, id):
        gui = Guichet.objects.get(id=id)
        pers = Personne.objects.filter(guichet=gui.nom)
        gui.delete()
        pers.delete()
        
        template = loader.get_template('base.html')
        guichet = Guichet.objects.all().values()
        pers = Personne.objects.all().values()
        context = {
            'g': guichet,
            'p': pers,
        }
        return HttpResponse(template.render(context, request))
    
    @staticmethod
    def modif_guichet(request, id):
        mymember = Guichet.objects.get(id=id)
        template = loader.get_template('modif_guichet.html')
        context = {
            'g': mymember,
        }
        return HttpResponse(template.render(context, request))
    
    @staticmethod
    def modif_guichet_m(request, id):
        nom = request.POST['nom']
        member = Guichet.objects.get(id=id)
        try:
            pers = Personne.objects.get(guichet=member.nom)
            pers.guichet = nom
            pers.save()
        except:
            pass
        
        member.nom = nom
        member.save()

        template = loader.get_template('base.html')
        guichet = Guichet.objects.all().values()
        pers = Personne.objects.all().values()
        context = {
            'g': guichet,
            'p': pers,
        }
        return HttpResponse(template.render(context, request))
    
    @staticmethod
    def modif_personne(request, id):
        mymember = Personne.objects.get(id=id)
        template = loader.get_template('modif_personne.html')
        context = {
            'p': mymember,
        }
        return HttpResponse(template.render(context, request))
    
    @staticmethod
    def modif_personne_m(request, id):
        nom = request.POST['nom']
        gui = request.POST['guichet']
        member = Personne.objects.get(id=id)
        member.nom = nom
        member.guichet = gui
        member.save()
        
        template = loader.get_template('base.html')
        guichet = Guichet.objects.all().values()
        pers = Personne.objects.all().values()
        context = {
            'g': guichet,
            'p': pers,
        }
        return HttpResponse(template.render(context, request))