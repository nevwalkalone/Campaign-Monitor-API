from django.urls import path
from . import views


urlpatterns = [ 
    path('form', views.subscribers_form, name="insert_subscriber"),
    path('', views.subscribers_list, name="subscribers_list"),
    path('delete/<str:email>/', views.subscribers_delete, name='delete_subscriber'),
]
