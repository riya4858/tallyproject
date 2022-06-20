from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('company',views.company,name='company'),
    path('index1',views.index1,name='index1'),
    path('createcompany',views.createcompany,name='createcompany'),
    path('companycreate',views.companycreate,name='companycreate'),
    path('group',views.group,name='group'),
    path('ledger',views.ledger,name='ledger'),
    path('costcentre',views.costcentre,name='costcentre'),
    path('currency',views.currency,name='currency'),
]
