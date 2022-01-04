from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


classification=(('Student','Student'),
('Staff','Staff'),
('Other','Other'),
)

mondays_available=(
('Monday Morning 6:00am-8:00am','Monday Morning 6:00am-8:00am'),
('Monday Morning 8:00am-10:00am','Monday Morning 8:00am-10:00am'),
('Monday Morning 10:00am-11:59am','Monday Morning 10:00am-11:59am'),
('Monday Morning 6:00am-11:59am','Monday Morning 6:00am-11:59am'),
('Monday AfterNoon 2:00pm-4:00pm','Monday AfterNoon 2:00pm-4:00pm'),
('Monday Everning 5:00pm-7:00pm','Monday Everning 5:00pm-7:00pm'),
('Monday Night 8:00pm-10:00pm','Monday Night 8:00pm-10:00pm'),
('Monday 10:00pm-6:00am','Monday 10:00pm-6:00am'),
('Monday Available','Monday Available'),
('Monday Unavailable','Monday Unavailable'),
)

tuesdays_available=(
('Tuesday Morning 6:00am-8:00am','Tuesday Morning 6:00am-8:00am'),
('Tuesday Morning 8:00am-10:00am','Tuesday Morning 8:00am-10:00am'),
('Tuesday Morning 10:00am-11:59am','Tuesday Morning 10:00am-11:59am'),
('Tuesday Morning 6:00am-11:59am','Tuesday Morning 6:00am-11:59am'),
('Tuesday AfterNoon 2:00pm-4:00pm','Tuesday AfterNoon 2:00pm-4:00pm'),
('Tuesday Everning 5:00pm-7:00pm','Tuesday Everning 5:00pm-7:00pm'),
('Tuesday Night 8:00pm-10:00pm','Tuesday Night 8:00pm-10:00pm'),
('Tuesday 10:00pm-6:00am','Tuesday 10:00pm-6:00am'),
('Tuesday Available','Tuesday Available'),
('Tuesday Unavailable','Tuesday Unavailable'),
)


wednesdays_available=(
('Wednesday Morning 6:00am-8:00am','Wednesday Morning 6:00am-8:00am'),
('Wednesday Morning 8:00am-10:00am','Wednesday Morning 8:00am-10:00am'),
('Wednesday Morning 10:00am-11:59am','Wednesday Morning 10:00am-11:59am'),
('Wednesday Morning 6:00am-11:59am','Wednesday Morning 6:00am-11:59am'),
('Wednesday AfterNoon 2:00pm-4:00pm','Wednesday AfterNoon 2:00pm-4:00pm'),
('Wednesday Everning 5:00pm-7:00pm','Wednesday Everning 5:00pm-7:00pm'),
('Wednesday Night 8:00pm-10:00pm','Wednesday Night 8:00pm-10:00pm'),
('Wednesday 10:00pm-6:00am','Wednesday 10:00pm-6:00am'),
('Wednesday Available','Wednesday Available'),
('Wednesday Unavailable','Wednesday Unavailable'),
)


thursdays_available=(
('Thursday Morning 6:00am-8:00am','Thursday Morning 6:00am-8:00am'),
('Thursday Morning 8:00am-10:00am','Thursday Morning8:00am-10:00am'),
('Thursday Morning 10:00am-11:59am','Thursday Morning 10:00am-11:59am'),
('Thursday Morning 6:00am-11:59am','Thursday Morning 6:00am-11:59am'),
('Thursday AfterNoon 2:00pm-4:00pm','Thursday AfterNoon 2:00pm-4:00pm'),
('Thursday Everning 5:00pm-7:00pm','Thursday Everning 5:00pm-7:00pm'),
('Thursday Night 8:00pm-10:00pm','Thursday Night 8:00pm-10:00pm'),
('Thursday 10:00pm-6:00am','Thursday 10:00pm-6:00am'),
('Thursday Available','Thursday Available'),
('Thursday Unavailable','Thursday Unavailable'),
)



