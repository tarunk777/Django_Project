from django.db import models
from Webapp.choices import ProductCategoryChoice
class Register(models.Model):
	username=models.CharField(max_length=122)
	Firstname=models.CharField(max_length=122)
	lastname=models.CharField(max_length=122)
	email=models.CharField(max_length=122)
	password=models.CharField(max_length=10)

	def __str__(self):
		return self.Firstname


class Contact(models.Model):
	name=models.CharField(max_length=122)
	email=models.CharField(max_length=122)
	state=models.CharField(max_length=122)
	city=models.CharField(max_length=122)
	zip=models.CharField(max_length=122)
	query=models.TextField()

	def __str__(self):
		return self.name
	
class Product(models.Model):
	p_name=models.CharField(max_length=250,blank=True,null=True)
	p_category=models.CharField(max_length=250,blank=True,null=True,choices=ProductCategoryChoice.choices)
	p_discription=models.CharField(max_length=250,blank=True,null=True)
	p_image = models.FileField()

	def __str__(self):
		#return self.p_name, self.id
		 return '{} {}'.format(self.p_name, self.id)
    
        
