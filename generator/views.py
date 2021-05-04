from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')


def password(request):
    generated_password = ''
    pass_dic = list('abcdefghijklmnopqrstuvwxyz')
    u_case_dic = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    number_dic = list('0123456789')
    special_dic = list('!@#$%^&*()')
    length = int(request.GET.get('length', 10))
    if request.GET.get('uppercase'):
        pass_dic.extend(u_case_dic)
    if request.GET.get('number'):
        pass_dic.extend(number_dic)
    if request.GET.get('special'):
        pass_dic.extend(special_dic)
    for i in range(length):
        generated_password += random.choice(pass_dic)
    return render(request, 'generator/password.html', {'generated_password': generated_password})
