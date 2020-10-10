from django.urls import path

from . import views


app_name = 'adopt'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pet_id>', views.detail, name='details'),
    path('request/', views.adopt_request, name='request'),
]
