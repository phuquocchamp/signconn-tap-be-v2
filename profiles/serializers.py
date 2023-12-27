from rest_framework import serializers

from profiles.models import Contact, Profiles


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'link']


class ProfilesSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True, read_only=True)

    class Meta:
        model = Profiles
        fields = ['id', 'name', 'slogan', 'img', 'contacts']