fridays_available=(
('Friday Morning 6:00am-8:00am','Friday Morning 6:00am-8:00am'),
('Friday Morning 8:00am-10:00am','Friday Morning 8:00am-10:00am'),
('Friday Morning 10:00am-11:59am','Friday Morning 10:00am-11:59am'),
('Friday Morning 6:00am-11:59am','Friday Morning 6:00am-11:59am'),
('Friday AfterNoon 2:00pm-4:00pm','Friday AfterNoon 2:00pm-4:00pm'),
('Friday Everning 5:00pm-7:00pm','Friday Everning 5:00pm-7:00pm'),
('Friday Night 8:00pm-10:00pm','Friday Night 8:00pm-10:00pm'),
('Friday 10:00pm-6:00am','Friday 10:00pm-6:00am'),
('Friday Available','Friday Available'),
('Friday Unavailable','Friday Unavailable'),
)


saturdays_available=(
('Saturday Morning 6:00am-8:00am','Saturday Morning 6:00am-8:00am'),
('Saturday Morning 8:00am-10:00am','Saturday Morning 8:00am-10:00am'),
('Saturday Morning 10:00am-11:59am','Saturday Morning 10:00am-11:59am'),
('Saturday Morning 6:00am-11:59am','Saturday Morning 6:00am-11:59am'),
('Saturday AfterNoon 2:00pm-4:00pm','Saturday AfterNoon 2:00pm-4:00pm'),
('Saturday Everning 5:00pm-7:00pm','Saturday Everning 5:00pm-7:00pm'),
('Saturday Night 8:00pm-10:00pm','Saturday Night 8:00pm-10:00pm'),
('Saturday 10:00pm-6:00am','Saturday 10:00pm-6:00am'),
('Saturday Available','Saturday Available'),
('Saturday Unavailable','Saturday Unavailable'),
)


sundaysdays_available=(
('Sunday Morning 6:00am-8:00am','Sunday Morning 6:00am-8:00am'),
('Sunday Morning 8:00am-10:00am','Sunday Morning 8:00am-10:00am'),
('Sunday Morning 10:00am-11:59am','Sunday Morning 10:00am-11:59am'),
('Sunday Morning 6:00am-11:59am','Sunday Morning 10:00am-11:59am'),
('Sunday AfterNoon 2:00pm-4:00pm','Sunday AfterNoon 2:00pm-4:00pm'),
('Sunday Everning 5:00pm-7:00pm','Sunday Everning 5:00pm-7:00pm'),
('Sunday Night 8:00pm-10:00pm','Sunday Night 8:00pm-10:00pm'),
('Sunday 10:00pm-6:00am','Sunday 10:00pm-6:00am'),
('Sunday Available','Sunday Available'),
('Sunday Unavailable','Sunday Unavailable'),
)

departments=(('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Gynecology','Gynecology'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
)

class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    mondays= models.CharField(max_length=50,choices=mondays_available,default='Monday Unavailable')
    tuesdays= models.CharField(max_length=50,choices=tuesdays_available,default='Tuesday Unavailable')
    wednesdays= models.CharField(max_length=50,choices=wednesdays_available,default='Wednesday Unavailable')
    thursdays= models.CharField(max_length=50,choices=thursdays_available,default='Thursday Unavailable')
    fridays= models.CharField(max_length=50,choices=fridays_available,default='Friday Unavailable')
    saturdays= models.CharField(max_length=50,choices=saturdays_available,default='Saturday Unavailable')
    sundays= models.CharField(max_length=50,choices=sundaysdays_available,default='Sunday Unavailable')

    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department,self.mondays)
    
        



class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    symptoms = models.CharField(max_length=100,null=False)
    classification= models.CharField(max_length=50,choices=classification)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name+" ("+self.symptoms+")"





class Appointment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)




class PatientDischargeDetails(models.Model):
    id = models.AutoField(primary_key=True)
    patientId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40)
    assignedDoctorName=models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    symptoms = models.CharField(max_length=100,null=True)


    admitDate=models.DateField(null=False)
    releaseDate=models.DateField(null=False)
    daySpent=models.PositiveIntegerField(null=False)

    roomCharge=models.PositiveIntegerField(null=False)
    medicineCost=models.PositiveIntegerField(null=False)
    doctorFee=models.PositiveIntegerField(null=False)
    OtherCharge=models.PositiveIntegerField(null=False)
    total=models.PositiveIntegerField(null=False)


