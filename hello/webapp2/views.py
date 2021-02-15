from django.shortcuts import render

# Create your views here.


def webapp2_demo_view(request):
    return render(request, 'demo.html')
