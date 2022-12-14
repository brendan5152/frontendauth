# Serialize converts basic Django structures,object,etc. from python to JSON so frontend can understand it

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Profile, Organisation, OrganisationProfile, Party, Category


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class OrganisationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organisation
        depth = 1
        fields = '__all__'

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        depth = 1
        fields = '__all__'

class OrganisationProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrganisationProfile
        fields = '__all__'

class PartySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Party
        depth = 2
        fields = '__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        depth = 1
        fields = '__all__'

    
