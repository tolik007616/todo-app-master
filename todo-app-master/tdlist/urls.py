from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from todo_list.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	url(r'^$', index, name="index"),
	path('register/', registration, name='register'),
	path('login/', login, name='login'),
	path('logout/', logout, name='logout'),
	path('add_list/', add_list, name='add_list'),
	path('change_status/', change_status, name='change_status'),
	path('delete_task/', delete_task, name='delete_task'),
	path('delete_list/', delete_list, name='delete_list'),
	path('add_task/', add_task, name='add_task'),
	path('add_list/', add_list, name='add_list'),
	path('edit_list/', edit_list, name='edit_list'),
	path('edit_task/', edit_task, name='edit_task'),
	path('prup/', prup, name='prup'),
	path('prdown/', prdown, name='prdown'),
	path('task_date/', task_date, name='task_date'),
	path('project_date/', project_date, name='project_date'),
    path('admin/', admin.site.urls, name='admin'),
] + staticfiles_urlpatterns()

