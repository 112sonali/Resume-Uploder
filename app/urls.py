from django.urls import path
from .views import *


urlpatterns = [
    path('resume/',ProfileView.as_view(), name='resume'),
    path('list/', ProfileView.as_view(), name='list'),
    path('all/', ProfileView.as_view(), name='all'),
    # path('resume/<int:pk>/', views.ProfileView.as_view(), name='resume-update'),
    # path('resume/', views.ProfileListView.as_view(), name='resume-list-create'),
    path('resume/<int:pk>/',ProfileDetailView.as_view(), name='resume-detail-update-delete'),


]

