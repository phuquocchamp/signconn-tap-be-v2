from django.urls import path

from .views import CreateAccountView, CreateTokenView, ManageProfileView, GetUsernameFromToken

urlpatterns = [
    path('register/', CreateAccountView.as_view(), name='register'),
    path('login/', CreateTokenView.as_view(), name='login'),
    path('me/<int:id>/', ManageProfileView.as_view(), name='me'),
    path('name/', GetUsernameFromToken.as_view(), name='get-username'),
]