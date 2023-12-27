from django.urls import path

from .views import CreateAccountView, CreateTokenView, ManageProfileView

urlpatterns = [
    path('register/', CreateAccountView.as_view(), name='register'),
    path('login/', CreateTokenView.as_view(), name='login'),
    path('me/<int:id>/', ManageProfileView.as_view(), name='me'),
]