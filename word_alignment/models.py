from django.db import models

# Create your models here.
class userInput(models.Model):
	first=models.CharField(max_length=30)
	second=models.CharField(max_length=30)
	ifile=models.FileField(upload_to='file/input/')

class savedFile(models.Model):
	name=models.CharField(max_length=100)
	date=models.DateTimeField(auto_now_add=True)
	ofile=models.FileField(upload_to='file/output')
	markfile=models.FileField(upload_to='file/markedfile')

	def __str__(self):
		return self.name