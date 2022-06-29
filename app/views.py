from django.shortcuts import render

# Create your views here.
def bootstrap_down(request):
    return render(request,'bootstrap_down.html')

def cdn(request):
    return render(request,'cdn.html')