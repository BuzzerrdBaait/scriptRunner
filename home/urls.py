from django.conf.urls.static import static
from django.urls import path
from . import views

app_name='home'

urlpatterns=[

    path('',views.home, name='homePage')

]
