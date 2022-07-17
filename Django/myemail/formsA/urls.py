from django.urls import path
from formsA.views import EmailView

urlpatterns = [
    path('contact/', EmailView, name="index" )
]