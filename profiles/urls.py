from django.urls import path

from profiles.views import *

urlpatterns = [
    # path('profile/', ProfileView.as_view(), name='profile'),
    path('list/<int:id>', ListProfile.as_view(), name='list_profile'),
    path('create/', CreateProfile.as_view(), name='create_profile'),
    path('delete/<int:id>/', DeleteProfile.as_view(), name='delete_profile'),
    path('edit/<int:id>', EditProfile.as_view(), name='edit_profile'),
]