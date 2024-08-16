from django.urls import path
from .views import Application

app = Application()

urlpatterns = [
    path('', app.attente),

    path('base', app.base),

    path('ajouter_personne', app.ajout_pers),
    path('ajouter_guichet', app.ajout_guichet),
    path('ajouter_guichet/ajouter', app.ajout_guichet_ajout),

    path('suppr_personne/<int:id>', app.suppr_personne),
    path('suppr_guichet/<int:id>', app.suppr_guichet),

    path('modif_guichet/<int:id>', app.modif_guichet),
    path('modif_guichet/modification/<int:id>', app.modif_guichet_m),

    path('modif_personne/<int:id>', app.modif_personne),
    path('modif_personne/modification/<int:id>', app.modif_personne_m),

    path('attente', app.attente_main),
]