from . import views
from django.urls import path
app_name='mapp'
urlpatterns = [

    path('',views.index,name='index'),

    path('movie/<int:movie_id>/',views.details,name='details'),
    path('add/',views.addmovie,name='addmovie'),
    path('edit/<int:id>/',views.edit,name='edit'),
     path('delete/<int:id>/',views.delete,name='delete')
]
