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
    path('companycreated',views.companycreated,name='companycreated'),
    path('create_group',views.create_group,name='create_group'),
    path('features',views.features,name='features'),
    path('altercompanyview',views.altercompanyview,name='altercompanyview'),
    path('selectcompany',views.selectcompany,name='selectcompany'),
    path('altercompany/<int:pk>',views.altercompany,name='altercompany'),
]
