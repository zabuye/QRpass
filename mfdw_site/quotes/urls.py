from django.urls import paths

from . import views

urlpatterns = [
    path('', views.quote_req, name='quote-request'),
]
