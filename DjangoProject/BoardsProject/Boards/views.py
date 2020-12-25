from django.http import HttpResponse


def home(request):
    return HttpResponse('here we can start our project')
