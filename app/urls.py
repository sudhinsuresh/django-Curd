from app import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name="about"),
    path('insert',views.insertDate,name="insertData"),
    path('update/<id>',views.updateData,name="updateData"),
    path('delete/<id>',views.deleteData,name="deleteData")
]
