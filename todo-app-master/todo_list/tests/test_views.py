from django.test import TestCase, Client
from django.urls import reverse
from todo_list.models import *
from datetime import date
import json

class TestViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.task1 = Task.objects.create(name ='Task 1', priority = 1)
		self.task2 = Task.objects.create(name ='Task 2', priority = 2)
		self.task3 = Task.objects.create(name ='Task 3', priority = 3)
		self.project = TDList.objects.create(name = 'Project 1')
		self.project.task.add(self.task1, self.task2, self.task3)

	def test_logout(self):
		response = self.client.get(reverse('logout'))
		self.assertEquals(response.status_code, 302)

	def test_login(self):
		response = self.client.post(reverse('login'))
		self.assertEquals(response.status_code, 302)
	
	def test_change_status(self):
		client = Client()
		response = client.post(reverse('change_status'),{
			'id':1
			})
		self.assertEquals(response.status_code, 200)

	def test_add_task(self):
		client = Client()
		response = client.post(reverse('add_task'),{
			'id':1,
			'newtask':'Task 4'
			})
		self.assertEquals(response.status_code, 200)

	def test_delete_task(self):
		client = Client()
		response = client.post(reverse('delete_task'),{
			'id':3
			})
		self.assertEquals(response.status_code, 200)

	def test_delete_list(self):
		client = Client()
		response = client.post(reverse('delete_list'),{
			'id':1
			})
		self.assertEquals(response.status_code, 200)

	def test_edit_list(self):
		client = Client()
		response = client.post(reverse('edit_list'),{
			'id':1,
			'newname':"Newname"
			})
		self.assertEquals(response.status_code, 200)

	def test_edit_task(self):
		client = Client()
		response = client.post(reverse('edit_task'),{
			'id':1,
			'newname':'Newname'
			})
		self.assertEquals(response.status_code, 200)

	def test_prup(self):
		client = Client()
		response = client.post(reverse('prup'),{
			'id':2
			})
		self.assertEquals(response.status_code, 200)

	def test_prdown(self):
		client = Client()
		response = client.post(reverse('prdown'),{
			'id':2
			})
		self.assertEquals(response.status_code, 200)

	def test_task_date(self):
		client = Client()
		response = client.post(reverse('task_date'),{
			'id':1,
			'date': date.today()
			})
		self.assertEquals(response.status_code, 200)

	def test_project_date(self):
		client = Client()
		response = client.post(reverse('project_date'),{
			'id':1,
			'date': date.today()
			})
		self.assertEquals(response.status_code, 200)