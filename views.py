from django.http import HttpResponse
from djangoshortcuts import redirect

def index(request):
    return HttpResponse('index')

def login(request):
    return redirect('/index')
