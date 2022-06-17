from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('company',views.company,name='company'),
    path('index1',views.index1,name='index1'),
    path('createcompany',views.createcompany,name='createcompany'),
]
