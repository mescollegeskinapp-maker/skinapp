from django.db import models

# Create your models here.
class LoginTable(models.Model):
    username=models.CharField(max_length=100, null=True, blank=True)
    password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=100)

class UserTable(models.Model):
    LOGINID=models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    name=models.CharField(max_length=100 ,null=True, blank=True)
    age=models.CharField(max_length=200 ,null=True, blank=True)
    mobileno=models.BigIntegerField(null=True, blank=True)
    gender=models.CharField(max_length=100, null=True, blank=True)
    email=models.CharField(max_length=100, null=True, blank=True)

class DoctorTable(models.Model):
    LOGINID=models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    name=models.CharField(max_length=100, null=True,blank=True)
    age=models.IntegerField(null=True, blank=True)
    gender=models.CharField(max_length=100 ,null=True, blank=True)
    field=models.CharField(max_length=100)
    hospitalname=models.CharField(max_length=200, null=True, blank=True )
    mobileno=models.CharField(max_length=10 ,null=True, blank=True)
    
class BookingTable(models.Model):
    USERID=models.ForeignKey(UserTable, on_delete=models.CASCADE)
    DOCTORID=models.ForeignKey(DoctorTable, on_delete=models.CASCADE)
    appoinmentdate=models.DateField()
    status=models.CharField(max_length=100, null=True, blank=True)

class FeedbackTable(models.Model):
    USERID=models.ForeignKey(UserTable,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    feedback=models.CharField(max_length=200, null=True, blank=True)

class PrescriptionTable(models.Model):
    BookingID=models.ForeignKey(BookingTable,on_delete=models.CASCADE)
    Prescription=models.CharField(max_length=200 ,null=True, blank=True)
    date=models.DateField(auto_now_add=True)

class IntakingmedicineTable(models.Model):
    USER=models.ForeignKey(UserTable,on_delete=models.CASCADE)
    MedicineName=models.CharField(max_length=200 ,null=True, blank=True)
    prescriptionimage=models.ImageField(upload_to='intakingmedicine/', null=True, blank=True)
    description=models.CharField(max_length=200 ,null=True, blank=True)
    date=models.DateField(auto_now_add=True)