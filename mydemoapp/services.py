from django.http import HttpResponse

def greeting_service(request):
    return HttpResponse("Hello, world!")