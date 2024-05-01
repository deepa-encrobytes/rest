from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('virtual/', views.virtual, name='virtual'),
    path('profile/', views.profile, name='profile'),
    path('bill/', views.bill, name='bill'),
    path('table/', views.table, name='table'),
    path('rtl/', views.rtl, name='rtl'),
]
