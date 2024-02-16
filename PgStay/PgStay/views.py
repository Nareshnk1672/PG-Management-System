from django.shortcuts import render
'''
name: raghu
email:codebug15@gmail.com
password:raghu@3109


'''

def home(request):
    return render(request,'base.html')