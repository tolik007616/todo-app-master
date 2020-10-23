from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
	name = models.CharField(max_length = 255)
	done = models.BooleanField(default=False)
	deadline = models.DateField(null = True, blank = True)
	priority = models.IntegerField(default = 0)
	#tdlist = models.ForeignKey(TDList, on_delete=models.CASCADE, null = True, blank = True)

	def __str__(self):
		return self.name

class TDList(models.Model):
	name = models.CharField(max_length = 64)
	task = models.ManyToManyField(Task, blank = True)		
	deadline = models.DateField(null = True, blank = True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)	

	def __str__(self):
		return self.name