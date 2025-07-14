from django.shortcuts import render, get_object_or_404
from decouple import config
from .models import *
# Create your views here.

from django.http import HttpResponse
from django.conf import settings

def test_debug(request):
    return HttpResponse(f"DEBUG is {settings.DEBUG}")


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.core.mail import send_mail, BadHeaderError
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt  # If no CSRF token in AJAX (can be removed if you send token)
def send_message_ajax(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get('name', '').strip()
            email = data.get('email', '').strip()
            message = data.get('message', '').strip()

            errors = {}

            if not name:
                errors['name'] = 'Name is required.'
            if not email:
                errors['email'] = 'Email is required.'
            elif '@' not in email:
                errors['email'] = 'Enter a valid email.'
            if not message:
                errors['message'] = 'Message cannot be empty.'

            if errors:
                return JsonResponse({'success': False, 'errors': errors}, status=400)

            subject = f"New Contact Message from {name}"
            full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            recipient_list = [config('EMAIL_HOST_USER')]  # Sends mail to you

            try:
                send_mail(subject, full_message, config('DEFAULT_FROM_EMAIL'), recipient_list)
            except BadHeaderError:
                return JsonResponse({'success': False, 'errors': {'header': 'Invalid header found.'}}, status=500)

            return JsonResponse({'success': True, 'message': 'Thank you for contacting me!'})
        except Exception as e:
            return JsonResponse({'success': False, 'errors': {'server': str(e)}}, status=500)
    return JsonResponse({'success': False, 'errors': {'method': 'Invalid request method.'}}, status=405)


from .models import Project  # Import Project model

def homePage(request):
    projects = Project.objects.all()
    return render(request, "homePage.html", {"projects": projects})

