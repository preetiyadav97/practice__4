from django.contrib import admin
from django.urls import path
from .views import first,update_place,Delete_place,Create_place

urlpatterns = [
    path('first/',first,name='first1'),
    path('update/<int:pk>/',update_place, name = 'update1'),
    path('delete/<int:pk>/',Delete_place, name = 'delete1'),

    path('Create/',Create_place, name = 'Create1')

]

# urlpatterns = [
#     path('about/',readTable,name='about1'),
   
#     path('update/<int:pk>/',update_place, name = 'update1'),
#     path('delete/<int:pk>/',Delete_place, name = 'delete1'),

#     path('Create/',Create_place, name = 'Create1')

   
# ]