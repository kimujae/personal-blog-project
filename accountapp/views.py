from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.
def hello_world(request):
    #return HttpResponse('안녕하세요!') # 리스폰스를 직접 만들어서 반환
    return render(request,'accountapp/helloworld.html')



class AccountCreate(CreateView):
    model = User # 모델
    form_class = UserCreationForm # 폼
    success_url = reverse_lazy('accountapp : hello_world') #계정생성 성공 시 반환 링크 / reverse를 사용하면 error가 뜸
    template_name = 'accountapp/create.html'#템플릿 지정

