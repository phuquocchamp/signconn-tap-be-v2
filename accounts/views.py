from rest_framework import generics, permissions, authentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .models import Account
from profiles.models import Profiles
from .serializers import AccountSerializer, AuthTokenSerializer
from profiles.serializers import ProfilesSerializer


# Create your views here.
class CreateAccountView(generics.CreateAPIView):
    serializer_class = AccountSerializer


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageAccountView(generics.RetrieveAPIView):
    """ Manage the authenticated accounts. """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    # lookup_field = "id"
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """ Retrieve and return authenticated account """
        return self.request.data


class ManageProfileView(generics.RetrieveAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
    lookup_field = 'id'
