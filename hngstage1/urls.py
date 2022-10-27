from django.contrib import admin
from django.urls import path
from biodata import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/biodata', views.ProfileList.as_view)
]
