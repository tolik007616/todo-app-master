from django.test import SimpleTestCase
from django.urls import reverse, resolve
from todo_list.views import *

class TestUrls(SimpleTestCase):

	def test_index(self):
		url = reverse('index')		
		self.assertEquals(resolve(url).func, index)

	def test_register(self):
		url = reverse('register')		
		self.assertEquals(resolve(url).func, registration)

	def test_login(self):
		url = reverse('login')		
		self.assertEquals(resolve(url).func, login)

	def test_logout(self):
		url = reverse('logout')		
		self.assertEquals(resolve(url).func, logout)

	def test_add_list(self):
		url = reverse('add_list')		
		self.assertEquals(resolve(url).func, add_list)

	def test_change_status(self):
		url = reverse('change_status')		
		self.assertEquals(resolve(url).func, change_status)

	def test_delete_task(self):
		url = reverse('delete_task')		
		self.assertEquals(resolve(url).func, delete_task)

	def test_delete_list(self):
		url = reverse('delete_list')		
		self.assertEquals(resolve(url).func, delete_list)

	def test_add_task(self):
		url = reverse('add_task')		
		self.assertEquals(resolve(url).func, add_task)

	def test_add_list(self):
		url = reverse('add_list')		
		self.assertEquals(resolve(url).func, add_list)

	def test_edit_list(self):
		url = reverse('edit_list')		
		self.assertEquals(resolve(url).func, edit_list)

	def test_edit_task(self):
		url = reverse('edit_task')		
		self.assertEquals(resolve(url).func, edit_task)

	def test_prup(self):
		url = reverse('prup')		
		self.assertEquals(resolve(url).func, prup)

	def test_prdown(self):
		url = reverse('prdown')		
		self.assertEquals(resolve(url).func, prdown)

	def test_task_date(self):
		url = reverse('task_date')		
		self.assertEquals(resolve(url).func, task_date)

	def test_project_date(self):
		url = reverse('project_date')		
		self.assertEquals(resolve(url).func, project_date)