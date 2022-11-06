from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from bussin.serializers import UserSerializer, GroupSerializer, ProfileSerializer, OrganisationSerializer, OrganisationProfileSerializer, PartySerializer, CategorySerializer
from bussin.models import Profile, Organisation, OrganisationProfile, Party, Category
from django_filters.rest_framework import DjangoFilterBackend

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed, created, edited, etc.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed, created, edited, etc.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrganisationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows organisations to be viewed, created, edited, etc.
    """
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows profiles to be viewed, created, edited, etc.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class OrganisationProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows organisation profiles to be viewed, created, edited, etc.
    """
    queryset = OrganisationProfile.objects.all()
    serializer_class = OrganisationProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PartyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows parties to be viewed, created, edited, etc.
    """
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    filterset_fields = ['slug']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed, created, edited, etc.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slug']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
