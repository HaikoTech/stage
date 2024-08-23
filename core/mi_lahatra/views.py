from unittest import loader
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q

from mi_lahatra.models import Guichet
from mi_lahatra.models import Personne

from datetime import *

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
    def attente_main(request):
        template = loader.get_template('attente.html')
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

        date = datetime.now()
        date = date.strftime("%d/%m/%Y %H:%M:%S")

        context = {
            'g': guichet,
            'p': pers,
            'date': date,
        }
        return HttpResponse(template.render(context, request))
    
    @staticmethod
    def ajout_pers(request):
        x = request.POST['input_nom']
        y = request.POST['input_guichet']
        date = datetime.now()
        date = date.strftime("%d/%m/%Y %H:%M:%S")

        pers = Personne(nom=x, guichet=y)
        guichet = Guichet.objects.get(nom=y)
        guichet.nb_now += 1
        guichet.nb_personne += 1
        pers.numero = guichet.nb_now
        pers.date_temps = date
        pers.save()
        guichet.save()

        fin = f"{guichet.alpha}{pers.numero:03}"
         
        template = loader.get_template('main.html')
        guichet = Guichet.objects.all().values()
        pers = Personne.objects.all().values()
        context = {
            'g': guichet,
            'p': pers,
            'fin': fin,
        }
        return HttpResponse(template.render(context, request))
    
    @staticmethod
    def ajout_guichet(request):
        template = loader.get_template('ajout_guichet.html')
        guichet = Guichet.objects.all().values_list('alpha', flat=True)
        pers = Personne.objects.all().values()
        a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 

        a_filtered = [char for char in a if char not in guichet]
        guichet = Guichet.objects.all().values()

        context = {
            'g': guichet,
            'p': pers,
            'alpha': a_filtered,
        }
        return HttpResponse(template.render(context, request))
    
    @staticmethod
    def ajout_guichet_ajout(request):
        x = request.POST['input_nom']
        a = request.POST['input_alpha']
        gui = Guichet(nom=x, alpha=a)
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
    def suppr_personne(request, page, fini, id_guich):
        try:
            vraie_guichet = Guichet.objects.get(id=id_guich)
            guichet = vraie_guichet.nom
        except:
            vraie_guichet = {}
            guichet = {}

        try:
            pe = Personne.objects.get(statut='Load', guichet=guichet)
            pe.statut = "End"
            pe.save()

            # vraie_guichet.nb_personne -= 1
            # if vraie_guichet.nb_personne <= 0:
            #     vraie_guichet.nb_now = 0

            # vraie_guichet.save()
        except:
            pass

        try:
            if fini == 1:
                pers_suiv = Personne.objects.filter(statut='New', guichet=guichet).order_by('id').first()
                pers_suiv.statut = "Load"
                pers_suiv.save()
            elif fini == 0:
                pass

        except:
            pass



        template = loader.get_template(page+'.html')
        try:
            pers = Personne.objects.filter(guichet=guichet)
            p_now = Personne.objects.filter(statut='New', guichet=guichet).order_by('id').first()
        except:
            pers = {}
            p_now = {}

        context = {
            'g': vraie_guichet,
            'p': pers,
            'p_now': p_now,
        }
        return HttpResponse(template.render(context, request))

    
    @staticmethod
    def suppr_personne_page(request, page, id):
        template = loader.get_template(page+".html")

        guichet = Guichet.objects.get(id=id)
        pers = Personne.objects.filter(guichet=guichet.nom)
        try:
            p_now = Personne.objects.earliest('id')
        except:
            p_now = "0"
        context = {
            'g': guichet,
            'p': pers,
            'p_now': p_now,
        }
        return HttpResponse(template.render(context, request))
    
    @staticmethod
    def suppr_personne_base(request, page, id):
        pers = Personne.objects.get(id=id)
        guich = pers.guichet
        guichet = Guichet.objects.get(nom=guich)
        guichet.nb_now -= 0
        guichet.nb_personne -= 1

        pers.statut = "Load"

        if guichet.nb_personne <= 0:
            guichet.nb_now = 0
            guichet.nb_personne = 0

        guichet.save()
        pers.delete()

        
        template = loader.get_template(page+".html")

        if page == "guichet_id":
            guichet = Guichet.objects.get(nom=guich)
            pers = Personne.objects.filter(guichet=guichet.nom)
            try:
                p_now = Personne.objects.earliest('id')
            except:
                p_now = "0"
            context = {
                'g': guichet,
                'p': pers,
                'p_now': p_now,
            }
        else:
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

        guichet = Guichet.objects.all().values_list('alpha', flat=True)
        a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 

        a_filtered = [char for char in a if char not in guichet]

        context = {
            'g': mymember,
            'alpha': a_filtered,
        }
        return HttpResponse(template.render(context, request))
    
    @staticmethod
    def modif_guichet_m(request, id):
        nom_2 = ""
        nom = request.POST['nom']
        alpha = request.POST['alpha']
        member = Guichet.objects.get(id=id)
        all_member = Guichet.objects.filter(nom=nom).filter(~Q(id=id)).filter(~Q(alpha=alpha)).values()

        for i in all_member:
            nom_2 += str(i) + " | "
        
        if nom_2 != "" and nom_2 != nom:
            mymember = Guichet.objects.get(id=id)
            template = loader.get_template('modif_guichet.html')
            context = {
                'g': mymember,
            }
            return HttpResponse(template.render(context, request))

        else:
            # return HttpResponse("Aucun nom")

            try:
                pers = Personne.objects.get(guichet=member.nom)
                pers.guichet = nom
                pers.save()
            except:
                pass
            
            member.nom = nom
            member.alpha = alpha
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
        num = request.POST['numero']
        member = Personne.objects.get(id=id)
        member.nom = nom
        member.guichet = gui
        member.numero    = num
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
    def guichet(request):
        template = loader.get_template('guichet.html')
        guichet = Guichet.objects.all().values()
        pers = Personne.objects.all().values()
        context = {
            'g': guichet,
            'p': pers,
        }
        return HttpResponse(template.render(context, request))
    
    @staticmethod
    def guichet_id(request, id):
        template = loader.get_template('guichet_id.html')
        guichet = Guichet.objects.get(id=id)
        pers = Personne.objects.filter(guichet=guichet.nom)
        p_now = Personne.objects.filter(statut='New', guichet=guichet).order_by('id').first()

        p_if = Personne.objects.filter(statut='Load')

        context = {
            'g': guichet,
            'p': pers,
            'p_now': p_now,
            'p_if': p_if,
            'counter': range(len(pers)),
        }
        return HttpResponse(template.render(context, request))

