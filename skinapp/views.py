from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from skinapp.models import *
from skinapp.forms import DoctorForm, PrescriptionForm

# Create your views here.
class   LoginView(View):
    def get(self, request):
        return render(request, 'administration/login.html')
    def post(self, request):
        username1=request.POST['username']
        password1=request.POST['password']
        print(username1)
        print(password1)

        login_obj=LoginTable.objects.get(username=username1,password=password1)
        print("$$$$$$$$$$$$$$$$$$",login_obj)
        request.session['userid']=login_obj.id
        print(request.session['userid'])
              
        if login_obj.usertype=="admin":
            return HttpResponse('''<script>alert("admin_home");window.location=("adminhome")</script>''')
        elif login_obj.usertype=="Doctor":
               return HttpResponse('''<script>alert("doctor");window.location=("doctorhome")</script>''')
        else:
               return HttpResponse('''<script>alert("invalid user");window.location=("login")</script>''')
class AddDoctorView(View):
    def get(self, request):
            return render(request, 'administration/adddoctor.html')
    def post(self, request):
        form=DoctorForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.LOGINID=LoginTable.objects.create(username=request.POST['username'],password=request.POST['password'],usertype='Doctor')
            f.save()
            return HttpResponse('''<script>alert("Registered Successfully");window.location=("/adminhome")</script>''')
    
class EditDoctorView(View):
    def get(self, request, id):
            obj = DoctorTable.objects.get(id=id)   
            return render(request, 'administration/editdoctor.html',{'data':obj})
    def post(self, request, id):
        obj = DoctorTable.objects.get(id=id)   
        form=DoctorForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
          
            return HttpResponse('''<script>alert("Registered Successfully");window.location=("/managedoctor")</script>''')
    
class ManageDoctorView(View):
    def get(self, request):
            obj=DoctorTable.objects.all()
            return render(request, 'administration/managedoctor.html', {'data':obj})
class DeleteDoctor(View):
    def get(self, request,id):
            obj=LoginTable.objects.get(id=id)
            obj.delete()
            return  HttpResponse('''<script>alert("Deleted Successfully");window.location=("/managedoctor")</script>''')
    
class FeedbackView(View):
    def get(self, request):
            objects=FeedbackTable.objects.all()
            return render(request, 'administration/feedback.html', {'data':objects})
class ViewUserView(View):
    def get(self, request):
        obj=UserTable.objects.all()
        return render(request, 'administration/viewuser.html', {'data':obj})
    
class adminhomeView(View):
        def get(self,request):
            return render(request, 'administration/adminhome.html')

########################################  DOCTOR  #####################################################


class AddPrescriptionView(View):
    def get(self, request, id):
            c=BookingTable.objects.get(id=id)
            return render(request, 'doctor/addprescription.html',{'user':c})
    def post(self, request, id):
        form=PrescriptionForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.BookingID=BookingTable.objects.get(id=id)
            f.save()

       
        return HttpResponse('''<script>alert("Prescription added  Successfully");window.location=("/adminhome")</script>''')

    
class ViewPatientreqView(View):
    def get(self, request):
            obj=BookingTable.objects.all()
            return render(request, 'doctor/viewpatientreq.html',{'data':obj})
class AcceptBooking(View):
    def get(self, request,id):
            obj=BookingTable.objects.get(id=id)
            obj.status="Accepted"
            obj.save()
            return  HttpResponse('''<script>alert("Booking Accepted Successfully");window.location=("/viewpatientreq")</script>''')
class RejectBooking(View):
    def get(self, request,id):
            obj=BookingTable.objects.get(id=id)
            obj.status="Rejected"
            obj.save()
            return  HttpResponse('''<script>alert("Booking Rejected Successfully");window.location=("/viewpatientreq")</script>''')   
class ViewPrescriptionView(View):
    def get(self, request):
            obj=PrescriptionTable.objects.all()
                
            return render(request, 'doctor/viewprescription.html',{'data':obj})
    def post(self, request):
        form=PrescriptionForm(request.POST)
        if form.is_valid():
         f=form.save(commit=False)
         f.save()
        return HttpResponse('''<script>alert("Prescription added  Successfully");window.location=("/adminhome")</script>''')
class DeletePrescription(View):
    def get(self, request,id):
            obj=PrescriptionTable.objects.get(id=id)
            obj.delete()
            return  HttpResponse('''<script>alert("Deleted Successfully");window.location=("/viewprescription")</script>''')  

class EditPrescription(View):
    def get(self, request, id):
            obj = PrescriptionTable.objects.get(id=id)   
            print(obj)
            return render(request, 'doctor/editprescription.html',{'data':obj})
    def post(self, request, id):
        obj = PrescriptionTable.objects.get(id=id)

        # Get the textarea value
        prescription_text = request.POST.get('Prescription')

        # Update the field manually
        obj.Prescription = prescription_text
        obj.save()
        return  HttpResponse('''<script>alert("updated Successfully");window.location=("/viewprescription")</script>''')  
 
