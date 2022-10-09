from django.urls import path
from todolist.views import register 
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import tambahin
from todolist.views import show
from todolist.views import checklist
from todolist.views import hapus
from todolist.views import show_json

app_name = 'todolist'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', tambahin, name='create-task'),
    path('', show, name='show'),
    path('checklist/<int:pk>/', checklist, name='checklist'),
    path('hapus/<int:pk>/', hapus, name='hapus'),
    path('json/', show_json, name='show_json'),
]