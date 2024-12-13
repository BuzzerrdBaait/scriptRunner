from django.conf.urls.static import static
from django.urls import path
from . import views

app_name='scriptRunner'

urlpatterns=[

    path('',views.scriptRunner, name='scriptRunner')

]
