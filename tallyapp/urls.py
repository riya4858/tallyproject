from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('company',views.company,name='company'),
    path('index1',views.index1,name='index1'),
    path('createcompany',views.createcompany,name='createcompany'),
    path('companycreate',views.companycreate,name='companycreate'),
    path('group/<int:pk>',views.group,name='group'),
    path('ledger/<int:pk>',views.ledger,name='ledger'),
    path('costcentre/<int:pk>',views.costcentre,name='costcentre'),
    path('currency/<int:pk>',views.currency,name='currency'),
    path('features/<int:pk>',views.features,name='features'),
    path('creategroup/<int:pk>',views.creategroup,name='creategroup'),
    # path('features',views.features,name='features'),
    path('altercompanyview',views.altercompanyview,name='altercompanyview'),
    path('selectcompany',views.selectcompany,name='selectcompany'),
    path('shutcompany',views.shutcompany,name='shutcompany'),
    path('addstate',views.addstate,name='addstate'),
    path('addcountry',views.addcountry,name='addcountry'),
    path('altercompany/<int:pk>',views.altercompany,name='altercompany'),
    path('ratesofexchange/<int:pk>',views.ratesofexchange,name='ratesofexchange'),
    path('voucher/<int:pk>',views.voucher,name='voucher'),
    path('democreate',views.democreate,name='democreate'),
    path('demo1/<int:pk>',views.demo1,name='demo1'),
    # path('demo2/<int:pk>',views.demo2,name='demo2'),
    path('featurecompany/<int:pk>',views.featurecompany,name='featurecompany'),
    path('disable/<int:pk>',views.disable,name='disable'),
    path('enable/<int:pk>',views.enable,name='enable'),
    
]
