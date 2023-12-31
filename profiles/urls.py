from django.urls import path

from profiles import views
from profiles.views import *

urlpatterns = [
    path('<str:name>/', views.get_name, name='get_name'),
    # path('create/', views.create_profile, name='create_profile'),
    path('create/', CreateProfileView.as_view(), name='create_profile'),

    path('list/<int:id>', ListProfile.as_view(), name='list_profile'),
    path('delete/<int:id>/', views.delete_profile, name='delete_profile'),
    path('edit/<int:id>', EditProfile.as_view(), name='edit_profile'),
]