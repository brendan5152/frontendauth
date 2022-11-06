# Serialize converts basic Django structures,object,etc. from python to JSON so frontend can understand it

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Profile, Organisation, OrganisationProfile, Party, Category


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'email', 'groups']

class RegisterUserSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        # Create a new user, password is hashed by default  
        user = User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'email', 'password']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class OrganisationReadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organisation
        depth = 1
        fields = '__all__'

class OrganisationWriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organisation
        fields = ['name', 'description', 'kvk', 'user']

class ProfileReadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        depth = 1
        fields = '__all__'

class ProfileWriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'gender', 'age', 'phone_number', 'role']

class OrganisationProfileReadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrganisationProfile
        fields = '__all__'

class OrganisationProfileWriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrganisationProfile
        fields = ['bio', 'street_address', 'city', 'postal_code', 'country', 'phone_number', 'email', 'website', 'twitter', 'facebook', 'instagram']

class PartyReadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Party
        depth = 2
        fields = [
            'slug',
            'name', 
            'description', 
            'date', 
            'location', 
            'owner', 
            'members',
            ]

class PartyWriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Party
        fields = [
            'slug',
            'name', 
            'description', 
            'date', 
            'location', 
            'owner', 
            'members',
            ]

class CategoryReadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        party = PartyReadSerializer(many=True)
        model = Category
        depth = 1
        fields = [
            'name', 
            'slug', 
            'ordinal', 
            'party'
            ]

class CategoryWriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name', 
            'ordinal', 
            'party'
            ]

    
