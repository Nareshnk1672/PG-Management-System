from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

from Guest.forms import RoomForm
from Guest.models import Register, FillDetails, Floor, Room, Complaints


def guest_reg(request):
    return render(request,'guestreg.html')
def guestlog(request):
    return render(request,'guestlogin.html')
# def guestreg1(request):
#     return render(request,'register.html')

def read_fun(request):
    if request.method == "POST":
        name = request.POST['txtname']
        mobile = request.POST['txtnum']
        email = request.POST['txtmail']
        password = request.POST['txtpswd']
        data = {"name":name,"mobile":mobile,"email":email,"password":password}
        if Register.objects.filter(Q(Name=name) | Q(Email=email)).exists():
            data = {"msg": True}
            return render(request, 'register.html', data)
        else:
            u1 = Register(Name=name, Password=password,Mobile=mobile, Email=email)
            u1.save()
            return redirect('guestlog')
    return render(request, 'register.html', {'msg': False})



def login_fun(request):
    if request.method == "POST":
        name = request.POST['username']
        password = request.POST['password']
        if Register.objects.filter(Q(Name=name) & Q(Password=password)):
                return render(request,'guesthome1.html')
        else:
            data = {"msg": True}
            return render(request, 'guestlogin.html', data)
    else:
        return render(request, 'guestlogin.html', {'msg': False})


def menu(request):
    return render(request, 'menu.html')


def fill_details(request):
    if request.method == 'POST':
        s1 = FillDetails()
        s1.Name=request.POST['txtName']
        s1.Photo=request.POST['photo']
        s1.Father_Name=request.POST['txtFName']
        s1.Age=int(request.POST['txtAge'])
        s1.Dob=request.POST['date_of_birth']
        s1.Address=request.POST['txtAddress']
        s1.Aadhar=int(request.POST['txtAadhar'])
        s1.Doj=request.POST['date_of_joining']
        s1.Education=request.POST['txtEducation']
        s1.Profession=request.POST['txtProfession']
        s1.Office_Address=request.POST['txtOffice']
        s1.Phone_no=int(request.POST['txtPhone'])
        s1.Monthly_Rent=int(request.POST['txtRent'])
        s1.Deposit=int(request.POST['txtDeposit'])
        s1.Maintain_Charge=int(request.POST['txtCharge'])
        s1.save()
        redirect_url = request.POST.get('redirect_url', '/')
        return redirect('fill_details')
    else:
        return render(request, 'fill_details.html')

def complaints(request):

    if request.method == 'POST':
        c1 = Complaints()
        user_name = FillDetails.objects.get(pk=request.POST['ddlUser'])  # Assuming ddlUser is the dropdown for user selection
        user_room = Room.objects.get(pk=request.POST['ddlRoom'])
        c1.user_name = user_name
        c1.user_room = user_room
        c1.complaint_date = request.POST['date_of_complaint']
        c1.save()
        return redirect('complaints')

    else:
        floor_data = Floor.objects.all()
        room_data = Room.objects.all()
        user_data = FillDetails.objects.all()
        return render(request, 'complaints.html',
                      {'floordata': floor_data, 'roomdata': room_data, 'userdata': user_data})


def check_vacancy(request):
    return render(request, 'check_vacancy.html')