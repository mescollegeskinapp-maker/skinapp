from rest_framework.serializers import ModelSerializer
from .models import BookingTable, DoctorTable , FeedbackTable, PrescriptionTable

class DoctorSerializer(ModelSerializer):
  class Meta:
        model = DoctorTable
        fields = ['name', 'age', 'gender', 'field', 'hospitalname', 'mobileno']


class BookingSerializer(ModelSerializer):
  class Meta:
        model = BookingTable
        fields = ['USERID','DOCTORID','appoinmentdate','status']
class FeedbackSerializer(ModelSerializer):
  class Meta:
        model = FeedbackTable
        fields = ['feedback']
class PrescriptionSerializer(ModelSerializer):
  class Meta:
        model = PrescriptionTable
        fields = ['Prescription']
class IntakingmedicineSerializer(ModelSerializer):
  class Meta:
        model = PrescriptionTable
        fields = ['MedicineName','prescriptionimage','description']
class LoginSerializer(ModelSerializer):
  class Meta:
        model = PrescriptionTable
        fields = ['username','password','usertype']
class UserSerializer(ModelSerializer):
  class Meta:
        model = PrescriptionTable
        fields = ['name','age','mobileno,gender','email']