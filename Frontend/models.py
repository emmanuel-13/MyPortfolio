from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from PIL import Image
from ckeditor.fields import RichTextField
from django.core.mail import send_mail

def is_digit(value):
    if value.isdigit() == False:
        raise ValidationError('phone number must be in digit')


    
    
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11, validators=[is_digit])
    zip_code = models.CharField(max_length=5, validators=[is_digit])
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'My Profile'
        

class About(models.Model):
    about = RichTextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Skills(models.Model):
    skill = models.CharField(max_length=20, blank=False, null=False)
    average = models.CharField(max_length=3, validators=[is_digit])
    week_flow = models.CharField(max_length=3, validators=[is_digit])
    month_flow = models.CharField(max_length=3, validators=[is_digit])
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
        
        
    class Meta:
        verbose_name_plural = 'Skill'


class Hobbies(models.Model):
    title = models.CharField(max_length=50, null=True, blank=False)
    cover = RichTextField(help_text="enter brief summery of your hobbies")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = 'Hobbies'


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
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = 'Services'
        
class ProjectType(models.Model):
    
    project_type = models.CharField(max_length=30)
    content = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Project Type'
    
class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='upload-images/', null=False, blank=False)
    name = models.CharField(max_length=20, null=True)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.images.path)

        if img.height > 450 and img.width > 500:
            output_size = (450, 500)
            img.thumbnail(output_size)
            img.save(self.images.path)
            
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = 'Projects'
    

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='upload-images/', null=False, blank=False)
    title = models.CharField(max_length=50, blank=False, null=False)
    cover = RichTextField(help_text="blog content")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.images.path)

        if img.height > 450 and img.width > 500:
            output_size = (450, 500)
            img.thumbnail(output_size)
            img.save(self.images.path)
            
            
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = 'Blog'
    
    

import time
from django.conf import settings
import threading
from django.core.mail import EmailMessage

class EmailThread(threading.Thread):
    def __init__(self, mes):
        self.mes = mes
        threading.Thread.__init__(self)
        
    def run(self):
        self.mes.send()

class Contact(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField()
    subject = models.CharField(max_length=50, null=False, blank=False)
    content = RichTextField(help_text='please fill in your content here')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id)
    
    # def save(self, *args, **kwargs):
        
    #     # send_mail(subject=self.subject, message=self.content, from_email=self.email, recipient_list=[settings.EMAIL_HOST_USER], fail_silently=True)
    #     # time.sleep(10)
        
    #     mes = EmailMessage(subject=self.subject, body=self.content, from_email=self.email, to=[settings.EMAIL_HOST_USER])
    #     EmailThread(mes).start()
        
    #     super().save(*args, **kwargs)
    
    # class Meta:
    #     verbose_name_plural = "Contact"
        
        
    
    
    
    