from rest_framework import generics, status, authentication, permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from profiles.models import Profiles, Contacts
from profiles.serializers import ProfilesSerializer, ContactSerializer


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_profile(request):
    if request.method == 'POST':
        profile_data = request.data
        contacts_data = profile_data.pop('contacts')
        contacts_serializer = ContactSerializer(data=contacts_data, many=True)
        if contacts_serializer.is_valid():
            Response(contacts_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("Contacts data invalid", status=status.HTTP_400_BAD_REQUEST)


class CreateProfileView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ProfilesSerializer(data=request.data)
        if serializer.is_valid():
            # Tạo profile
            profile = serializer.save()

            # Tạo các contacts liên quan
            contacts_data = serializer.validated_data.get('contacts', [])
            for contact_data in contacts_data:
                Contacts.objects.create(
                    profile=profile,
                    name=contact_data['name'],
                    link=contact_data['link']
                )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_name(request, name):
    profiles = Profiles.objects.filter(name=name)
    if not profiles.exists():
        return Response({'message': 'No found profile.'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProfilesSerializer(profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ListProfile(generics.RetrieveAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
    lookup_field = "id"
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class DeleteProfile(generics.DestroyAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
    lookup_field = "id"
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_profile(request, id):
    try:
        profile = Profiles.objects.get(id=id)
    except Profiles.DoesNotExist:
        return Response({'message': 'No found profile.'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        profile.delete()
        return Response({'detail': 'Profile deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


class EditProfile(generics.UpdateAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
    lookup_field = "id"
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
