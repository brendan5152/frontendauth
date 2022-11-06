from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from bussin.serializers import UserSerializer, GroupSerializer, ProfileReadSerializer, ProfileWriteSerializer,OrganisationReadSerializer, OrganisationWriteSerializer, OrganisationProfileReadSerializer, OrganisationProfileWriteSerializer, PartyReadSerializer, PartyWriteSerializer, CategoryReadSerializer, CategoryWriteSerializer,RegisterUserSerializer
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
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'POST':
            return OrganisationWriteSerializer
        else:
            return OrganisationReadSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows profiles to be viewed, created, edited, etc.
    """
    queryset = Profile.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'POST':
            return ProfileWriteSerializer
        else:
            return ProfileReadSerializer

class OrganisationProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows organisation profiles to be viewed, created, edited, etc.
    """
    queryset = OrganisationProfile.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'POST':
            return OrganisationProfileWriteSerializer
        else:
            return OrganisationProfileReadSerializer


class PartyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows parties to be viewed, created, edited, etc.
    """
    queryset = Party.objects.all()
    filterset_fields = ['slug']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'POST':
            return PartyWriteSerializer
        else:
            return PartyReadSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed, created, edited, etc.
    """
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slug']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'POST':
            return CategoryWriteSerializer
        else:
            return CategoryReadSerializer

class UserAPIView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class RegisterUserAPIView(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterUserSerializer