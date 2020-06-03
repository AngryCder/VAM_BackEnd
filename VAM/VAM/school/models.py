from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class School(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=100, help_text="name of the school")
	address = models.CharField(max_length=500, help_text="address of the school")

	def __str__(self):
		return self.name

class Teacher(models.Model):
	name = models.CharField(max_length=100, help_text="name of the teacher")
	school = models.ForeignKey(School, on_delete=models.CASCADE, help_text="School")
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	Courses = models.ForeignKey(Courses, on_delete=models.CASCADE, help_text="Courses")

	def __str__(self):
		return self.name

class Courses(models.Model):
	subject = models.CharField(max_length=50, help_text="name of the course")

class Student(model.Model):
	school = models.ForeignKey(School, on_delete=models.CASCADE, help_text="School")
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	Courses = models.ForeignKey(Courses, on_delete=models.CASCADE, help_text="Courses")
	roll = models.IntegerField(primary_key=True)

	def __str__(self):
		return self.roll