from django.shortcuts import render,redirect
from .models import Portfolio, Skill, About
from django.urls import reverse
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings

def home(request):
  if request.method == 'POST':
    fname = request.POST.get('firstname')
    lname = request.POST.get('lastname')
    email = request.POST.get('email')
    message = request.POST.get('message')
    phone = request.POST.get('phone')

    subject = "Thanks for contacting me"
    body = f"Hello {fname} {lname},\n\nThank you for reaching out to me, your message has been received successfully, we will get back to you in due time\n\nWarm Regards,\n\nOlajire Stephen\n"

    mail = EmailMessage(subject= subject, body=body, from_email=settings.EMAIL_HOST_USER , to = [email])
    mail.send()
    
    subject = "New message Alert"
    body = f"A new message was received from {fname} {lname} {phone}, with the message of '{message}', and a mail has been automatically sent to their eamil, which is {email} Please attend to it"
    
    mail = EmailMessage(subject= subject, body=body, from_email=settings.EMAIL_HOST_USER , to = [settings.EMAIL_HOST_USER])
    mail.send()
    messages.info(request, "Your message was sent successfully")
    return redirect(reverse('home'))

  portfolios = Portfolio.objects.all()
  skills = Skill.objects.all()
  abouts = About.objects.all()
  context = {
    'portfolio': portfolios,
    'skill':skills,
    'about':abouts
    }


  return render(request, 'html/index.html', context)