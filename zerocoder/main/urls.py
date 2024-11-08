from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cats', views.our_cats, name='page_cats'),
    path('program', views.affiliate_program, name='page_prog'),
    path('community', views.community, name='page_com'),
    path('training', views.training, name='page_tr'),
]
