from rest_framework import generics, status, authentication, permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from profiles.models import Profiles
from profiles.serializers import ProfilesSerializer


# @api_view(['POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def create_profile(request):
#     if request.method == 'POST':
#         profile_data = request.data
#         contacts_data = profile_data.pop('contacts')
#         contacts_serializer = ContactSerializer(data=contacts_data, many=True)
#         if contacts_serializer.is_valid():
#             Response(contacts_serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response("Contacts data invalid", status=status.HTTP_400_BAD_REQUEST)


class CreateProfileView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    selializer_class = ProfilesSerializer
    def post(self, request, format=None):
        print("sdsfgvf")
        data = request.data
        data['user'] = request.user.id
        serializer = ProfilesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("Profile data invalid", status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
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
    permission_classes = [permissions.AllowAny]

class AllProfile(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        profiles = Profiles.objects.all()
        serializer = ProfilesSerializer(profiles, many=True)
        data = serializer.data
        responseData = []
        for i in range(len(data)):
            if data[i]['user'] == request.user.id:
                responseElement = data[i]
                responseElement.pop('user')
                responseData.append(responseElement)
        return Response(responseData, status=status.HTTP_200_OK)


class DeleteProfile(generics.DestroyAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
    lookup_field = "id"
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def delete(self, request, id, format=None):
        profile = Profiles.objects.get(id=id)
        print(profile.user.id, request.user.id)
        if request.user.id != profile.user.id:
            return Response({'message': 'You are not allowed to delete this profile.'}, status=status.HTTP_403_FORBIDDEN)
        # profile.delete()
        return Response({'detail': 'Profile deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_profile(request, id):
    try:
        profile = Profiles.objects.get(id=id)
    except Profiles.DoesNotExist:
        return Response({'message': 'No found profile.'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        if request.user.id != profile.user.id:
            return Response({'message': 'You are not allowed to delete this profile.'}, status=status.HTTP_403_FORBIDDEN)
        profile.delete()
        return Response({'detail': 'Profile deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


class EditProfile(generics.UpdateAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
    lookup_field = "id"
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def put(self, request, id, format=None):
        profile_data = request.data
        print(profile_data)
        profile = Profiles.objects.get(id=id)
        if request.user.id != profile.user.id:
            return Response({'message': 'You are not allowed to edit this profile.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = ProfilesSerializer(profile, data=profile_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("Profile data invalid", status=status.HTTP_400_BAD_REQUEST)
        