class doctorhomeView(View):
       def get(self, request):
            return render(request, 'doctor/doctorhome.html')    

class IntakingmedicineView(View):
    
    def get(self, request):
        obj=IntakingmedicineTable.objects.all()
        return render(request, 'doctor/intakingmedicine.html', {'data':obj})
    
#########################api views #########################
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from skinapp.serializer import *

class LoginPage_api(APIView):
     def post(self, request):
          response_dict={}
          username=request.data.get('username')
          password=request.data.get('password')
          if not username or not password:
               response_dict['message']="failed"
               return Response(response_dict,status=status.HTTP_400_BAD_REQUEST)
          t_user=LoginTable.objects.filter(username=username,password=password).first()
          if not t_user:
               response_dict['message']="invalid user"
               return Response(response_dict,status=status.HTTP_404_NOT_FOUND)
          else:   
                response_dict['message']="success"
                response_dict['login_id']=t_user.id   
                response_dict['usertype']=t_user.usertype
                return Response(response_dict,status=status.HTTP_200_OK)
    
class UserReg_api(APIView):
     def post(self,request):
        print("#######################",request.data)
        user_serial=UserSerializer(data=request.data)
        login_serial=LoginSerializer(data=request.data)
        print("#######################",user_serial.is_valid())
        print("#######################",login_serial.is_valid())
        data_valid=user_serial.is_valid()
        login_valid=login_serial.is_valid()
        if data_valid and login_valid:
            login_profile=login_serial.save(usertype='user')
            user_serial.save(LOGINID=login_profile)

            return Response(user_serial.data,status=status.HTTP_201_CREATED)
        return Response({
                'login error_errors':user_serial.errors if not login_valid else None,

                'user_errors':user_serial.errors if not data_valid else None
        },status=status.HTTP_400_BAD_REQUEST
        )
     
class ViewDoctor_api(APIView):
    def get(self, request):
        d=DoctorTable.objects.all()
        serializer=DoctorSerializer(d,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class ViewBooking_api(APIView):
     def get(self, request,id):
        b=BookingTable.objects.filter(USERID__LOGINID__id=id)
        serializer=BookingSerializer(b,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class Bookappoinment_api(APIView):
    def post(self, request, id):
        try:
            user=UserTable.objects.get(LOGINID_id=id)
        except UserTable.DoesNotExist:
               return Response({'message':'User not found'}, status=status.HTTP_404_NOT_FOUND)
        data=request.data.copy()
        serializer=BookingSerializer(data=data)
        if serializer.is_valid():
            booking =serializer.save(USERID=user)
            return Response({'message':'Appointment booked succesfully','booking_id':booking.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ViewFeedback_api(APIView):
    #  def get(self, request,id):
    #     f=FeedbackTable.objects.filter(USERID__LOGINID_id=id)
    #     serializer=FeedbackSerializer(f,many=True)
    #     return Response(serializer.data,status=status.HTTP_200_OK)
     def post(self, request,id):
        try:
            user=UserTable.objects.get(LOGINID_id=id)
        except UserTable.DoesNotExist:
               return Response({'message':'User not found'}, status=status.HTTP_404_NOT_FOUND)
        data=request.data.copy()
        serializer=FeedbackSerializer(data=data)
        if serializer.is_valid():
            feedback =serializer.save(USERID=user)
            return Response({'message':'Feedback added succesfully','feedback_id':feedback.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
class ViewPrescription_api(APIView):
     def get(self, request,id):
        p = PrescriptionTable.objects.filter(BookingID__id=id)
        serializer = PrescriptionSerializer(p, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
     
class Addmedicine_api(APIView):
      def post(self, request, id):
        try:
            user=UserTable.objects.get(LOGINID_id=id)
        except UserTable.DoesNotExist:
               return Response({'message':'User not found'}, status=status.HTTP_404_NOT_FOUND)
        data=request.data.copy()
        serializer=IntakingmedicineSerializer(data=data)
        if serializer.is_valid():
            booking =serializer.save(USER=user)
            return Response({'message':'medicine added succesfully','booking_id':booking.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ViewMedicine_api(APIView):
    def get(self, request, id):
        user = UserTable.objects.get(LOGINID_id=id)
        m = IntakingmedicineTable.objects.filter(USER=user)
        serializer = IntakingmedicineSerializer(m, many=True)
        return Response(serializer.data)

class EditMedicine_api(APIView):
    def put(self, request, id):
        try:
            med = IntakingmedicineTable.objects.get(id=id)
        except:
            return Response({"error": "Not Found"}, status=404)

        serializer = IntakingmedicineSerializer(med, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Updated Successfully"})
        return Response(serializer.errors, status=400)

class DeleteMedicine_api(APIView):
    def delete(self, request, id):
        try:
            med = IntakingmedicineTable.objects.get(id=id)
            med.delete()
            return Response({"message": "Deleted"}, status=200)
        except:
            return Response({"error": "Not Found"}, status=404)
