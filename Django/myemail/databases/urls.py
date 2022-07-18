from django.urls import path
from databases.views import EmailView


urlpatterns = [
    path('contact/', EmailView, name="index" )
]
