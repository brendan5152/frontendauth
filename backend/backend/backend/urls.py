from django.urls import path, include
from rest_framework import routers
from bussin import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'organisations', views.OrganisationViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'organisationprofiles', views.OrganisationProfileViewSet)
router.register(r'parties', views.PartyViewSet)
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
