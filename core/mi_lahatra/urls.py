from django.urls import path
from .views import Application

app = Application()

urlpatterns = [
    path('', app.attente),
]