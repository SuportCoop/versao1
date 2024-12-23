from django.http import HttpResponse

def cars_view(resquest):
    return HttpResponse('cars/html')