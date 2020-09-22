from django.http import HttpResponse

def about(request):
    return HttpResponse('about')

def homepage(request):
    return HttpResponse('homepage')