from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from PIL import Image
from ckeditor.fields import RichTextField
import os


def is_digit(value):
    if not value.isdigit():
        raise ValidationError('Phone number must contain only digits')


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile-image/', null=True, blank=True)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11, validators=[is_digit])
    zip_code = models.CharField(max_length=5, validators=[is_digit])
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'My Profile'

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            image_path = self.image.path
            img = Image.open(image_path)

            # Resize only if larger than 1080p
            max_size = (1080, 1080)
            img.thumbnail(max_size, Image.Resampling.LANCZOS)

            # Convert to RGB if not already (avoids issues with PNG or alpha)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            # Save optimized with good quality
            img.save(image_path, optimize=True, quality=90)
    

class Hobbies(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    hobby = models.CharField(max_length=20, null=False, blank=False, default="")
    
    def __str__(self):
        return self.hobby
    
    class Meta:
        verbose_name_plural = "Profile Hobby"
    
        

class About(models.Model):
    about = RichTextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.about

class Skills(models.Model):
    skill = models.CharField(max_length=20, blank=False, null=False)
    average = models.CharField(max_length=3, validators=[is_digit])
    week_flow = models.CharField(max_length=3, validators=[is_digit])
    month_flow = models.CharField(max_length=3, validators=[is_digit])
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.skill
    
        
    class Meta:
        verbose_name_plural = 'Skill'


# class Hobbies(models.Model):
#     title = models.CharField(max_length=50, null=True, blank=False)
#     cover = RichTextField(help_text="enter brief summery of your hobbies")
#     icon = models.CharField(max_length=20, null=True)
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return self.user.username
    
#     class Meta:
#         verbose_name_plural = 'Hobbies'


class Service(models.Model):
    content = models.TextField()
    service = models.CharField(max_length=20, blank=False, null=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Service'

class MyServices(models.Model):
    title = models.CharField(max_length=50, null=True, blank=False)
    cover = RichTextField()
    icon = models.CharField(max_length=50, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.profile.user.username
    
    class Meta:
        verbose_name_plural = 'Services'
        
class ProjectCover(models.Model):
    
    title = models.CharField(max_length=30)
    content = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Project Type'
    
class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='upload-images/', null=False, blank=False)
    name = models.CharField(max_length=20, null=True)
    content = models.TextField()
    url = models.URLField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 450 and img.width > 500:
            output_size = (450, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
    
    def __str__(self):
        return self.profile.user.username
    
    class Meta:
        verbose_name_plural = 'Projects'
    

# class Blog(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     images = models.ImageField(upload_to='upload-images/', null=False, blank=False)
#     title = models.CharField(max_length=50, blank=False, null=False)
#     cover = RichTextField(help_text="blog content")
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
    
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)

#         img = Image.open(self.images.path)

#         if img.height > 450 and img.width > 500:
#             output_size = (450, 500)
#             img.thumbnail(output_size)
#             img.save(self.images.path)
            
            
#     def __str__(self):
#         return self.user.username
    
#     class Meta:
#         verbose_name_plural = 'Blog'
    
    


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)
        
        
    
    
    
    
