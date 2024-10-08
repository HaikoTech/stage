from unittest import loader
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q

from mi_lahatra.models import Guichet
from mi_lahatra.models import Personne
from mi_lahatra.models import Date
from mi_lahatra.models import Admin

from datetime import *

import openpyxl


class Application():

    @staticmethod   
    def get_date(request):
        date_base = Date.objects.all().values()
        date_list = list(date_base)

        return JsonResponse(date_list, safe=False)
    

    @staticmethod
    def change_day(request, page):
        date = datetime.now()
        date_str = date.strftime("%Y-%m-%d")

        date_base = Date.objects.get(id=1)
        date_base.valeur = date_str

        Guichet.objects.update(nb_now=0, nb_personne=0)

        template = loader.get_template(page)
        guichet = Guichet.objects.all().values()
        pers = Personne.objects.all().values()
        context = {
            'g': guichet,
            'p': pers,
            'admin_v': False,
        }
        return HttpResponse(template.render(context, request))

    @staticmethod
    def get_all_data(request):
        personnes = Personne.objects.all().values()
        personne_list = list(personnes)
        guichet = Guichet.objects.all().values()
        guichet_list = list(guichet)

        data = {
            'clients': personne_list,
            'guichets': guichet_list,
        }

        return JsonResponse(data, safe=False)
    

    @staticmethod
    def get_personne(request):
        personnes = Personne.objects.all().values()
        personne_list = list(personnes)

        return JsonResponse(personne_list, safe=False)
    

    @staticmethod
    def get_guichet(request):
        guichet = Guichet.objects.all().values()
        guichet_list = list(guichet)

        return JsonResponse(guichet_list, safe=False)
    

    @staticmethod
    def get_admin(request):
        admin = Admin.objects.all().values()
        admin_list = list(admin)

        return JsonResponse(admin_list, safe=False)
    

    @staticmethod
    def get_guichet(request):
        guichets = Guichet.objects.all().values()
        guichets_list = list(guichets)
        
        return JsonResponse(guichets_list, safe=False)
    
    @staticmethod
    def get_personne(request):
        personne = Personne.objects.all().values()
        personne_list = list(personne)

        return JsonResponse(personne_list, safe=False)

    @staticmethod
    def get_admin(request):
        admin = Admin.objects.all().values()
        admin_list = list(admin)
        
        return JsonResponse(admin_list, safe=False)
    
    @staticmethod
    def get_date_data(request):
        date = datetime.now()
        date_str = date.strftime("%d/%m/%Y %H:%M:%S")
        print("1")

        return JsonResponse(date_str, safe=False)
        

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
    def base(request, admin):
        template = loader.get_template('base.html')
        guichet = Guichet.objects.all().values()
        pers = Personne.objects.all().values()

        

        date = datetime.now()
        date = date.strftime("%d/%m/%Y %H:%M:%S")

        context = {
            'g': guichet,
            'p': pers,
            'date': date,
            'admin': "",
            'admin_v': admin,
        }
        return HttpResponse(template.render(context, request))


    @staticmethod
    def base_log(request):
        template = loader.get_template('base_log.html')
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
    def base_v(request):
        nom = request.POST['nom']
        mdp = request.POST['mdp']

        try:
            admin = Admin.objects.get(nom=nom, mdp=mdp)
            template = loader.get_template('base.html')
            guichet = Guichet.objects.all().values()
            pers = Personne.objects.all().values()

            date = datetime.now()
            date = date.strftime("%d/%m/%Y %H:%M:%S")

            context = {
                'g': guichet,
                'p': pers,
                'date': date,
                'admin': admin,
                'admin_v': True,
            }
            return HttpResponse(template.render(context, request))  
        except Exception as e:
            print(f"Erreur inattendue: {e}")
            template = loader.get_template('base_log.html')
            guichet = Guichet.objects.all().values()
            pers = Personne.objects.all().values()

            date = datetime.now()
            date = date.strftime("%d/%m/%Y %H:%M:%S")

            context = {
                'g': guichet,
                'p': pers,
                'date': date,
                'admin': False,
                'admin_v': False,
            }
            return HttpResponse(template.render(context, request))  

        
    @staticmethod
    def base_c(request):
        template = loader.get_template('base_change.html')
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
    def base_c_v(request):
        nom = request.POST['nom']
        old_mdp = request.POST['old_mdp']
        new_mdp = request.POST['new_mdp']

        try:
            admin = Admin.objects.get(nom=nom)

            if admin.mdp == old_mdp:
                admin.mdp = new_mdp
                template = loader.get_template('base.html')
                guichet = Guichet.objects.all().values()
                pers = Personne.objects.all().values()

                date = datetime.now()
                date = date.strftime("%d/%m/%Y %H:%M:%S")

                context = {
                    'g': guichet,
                    'p': pers,
                    'date': date,
                    'admin': admin,
                    'admin_v': True,
                }
                return HttpResponse(template.render(context, request))  
            else:
                template = loader.get_template('base_change.html')
                guichet = Guichet.objects.all().values()
                pers = Personne.objects.all().values()

                mess = "Le mot de passe est incorecte"

                date = datetime.now()
                date = date.strftime("%d/%m/%Y %H:%M:%S")

                context = {
                    'g': guichet,
                    'p': pers,
                    'date': date,
                    'admin': admin,
                    'message': mess,
                    'admin_v': True,
                }
                return HttpResponse(template.render(context, request))  
            
        except:
            template = loader.get_template('base_change.html')
            guichet = Guichet.objects.all().values()
            pers = Personne.objects.all().values()

            mess = "Le nom d'Utilisateur n'existe pas"

            date = datetime.now()
            date = date.strftime("%d/%m/%Y %H:%M:%S")

            context = {
                'g': guichet,
                'p': pers,
                'date': date,
                'admin': False,
                'message': mess,
                'admin_v': False,
            }
            return HttpResponse(template.render(context, request))  


    @staticmethod
    def test(request):
        template = loader.get_template('test.html')
        guichet = Guichet.objects.all().values()
        pers = Personne.objects.all().values()

        date = datetime.now()
        date_time = date.strftime("%d/%m/%Y %H:%M:%S")
        date = date.strftime("%d/%m/%Y")

        context = {
            'g': guichet,
            'p': pers,
            'date_time': date_time,
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
         
        template = loader.get_template('numero.html')
        guichet = Guichet.objects.all().values()
        pers = Personne.objects.all().values()
        context = {
            'g': guichet,
            'p': pers,
            'fin': fin,
        }
        return HttpResponse(template.render(context, request))
    

    @staticmethod
    def main(request):         
        template = loader.get_template('main.html')
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
        guichet = Guichet.objects.all().values_list('alpha', flat=True)
        pers = Personne.objects.all().values()
        a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 

        a_filtered = [char for char in a if char not in guichet]
        guichet = Guichet.objects.all().values()

        context = {
            'g': guichet,
            'p': pers,
            'alpha': a_filtered,
            'admin_v': True,
        }
        return HttpResponse(template.render(context, request))
    

    @staticmethod
    def ajout_guichet_ajout(request):
        x = request.POST['input_nom']
        a = request.POST['input_guichet']
        gui = Guichet(nom=x, alpha=a)
        gui.save()
        
        template = loader.get_template('base.html')
        guichet = Guichet.objects.all().values()
        pers = Personne.objects.all().values()
        context = {
            'g': guichet,
            'p': pers,
            'admin_v': True,
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

            vraie_guichet.nb_personne -= 1
            if vraie_guichet.nb_personne <= 0 :
                vraie_guichet.nb_now = 0
                
            vraie_guichet.save()
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
            'admin_v': True,
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
            'admin_v': True,
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
                'admin_v': True,
            }
        else:
            guichet = Guichet.objects.all().values()
            pers = Personne.objects.all().values()
            context = {
                'g': guichet,
                'p': pers,
                'admin_v': True,
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
            'admin_v': True,
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
            'admin_v': True,
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
                'admin_v': True,
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
        guichet = Guichet.objects.all().values()
        context = {
            'p': mymember,
            'g': guichet,
            'admin_v': True,
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
            'admin_v': True,
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
            'p_load': p_if,
            'counter': range(len(pers)),
        }
        return HttpResponse(template.render(context, request))

    @staticmethod
    def export(request):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Personnes"

        ws.append(["Nom", "Guichet", "Numéro", "Date et Temps", "Statut"])

        personnes = Personne.objects.all()

        for personne in personnes:
            ws.append([personne.nom, personne.guichet, personne.numero, personne.date_temps, personne.statut])

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=mi-lahatra.xlsx'

        wb.save(response)
        print("exportation fini_2")

        return response