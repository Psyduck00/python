from django.urls import path, include
from .views import home

urlpatterns = [
#path('get-polls','',name='polls')
    path('home=page',home,name='home-page')
]

#domain-name/polls/get-polls

