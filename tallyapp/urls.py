from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('basepage',views.basepage,name='basepage'),
    path('company',views.company,name='company'),
    path('createcompany',views.createcompany,name='createcompany'),
    path('company_create',views.company_create,name='company_create'),
    path('company_feature/<int:pk>',views.company_feature,name='company_feature'),
    path('tally_gst/<int:pk>',views.tally_gst,name='tally_gst'),
    path('tds/<int:pk>',views.tds,name='tds'),
    path('gst_tax/<int:pk>',views.gst_tax,name='gst_tax'),
    path('lut_bond',views.lut_bond,name='lut_bond'),
    path('create_tds/<int:pk>',views.create_tds,name='create_tds'),
    path('create_gst/<int:pk>',views.create_gst,name='create_gst'),
    path('person_tds/<int:pk>',views.person_tds,name='person_tds'),

    path('person/<int:pk>',views.person,name='person'),
    path('group/<int:pk>',views.group,name='group'),
    path('ledger/<int:pk>',views.ledger,name='ledger'),
    path('costcentre/<int:pk>',views.costcentre,name='costcentre'),
    path('costcentre2/<int:pk>',views.costcentre2,name='costcentre2'),
    path('group2/<int:pk>',views.group2,name='group2'),
    path('currency/<int:pk>',views.currency,name='currency'),
    path('creategroup/<int:pk>',views.creategroup,name='creategroup'),
    # path('features',views.features,name='features'),
    path('altercompanyview',views.altercompanyview,name='altercompanyview'),
    path('selectcompany',views.selectcompany,name='selectcompany'),
    path('shutcompany',views.shutcompany,name='shutcompany'),
    path('addstate',views.addstate,name='addstate'),
    path('addstatenew',views.addstatenew,name='addstatenew'),    path('altercompany/<int:pk>',views.altercompany,name='altercompany'),

    path('addcountry',views.addcountry,name='addcountry'),
    path('ratesofexchange/<int:pk>',views.ratesofexchange,name='ratesofexchange'),
    path('voucher/<int:pk>',views.voucher,name='voucher'),
   
    path('disable/<int:pk>',views.disable,name='disable'),
    path('enable/<int:pk>',views.enable,name='enable'),
    path('featurepage',views.featurepage,name='featurepage'),
    
]
