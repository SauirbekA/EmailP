from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

class MyView(View):
    def get(self, request):
        context = {
            'title': 'Mainpage',
        }
        return render(request, 'main/mainpage.html', context=context)
def main(request):
    context = {
        'title': 'Mainpage',
    }
    return render(request, 'main/mainpage.html', context=context)

def emailsend(request):
    context = {
        'title': 'EmailSender',
    }
    return render(request, 'main/emailpage.html', context=context)
