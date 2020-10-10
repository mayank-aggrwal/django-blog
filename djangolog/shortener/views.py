from django.shortcuts import render

# Create your views here.
def shorten_url(request):
    user = 'Anonymous'
    user = request.user
    return render(request, 'shortener/shortener_base.html', {'user': user})