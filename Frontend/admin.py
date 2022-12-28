from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group


admin.site.unregister(Group)

class AboutInline(admin.StackedInline):
    model = About
    extra = 0
    max_num = 1
    

class HobbyInline(admin.StackedInline):
    model = Hobbies
    extra = 0
    

class SkillInline(admin.StackedInline):
    model = Skills
    extra = 0
    

class ProjectInline(admin.StackedInline):
    model = Project
    extra = 0
    

class ProjectTypeInline(admin.StackedInline):
    model = ProjectCover
    extra = 0
    max_num = 1
    

class ServiceInline(admin.StackedInline):
    model = MyServices
    extra = 0


class ServicesInline(admin.StackedInline):
    model = Service
    extra = 0
    max_num = 1
    

class CoverHeader(admin.StackedInline):
    model = CoverHeader
    extra = 0
    

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number']
    inlines = [CoverHeader, AboutInline, SkillInline, HobbyInline, ServiceInline, ServicesInline, ProjectTypeInline, ProjectInline]
    exclude = ['user']
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'date_updated']
    