from django import forms

from skinapp.models import BookingTable, DoctorTable, FeedbackTable, PrescriptionTable


class DoctorForm(forms.ModelForm):
  class Meta:
        model = DoctorTable
        fields = ['name', 'age', 'gender', 'field', 'hospitalname', 'mobileno']
class BookingForm(forms.ModelForm):
  class Meta:
        model = BookingTable
        fields = ['USERID','DOCTORID','appoinmentdate','status']
class FeedbackForm(forms.ModelForm):
  class Meta:
        model = FeedbackTable
        fields = ['feedback'] 
class PrescriptionForm(forms.ModelForm):
  class Meta:
        model = PrescriptionTable
        fields = ['Prescription']
