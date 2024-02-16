from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def admin_login(request):
    return render(request,'adminhome.html')


def login_fun(request):
    if request.method == "POST":
        name = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=name, password=password)
        if user is not None:
            if user.is_superuser:
                return render(request,'adminhome1.html')
            else:
                data = {"msg": True}
                return render(request, 'adminhome.html', data)
        else:
            data = {"msg": True}
            return render(request, 'adminhome.html', data)
    else:
        return render(request, 'login.html', {'msg': False})