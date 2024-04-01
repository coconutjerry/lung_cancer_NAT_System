from urllib import request

from django.shortcuts import render, HttpResponse

# Create your views here.
def adminsys(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def tables(request):
    return render(request,"tables.html")

def register(request):
    return render(request,"register.html")

def charts(request):
    return render(request,"charts.html")

def cards(request):
    return render(request,"cards.html")

def sys404(request):
    return render(request,"404.html")

def blank(request):
    return render(request,"blank.html")

def forgot_password(request):
    return render(request,"forgot-password.html")

def modify_password(request):
    return render(request,"modify-password.html")

def account_Information(request):
    return HttpResponse("账户信息页")

def buttons(request):
    return render(request,"buttons.html")

def utilities_color(request):
    return render(request, "avilable/utilities-color.html")

def utilities_border(request):
    return render(request, "avilable/utilities-border.html")

def utilities_animation(request):
    return render(request, "avilable/utilities-animation.html")

def utilities_other(request):
    return render(request, "avilable/utilities-other.html")