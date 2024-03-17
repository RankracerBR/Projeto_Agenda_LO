from django.urls import path
from contact import views

app_name = 'contact' # Evita duplicação de nomes no name=''

urlpatterns = [
    path('', views.index, name='index'),
]
