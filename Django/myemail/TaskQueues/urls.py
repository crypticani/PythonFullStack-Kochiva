from django.urls import path
from TaskQueues.views import EmailView


urlpatterns = [
    path('contact/', EmailView, name="index" )
]
