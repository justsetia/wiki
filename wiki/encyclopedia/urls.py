
from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:title>', views.title, name='title'),
    path('search/', views.search, name='search'),
    path('create/', views.create, name='create'),
    path('delete/<str:title>', views.delete, name='delete'),
    path('random/', views.chance, name='random'),
    path('smart_search/<str:char>', views.smart_search, name='smart_search'),
    path('edit/<str:title>', views.edit, name='edit')
]
