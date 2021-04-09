
from django.db import models
# Create your models here.
class Patients(models.Model):
    name= models.CharField(max_length=20)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    address=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Doctors(models.Model):
	name=models.CharField(max_length=30)
	qualification=models.CharField(max_length=50)
	specialist=models.CharField(max_length=50)
	treatable_disease=models.CharField(max_length=200)
	description=models.CharField(max_length=300)
	username=models.CharField(max_length=200)
	contact_no=models.CharField(max_length=200)
	image=models.ImageField()
	email=models.EmailField(null=True)
	address=models.CharField(max_length=100,null=True)
	def __str__(self):
		return self.name

class Diseases(models.Model):
	name=models.CharField(max_length=50)
	discription=models.CharField(max_length=500)
	causes=models.CharField(max_length=500)
	preventive_measures=models.CharField(max_length=500)
	symptoms=models.CharField(max_length=200)
	image=models.ImageField()
	def __str__(self):
		return self.name

class Donator(models.Model):
	name=models.CharField(max_length=50,null=True)
	address=models.CharField(max_length=50)
	email=models.EmailField()
	amounts=models.IntegerField()
	comment=models.CharField(max_length=500,default=None)
	def __str__(self):
		return self.name

class Donator_success(models.Model):
	name=models.CharField(max_length=50,default=None)
	amount=models.IntegerField(default=None,null=True)
	payment_status=models.CharField(max_length=50,default=None,null=True)
	def __str__(self):
		return self.payment_status

class Appointment(models.Model):
	patient_name=models.CharField(max_length=50)
	email=models.EmailField()
	phone=models.IntegerField(null=True)
	address=models.CharField(max_length=100)
	appointment_date=models.DateField()
	time=models.CharField(max_length=50)
	gender=models.CharField(max_length=20)
	doctor_name=models.CharField(max_length=50)
	message=models.CharField(max_length=800)

	def __str__(self): #showing models based on the doctor's name
		return self.doctor_name
#database for online consultation
class Online_consultation(models.Model):
	patient_name=models.CharField(max_length=50)
	email=models.EmailField()
	phone=models.IntegerField(null=True)
	address=models.CharField(max_length=100)
	problem_start_date=models.DateField()
	age=models.CharField(max_length=50)
	gender=models.CharField(max_length=20)
	doctor_name=models.CharField(max_length=50)
	issue=models.CharField(max_length=800)

	def __str__(self): #showing models based on the doctor's name
		return self.doctor_name

# creating user type ' doctor ' to handle doctor login
# class User(AbstractUser):
#     is_doctor = models.BooleanField(default=False)
#
# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class User_type(models.Model):
	username=models.CharField(max_length=50, null=True)
	user_type=models.CharField(max_length=50, null=True)
	email=models.CharField(max_length=50,null=True)
