
from django.urls import path

from skinapp.views import *

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('adddoctor', AddDoctorView.as_view(), name='adddoctor'),
    path('editdoctor/<int:id>', EditDoctorView.as_view(), name='editdoctor'),
     path('DeleteDoctor/<int:id>', DeleteDoctor.as_view(), name='DeleteDoctor'),
    path('managedoctor', ManageDoctorView.as_view(), name='managedoctor'),
    path('feedback', FeedbackView.as_view(), name='feedback'),
    path('viewuser', ViewUserView.as_view(), name='viewuser'),
    path('adminhome',adminhomeView.as_view(),name='adminhome'),
    ########################################  DOCTOR  #####################################################
    path('addprescription/<int:id>', AddPrescriptionView.as_view(), name='addprescription'),
    path('viewpatientreq', ViewPatientreqView.as_view(), name='viewpatientreq'),
    path('AcceptBooking/<int:id>', AcceptBooking.as_view(), name='AcceptBooking'),
    path('RejectBooking/<int:id>', RejectBooking.as_view(), name='RejectBooking'),
    path('viewprescription', ViewPrescriptionView.as_view(), name='viewprescription'),
    path('DeletePrescription/<int:id>', DeletePrescription.as_view(), name='DeletePrescription'),
    path('editprescription/<int:id>', EditPrescription.as_view(), name='editprescription'),
    path('doctorhome',doctorhomeView.as_view(),name='doctorhome'),
    path('intakingmedicine', IntakingmedicineView.as_view(), name='intakingmedicine'),
    ##################################api urls #########################################
    path('LoginPage_api', LoginPage_api.as_view(), name='LoginPage_api'),
    path('UserReg_api', UserReg_api.as_view(), name='UserReg_api'),
    path('ViewDoctor_api', ViewDoctor_api.as_view(), name='ViewDoctor_api'),
    path('ViewBooking_api/<int:id>', ViewBooking_api.as_view(), name='ViewBooking_api'),
    path('ViewFeedback_api/<int:id>', ViewFeedback_api.as_view(), name='ViewFeedback_api'),
    path('ViewPrescription_api/<int:id>', ViewPrescription_api.as_view(), name='ViewPrescription_api'),
    path('Bookappointment_api/<int:id>', Bookappoinment_api.as_view(), name='Bookappointment_api'),
    path('Addmedicine_api/<int:id>', Addmedicine_api.as_view(), name='Addmedicine_api'),
    path('ViewMedicine_api/<int:id>', ViewMedicine_api.as_view(), name='ViewIntakingmedicine_api'),
    path('EditMedicine_api/<int:id>', EditMedicine_api.as_view(), name='EditIntakingmedicine_api'),
    path('DeleteMedicine_api/<int:id>', DeleteMedicine_api.as_view(), name='DeleteIntakingmedicine_api'),

]