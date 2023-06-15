from . import views
from django.urls import path
app_name='movieapp'

urlpatterns = [
    path('',views.index,name='intex'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.add_movie,name='add'),
    path('update/<int:id>/',views.edit_movie,name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),

]
