from django.urls import path
from.views import *

urlpatterns = [
    path("",profile_view.as_view()),
]
