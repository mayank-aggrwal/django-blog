from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail

def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html')

def homepage(request):
    # return HttpResponse('homepage')
    return render(request, 'home.html')

def sendAcknowledgementEmail(name, email):
    subject = 'Djangolog message received'
    message_body = 'Thankyou for contacting me!\n\nI will reach out to you as soon as possible\n\nThanks and regards\nMayank Aggarwal'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message_body, email_from, recipient_list)

def contact(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        subject = "Djangolog User Contact"
        message_body = 'Someone is trying to connect with you\n\nName: ' + name + '\nEmail: ' + email + '\nMessage:\n' + message + '\n\nYours sincerely\nDjangolog'

        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['mayankaggarwal018@gmail.com']
        # Email with the details
        send_mail(subject, message_body, email_from, recipient_list)
        sendAcknowledgementEmail(name, email)
        return redirect('articles:list')
    else:
        return render(request, 'contact.html')