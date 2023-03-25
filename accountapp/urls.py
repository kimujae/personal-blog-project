from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from accountapp.views import hello_world, AccountCreate

app_name = "accountapp" #경로 북마크와 같은 역할인듯
urlpatterns = [
    path('hello_world/', hello_world, name = 'hello_world'), #주소, view, 라우트에 대한 대표 이름
    path('create/', AccountCreate.as_view(), name = 'create'),
    path('login/', LoginView.as_view(template_name = 'accountapp/login.html'), name = 'login'),
    path('login/', LogoutView.as_view(template_name = 'accountapp/logout.html'), name = 'logout'),
]