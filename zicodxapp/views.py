from django.shortcuts import render


def index(request):
     '''The home page for Zicodxapp.'''

     return render(request, 'zicodxapp/index.html')
