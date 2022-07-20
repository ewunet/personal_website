from django.urls import path
from . import views

urlpatterns = [
	path('', views.home) # when a url is called, we will render a specific template (function) from views
]