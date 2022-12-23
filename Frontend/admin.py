from django.contrib import admin
from .models import *

class AboutInline(admin.StackedInline):
    model = About
    extra = 0
    max_num = 1
    

class HobbyInline(admin.StackedInline):
    model = Hobbies
    extra = 0
    max_num = 1
    

class SkillInline(admin.StackedInline):
    model = Skills
    extra = 0
    

class ProjectInline(admin.StackedInline):
    model = Project
    extra = 0
    max_num = 1
    

class ProjectTypeInline(admin.StackedInline):
    model = ProjectType
    extra = 0
    

class ServiceInline(admin.StackedInline):
    model = MyServices
    extra = 0
    max_num = 1


class ServicesInline(admin.StackedInline):
    model = Service
    extra = 0
    max_num = 1
    

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number']
    inlines = [AboutInline, SkillInline, HobbyInline, ProjectInline, ProjectTypeInline, ServiceInline, ServicesInline]
    exclude = ['user']
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()
    
    

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'date_updated']
    exclude = ['user']
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'date_updated']
    