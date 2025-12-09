from rest_framework.serializers import ModelSerializer
from .models import *

class DoctorSerializer(ModelSerializer):
  class Meta:
        model = DoctorTable
        fields = ['id','name', 'age', 'gender', 'field', 'hospitalname', 'mobileno']


class BookingSerializer(ModelSerializer):
    DOCTORID = DoctorSerializer()

    class Meta:
        model = BookingTable
        fields = ['id','DOCTORID', 'appoinmentdate', 'status']

class FeedbackSerializer(ModelSerializer):
  class Meta:
        model = FeedbackTable
        fields = ['rating', 'feedback']
class PrescriptionSerializer(ModelSerializer):
  class Meta:
        model = PrescriptionTable
        fields = ['Prescription']
class IntakingmedicineSerializer(ModelSerializer):
  class Meta:
        model = IntakingmedicineTable
        fields = ['id','MedicineName','prescriptionimage','description']
class LoginSerializer(ModelSerializer):
  class Meta:
        model = LoginTable
        fields = ['username','password']
class UserSerializer(ModelSerializer):
  class Meta:
        model = UserTable
        fields = ['name','age','mobileno','gender','email']