from rest_framework import serializers
from profiles.models import Contacts, Profiles


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['name', 'link']


class ProfilesSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(required=False, many=True)

    class Meta:
        model = Profiles
        fields = ['id', 'name', 'slogan', 'img', 'contacts']

    # def create(self, validated_data):
    #     contacts_data = validated_data.pop('contacts')
    #     profile = Profiles.objects.create(**validated_data)
    #     Contacts.objects.create(profile=profile, **contacts_data)
    #     return profile


