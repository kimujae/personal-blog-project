from django.urls import path
from accountapp.views import hello_world

app_name = "accountapp" #경로 북마크와 같은 역할인듯
urlpatterns = [
    path('hello_world/', hello_world, name = 'hello_world') #주소, view, 라우트에 대한 대표 이름
]