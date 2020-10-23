from django.shortcuts import render
from django.http import HttpResponseRedirect
from todo_list.models import TDList, Task
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.template.context_processors import csrf
from django.http import JsonResponse
from django.conf.urls.static import static
from django.conf import settings

def registration(request):
	User.objects.create_user(username = request.POST.get('login'), password = request.POST.get('pass'))
	login(request)

def login(request):
	if request.POST.get('login') and request.POST.get('pass'):
		if User.objects.filter(username=request.POST.get('login')).exists():	
			user = auth.authenticate(username = request.POST.get('login',''), password = request.POST.get('pass',''))
			if user:
				print('login')
				auth.login(request, user)
		else:
			registration(request)
	return HttpResponseRedirect('/')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')

@login_required()
def showdata(request, context):
	user = request.user		
	context['tdlists'] = TDList.objects.filter(user=user)
	return render(request, 'index.html', context)

def index(request):
	context = {}
	context['username'] = request.user.username

	response = showdata(request, context)
	if response.status_code == 200:
		return response
	elif response.status_code == 302:
		return render(request, 'index.html', context)

def change_status(request):	
	data = request.POST
	task = Task.objects.get(id=data.get('id'))
	task.done = not task.done
	task.save()
	return JsonResponse({'status': 'success'})

def add_task(request):	
	data = request.POST
	ID = data.get('id')
	project = TDList.objects.get(id=ID)
	prior = project.task.count() + 1
	newtask = Task.objects.create(name = data.get('newtask'), priority = prior)
	project.task.add(newtask)
	return JsonResponse({'status': 'success',
						'id': newtask.id,
						'name': newtask.name})

def delete_task(request):
	data = request.POST
	ID = data.get('id')
	task = Task.objects.get(id=ID)
	tasks = Task.objects.filter(priority__gt=task.priority)
	for t in tasks:
		t.priority -= 1
		t.save()
	task.delete()
	return JsonResponse({'status': 'success'})

def delete_list(request):
	data = request.POST
	ID = data.get('id')
	project = TDList.objects.get(id=ID)
	project.task.all().delete()
	project.delete()
	return JsonResponse({'status': 'success'})

def add_list(request):
	data = request.POST
	newlist = TDList.objects.create(name = data.get('name'), user = request.user)
	return JsonResponse({'status': 'success',
						'id':newlist.id})
def edit_list(request):
	data = request.POST
	project = TDList.objects.get(id=data['id'])
	project.name = data['newname']
	project.save()
	return JsonResponse({'status': 'success'})

def edit_task(request):
	data = request.POST
	task = Task.objects.get(id=data['id'])
	task.name = data['newname']
	task.save()
	return JsonResponse({'status': 'success'})

def prup(request):
	data = request.POST
	ID = data['id']
	project = TDList.objects.get(task__id=ID)
	maxprior = project.task.count()
	task = project.task.get(id=data['id'])
	prevprior = task.priority
	if prevprior < maxprior:
		newprior = task.priority + 1
		taskswap = project.task.get(priority=newprior)
		taskswap.priority = prevprior
		taskswap.save()
		task.priority = newprior	
		task.save()			
		return JsonResponse({'status': 'success',
							'swapid': taskswap.id,
							'swapname': taskswap.name,
							'checked': taskswap.done,
							'date':taskswap.deadline})
	else:
		print('fail')
		return JsonResponse({'status':'fail'})

def prdown(request):
	data = request.POST
	ID = data['id']
	project = TDList.objects.get(task__id=ID)
	maxprior = project.task.count()
	task = project.task.get(id=data['id'])
	prevprior = task.priority
	if prevprior > 1:
		newprior = task.priority - 1
		taskswap = project.task.get(priority=newprior)
		taskswap.priority = prevprior
		taskswap.save()
		task.priority = newprior	
		task.save()		
		return JsonResponse({'status': 'success',
							'swapid': taskswap.id,
							'name': task.name,
							'checked': task.done,
							'date':task.deadline})
	else:
		print('fail')
		return JsonResponse({'status':'error'})

def task_date(request):
	data = request.POST
	ID = data['id']
	task = Task.objects.get(id=ID)
	task.deadline = data['date']
	task.save()
	return JsonResponse({'status': 'success'})

def project_date(request):
	data = request.POST
	ID = data['id']
	project = TDList.objects.get(id=ID)
	project.deadline = data['date']
	project.save()
	return JsonResponse({'status': 'success'})