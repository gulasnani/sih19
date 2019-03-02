from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Region(models.Model):
	pincode = models.CharField(max_length=6, primary_key=True)
	city = models.CharField(max_length=255, default=None)
	state = models.CharField(max_length=255, default=None)
	longitude = models.FloatField(default=25.3176)
	latitude = models.FloatField(default=82.9739)


class User(AbstractUser):
	GENDER_CHOICES = (
			('M','Male'),
			('F','Female'),
			('O','Other')
		)
	USER_TYPE_CHOICES = (
			('P','Person'),
			('H','Hospital'),
			('D','Dispensary'),
			('L','Lab')
		)
	age = models.IntegerField(null=True)
	gender = models.CharField(GENDER_CHOICES,null=True,max_length=1)
	phone = models.CharField(max_length=13,null=True)
	address = models.TextField(default='') 
	pincode = models.ForeignKey(Region,on_delete=models.CASCADE,null=True)
	type_user = models.CharField(USER_TYPE_CHOICES,max_length=1,null=True)

	def __str__(self):
		return str(self.id) + str(self.first_name)


class Report(models.Model):
	sentByUser = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="by_user")
	sentForUser = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="for_user")
	report_time = models.DateTimeField(auto_now_add=True)
	disease = models.CharField(max_length=255)
	diagnosis = models.BooleanField()
	pdf_path = models.FileField(upload_to='reports/user_{0}/user_{1}/%Y/%m/%d'.format(sentForUser,sentByUser),max_length=500,null=True)
	#pdf_path = models.FileField(upload_to='reports/user_1/%Y/%m/%d',null=True)
	
	def __str__(self):
		return str(self.disease)


class WaterbodyReport(models.Model):
	sent_by_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	report_time = models.DateTimeField(auto_now_add=True)
	bodyname = models.CharField(max_length=255)
	rating = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)],default=5)
	pincode = models.ForeignKey(Region,on_delete=models.CASCADE,null=True)
	image_path = models.ImageField(upload_to='images/user_{0}/%Y/%m/%d'.format(sent_by_user),null=True)

	def __str__(self):
		return str(self.bodyname)


class Predict(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	prediction_time = models.DateTimeField(auto_now_add=True)
	disease_predicted = models.CharField(max_length=255)
	pincode = models.ForeignKey(Region,on_delete=models.CASCADE)


class Hospital(User):
	malaria_free = models.PositiveSmallIntegerField()
	tb_free = models.PositiveSmallIntegerField()
	dengue_free = models.PositiveSmallIntegerField()
	rating = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)],default=3)

class HospitalCurrent(models.Model):
	hospital = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	time = models.DateTimeField(auto_now_add=True)
	malaria_rep = models.PositiveSmallIntegerField()
	tb_rep = models.PositiveSmallIntegerField()
	dengue_rep = models.PositiveSmallIntegerField()
	malaria_dis = models.PositiveSmallIntegerField()
	tb_dis = models.PositiveSmallIntegerField()
	dengue_dis = models.PositiveSmallIntegerField()


class HeatmapActual(models.Model):
	pincode = models.ForeignKey(Region,on_delete=models.CASCADE)
	intensity = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(0)],default=5)


class HeatmapPredicted(models.Model):
	pincode = models.ForeignKey(Region,on_delete=models.CASCADE)
	intensity = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(0)],default=5)


class News(models.Model):
	date = models.DateTimeField()
	article_author = models.CharField(max_length=255)
	article_text_path = models.FilePathField(path="/")
	article_img_path = models.FilePathField(path="/")
	pincode = models.ForeignKey(Region,on_delete=models.CASCADE)


class Lab(User):
	certificate = models.ImageField(upload_to='certificates/user_{0}/%Y/%m/%d'.format(id))
	owner = models.CharField(max_length=255)
	govt_id = models.CharField(max_length=255)






	