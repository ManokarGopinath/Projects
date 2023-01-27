from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.index, name='index'),
    path('paraphrasetool/', views.grammerform, name='grammerform'),
    path('paraphrase/', views.paraform, name='paraform'),
    path('grammarchecker/', views.spellform, name='spellform'),
    path('grammar/', views.filespellform, name='filespellform')
]