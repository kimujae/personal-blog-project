from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_world(request):
    #return HttpResponse('안녕하세요!') # 리스폰스를 직접 만들어서 반환
    return render(request, 'base.html')