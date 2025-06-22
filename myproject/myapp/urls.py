from django.urls import path
from . import views

app_name = 'myapp'  # required for namespacing
urlpatterns = [
    path('', views.home_view, name='home'),
]