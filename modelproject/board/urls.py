from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_list),
    path('<int:pk>/', blog_detail), #여기서 pk는 blog_detail함수의 인자 pk를 말함
]

