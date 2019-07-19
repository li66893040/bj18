from django.http import HttpResponse
from django.shorcuts import redirect

def views(request):
    return HttpResponse('IS-OK')

def login(request):
    return redirect('/views')
