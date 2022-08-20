from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('users/', views.users, name="users"),
    path('admin/', admin.site.urls),
    path('json/', views.platenum_json, name='platenum_json')

    # CREATE

    # READ

    # UPDATE (EDIT)
    
    # DELETE
]
