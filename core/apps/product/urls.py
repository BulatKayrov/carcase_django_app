from django.urls import path

from core.apps.product import views

app_name = 'product'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]