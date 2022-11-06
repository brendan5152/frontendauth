from email.errors import NoBoundaryInMultipartDefect
from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
  '''
  The Role entries are managed by the system,
  automatically created via a Django data migration.
  '''
  PARTY_LEVEL_ONE = 1
  PARTY_LEVEL_TWO = 2
  PARTY_LEVEL_THREE = 3
  PARTY_LEVEL_FOUR = 4
  ADMIN = 5
  ROLE_CHOICES = (
      (PARTY_LEVEL_ONE, 'student'),
      (PARTY_LEVEL_TWO, 'teacher'),
      (PARTY_LEVEL_THREE, 'secretary'),
      (PARTY_LEVEL_FOUR, 'supervisor'),
      (ADMIN, 'admin'),
  )

  id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

  def __str__(self):
      return self.get_id_display()


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    age = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    roles = models.ManyToManyField(Role)

    def __str__(self):
        return self.user.username


class Party(models.Model):
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    owner = models.ForeignKey('Organisation', on_delete=models.CASCADE)
    members = models.ForeignKey(User, on_delete=models.CASCADE)
    #image = models.ImageField(upload_to='party_images', blank=True)

    def __str__(self):
        return self.name

class Organisation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    kvk = models.IntegerField()
    valid = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class OrganisationProfile(models.Model):
    organisation = models.OneToOneField('Organisation', on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    street_address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    ordinal = models.IntegerField()
    party = models.ForeignKey('Party', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
