from django.urls import path

from Admin1 import views

urlpatterns = [
    path('adminlogin',views.admin_login,name="adminlogin"),
    path('adminhome',views.login_fun,name="adminhome")
]