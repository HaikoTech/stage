from django.urls import path
from .views import Application

app = Application()

urlpatterns = [
    path('', app.attente),

    path('base', app.base_log),
    path('base_view/<str:admin>', app.base),
    path('base_verified', app.base_v),
    path('base_change', app.base_c),
    path('base_change_v', app.base_c_v),

    path('ajouter_personne', app.ajout_pers),
    path('main', app.main),
    path('ajouter_guichet', app.ajout_guichet),
    path('ajouter_guichet/ajouter', app.ajout_guichet_ajout),

    path('suppr_personne/<str:page>/<int:fini>/<int:id_guich>', app.suppr_personne),
    path('suppr_personne_page/<str:page>/', app.suppr_personne_page),
    path('suppr_personne_base/<str:page>/<int:id>', app.suppr_personne_base),
    path('suppr_guichet/<int:id>', app.suppr_guichet),

    path('modif_guichet/<int:id>', app.modif_guichet),
    path('modif_guichet/modification/<int:id>', app.modif_guichet_m),

    path('modif_personne/<int:id>', app.modif_personne),
    path('modif_personne/modification/<int:id>', app.modif_personne_m),

    path('test', app.test),

    path('change_day/<str:page>', app.change_day),

    path('guichet', app.guichet),
    path('guichet/<int:id>', app.guichet_id),

    path('export/', app.export),

    # 

    path('api/personnes/', app.get_all_data, name='get_personne_data'),
    path('api/date/', app.get_date_data, name='get_date_data'),
    path('api/guichet/', app.get_guichet, name='get_guichet'),
    path('api/personne/', app.get_personne, name='get_personne'),
    path('api/admin/', app.get_admin, name='get_admin'),


]