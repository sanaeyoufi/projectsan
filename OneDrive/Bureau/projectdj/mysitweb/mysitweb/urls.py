
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('JuliaShop/', views.JuliaShop_view),
    path('aa/', views.aa_view),
    path('bb/', views.bb_view),
    path('cc/', views.cc_view),
    path('ss/', views.ss_view),
]
