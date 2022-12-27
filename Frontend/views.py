from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.conf import settings
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import requests
from environs import Env


env = Env()
env.read_env()


def error_500(request):
    return render(request, 'errors/500.html', status=500)


def error_404(request, exception):
    return render(request, 'errors/404.html', status=404)

# Create your views here.
class Home(TemplateView):
    template_name = "frontend/home.html"
    
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.filter(date_created__lte=timezone.now()).first()
        
        url = ('https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=') + env.str('apikey')
        response = requests.get(url)
        context['news'] = response.json()['articles'][:3]
        
        return context
    
@csrf_protect
def contact(request):
    if request.method == "POST":
        name = request.POST.get('names')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        contact = Contact(name=name, email=email, subject=subject, content=message)
        contact.save()
        
        return JsonResponse({'status': True, 'msg': f"Hello {name}, your information has been submitted successfully"})
    else:
        return JsonResponse({'status': False, 'msg': f"your information not submitted successfully "})
    
    
import requests
