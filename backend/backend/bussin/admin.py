from django.contrib import admin

from bussin.models import Role, Profile, Party, Organisation, OrganisationProfile, Category

@admin.register(Role)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Party)
class GradeAdmin(admin.ModelAdmin):
    pass

@admin.register(Organisation)
class GradeAdmin(admin.ModelAdmin):
    pass

@admin.register(OrganisationProfile)
class GradeAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class GradeAdmin(admin.ModelAdmin):
    pass