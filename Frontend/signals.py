from django.conf import settings
import threading
from django.core.mail import EmailMessage
from django.db import models 
from django.db.models.signals import post_save, pre_save
from .models import *
from django.dispatch import receiver
from django.contrib.auth import get_user_model



class EmailThread(threading.Thread):
    def __init__(self, mes):
        self.mes = mes
        threading.Thread.__init__(self)
        
    def run(self):
        self.mes.send()
        
from django.template.loader import render_to_string


@receiver(post_save, sender=Contact)
def send_emails(sender, instance, created, *args, **kwargs):
    if created:
        
        email_template_name = "frontend/contact.txt"
        c = {
        "subject": instance.subject,
        "email": settings.EMAIL_HOST_USER,
        "new_message": instance.email,
        "content": instance.content,
        'site_name': 'PortFolio',
        'protocol': 'https',
        "domain": "https://solution-pfbp.onrender.com/",
        }
        myrender = render_to_string(email_template_name, c)
            
        mes = EmailMessage(instance.subject, myrender, instance.email, [settings.EMAIL_HOST_USER])
        
        mes.content_subtype = "html"
        
        EmailThread(mes).start()
        


        
        
