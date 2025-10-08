from django.urls import path
from . import views

app_name = 'gestionapp' # Namespace pour �viter les conflits de noms d'URL

urlpatterns = [
    # Page d'accueil de l'application : liste des adh�rents
    path('', views.adherent_list, name='adherent_list'),

    # Page de d�tail d'un adh�rent
    path('adherent/<int:pk>/', views.adherent_detail, name='adherent_detail'),

    # Page pour ajouter un nouvel adh�rent
    path('adherent/ajouter/', views.adherent_create, name='adherent_create'),

    # Page pour modifier un adh�rent
    path('adherent/<int:pk>/modifier/', views.adherent_update, name='adherent_update'),
]