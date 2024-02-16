from django.urls import path

from Guest import views

urlpatterns = [
    path('guestreg',views.guest_reg,name="guestreg"),
    # path('guestreg1',views.guestreg1,name='guestreg1'),
    path('guestlog',views.guestlog,name='guestlog'),
    path('read',views.read_fun,name='read'),
    path('readlog',views.login_fun,name='readlog'),
    path('menu/', views.menu, name='menu'),
    path('fill_details/', views.fill_details, name='fill_details'),
    path('complaints',views.complaints,name='complaints'),
    path('vacancy',views.check_vacancy,name='vacancy')
]