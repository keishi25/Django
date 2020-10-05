from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. Yo\lu're at the polls index")
