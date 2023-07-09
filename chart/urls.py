
from django.urls import path
from . import views
urlpatterns = [
  
    path('',views.index,name='index'),
    path('display_plot',views.display_plot,name='display_plot'),
]