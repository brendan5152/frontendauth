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
  PARTY_LEVEL_PROMOTER = 4
  PARTY_LEVEL_MANAGER = 5
  PARTY_LEVEL_ACCOUNTANT = 6
  ROLE_CHOICES = (
      (PARTY_LEVEL_ONE, 'Party Person'),
      (PARTY_LEVEL_TWO, 'Raver'),
      (PARTY_LEVEL_THREE, 'Pro Raver'),
      (PARTY_LEVEL_PROMOTER, 'Promoter'),
      (PARTY_LEVEL_ACCOUNTANT, 'Accountant'),
  )

  id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

  def __str__(self):
      return f"{self.id}" 


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    age = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    roles = models.ManyToManyField(Role)

    def __str__(self):
        return f"{self.user}, {self.bio}, {self.gender}, {self.age}, {self.phone_number}, {self.roles.all()}" 


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
        return f"{self.slug}, {self.name}, {self.description}, {self.date}, {self.location}, {self.owner}, {self.members}"

class Organisation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    kvk = models.IntegerField()
    valid = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name}, {self.description}, {self.kvk}, {self.valid}, {self.user}"

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
        return f"{self.name}, {self.slug}, {self.ordinal}, {self.party}"
