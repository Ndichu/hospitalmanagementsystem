

from django.contrib import admin
from django.urls import path, include
from hospital import views
from django.contrib.auth.views import LoginView,LogoutView

#-------------FOR ADMIN RELATED URLS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    
    path('departments', views.alldepartments_view),
    path('book-appointment', views.bookappointment_view),

    path('Receptionist', views.adminclick_view),
    path('Doctor', views.doctorclick_view),
    path('Patient', views.patientclick_view),

    path('Receptionistsignup', views.admin_signup_view,name='Receptionistsignup'),
    path('doctorsignup', views.doctor_signup_view,name='doctorsignup'),
    path('patientsignup', views.patient_signup_view),
    
    path('Receptionistlogin', LoginView.as_view(template_name='hospital/adminlogin.html')),
    path('doctorlogin', LoginView.as_view(template_name='hospital/doctorlogin.html')),
    path('patientlogin', LoginView.as_view(template_name='hospital/patientlogin.html')),


    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='hospital/index.html'),name='logout'),


    path('Receptionist-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    # search url
    path('search_patients', views.search_patients, name='search_patients'),

    # calendar url

    path('<int:year>/<str:month>/', views.admin_dashboard_view, name='doctor_calendar'),




    path('Receptionist-doctor', views.admin_doctor_view,name='admin-doctor'),
    path('Receptionist-view-doctor', views.admin_view_doctor_view,name='Receptionist-view-doctor'),
    path('delete-doctor-from-hospital/<int:pk>', views.delete_doctor_from_hospital_view,name='delete-doctor-from-hospital'),
    path('update-doctor/<int:pk>', views.update_doctor_view,name='update-doctor'),
    path('Receptionist-add-doctor', views.admin_add_doctor_view,name='admin-add-doctor'),
    path('Receptionist-approve-doctor', views.admin_approve_doctor_view,name='Receptionist-approve-doctor'),
    path('approve-doctor/<int:pk>', views.approve_doctor_view,name='approve-doctor'),
    path('reject-doctor/<int:pk>', views.reject_doctor_view,name='reject-doctor'),
    path('Receptionist-view-doctor-specialisation',views.admin_view_doctor_specialisation_view,name='admin-view-doctor-specialisation'),


    path('Receptionist-patient', views.admin_patient_view,name='admin-patient'),
    path('Receptionist-view-patient', views.admin_view_patient_view,name='Receptionist-view-patient'),
    path('doc-view-patient', views.doc_view_patient_view,name='doc-view-patient'),
    path('Receptionist-update-patient', views.admin_view_patient_view,name='admin-update-patient'),
    path('delete-patient-from-hospital/<int:pk>', views.delete_patient_from_hospital_view,name='delete-patient-from-hospital'),
    path('update-patient/<int:pk>', views.update_patient_view,name='update-patient'),
    path('doc-update-patient/<int:pk>', views.doc_update_patient_view,name='doc-update-patient'),
    path('Receptionist-add-patient', views.admin_add_patient_view,name='Receptionist-add-patient'),
    path('Receptionist-approve-patient', views.admin_approve_patient_view,name='Receptionist-approve-patient'),
    path('approve-patient/<int:pk>', views.approve_patient_view,name='approve-patient'),
    path('reject-patient/<int:pk>', views.reject_patient_view,name='reject-patient'),
    path('Receptionist-discharge-patient', views.admin_discharge_patient_view,name='admin-discharge-patient'),
    path('discharge-patient/<int:pk>', views.discharge_patient_view,name='discharge-patient'),
    path('download-pdf/<int:pk>', views.download_pdf_view,name='download-pdf'),


    path('Receptionist-appointment', views.admin_appointment_view,name='admin-appointment'),
    path('Receptionist-view-appointment', views.admin_view_appointment_view,name='Receptionist-view-appointment'),
    path('Receptionist-add-appointment', views.admin_add_appointment_view,name='admin-add-appointment'),
    path('Receptionist-approve-appointment', views.admin_approve_appointment_view,name='admin-approve-appointment'),
    path('approve-appointment/<int:pk>', views.approve_appointment_view,name='approve-appointment'),
    path('reject-appointment/<int:pk>', views.reject_appointment_view,name='reject-appointment'),
]


#---------FOR DOCTOR RELATED URLS-------------------------------------
urlpatterns +=[
    path('doctor-dashboard', views.doctor_dashboard_view,name='doctor-dashboard'),

    path('doctor-patient', views.doctor_patient_view,name='doctor-patient'),
    path('doctor-view-patient', views.doctor_view_patient_view,name='doctor-view-patient'),
    path('doctor-view-discharge-patient',views.doctor_view_discharge_patient_view,name='doctor-view-discharge-patient'),

    path('doctor-appointment', views.doctor_appointment_view,name='doctor-appointment'),
    path('doctor-view-appointment', views.doctor_view_appointment_view,name='doctor-view-appointment'),
    path('doctor-delete-appointment',views.doctor_delete_appointment_view,name='doctor-delete-appointment'),
    path('delete-appointment/<int:pk>', views.delete_appointment_view,name='delete-appointment'),
]




#---------FOR PATIENT RELATED URLS-------------------------------------
urlpatterns +=[

    path('patient-dashboard', views.patient_dashboard_view,name='patient-dashboard'),
    path('patient-appointment', views.patient_appointment_view,name='patient-appointment'),
    path('patient-book-appointment', views.patient_book_appointment_view,name='patient-book-appointment'),
    path('patient-view-appointment', views.patient_view_appointment_view,name='patient-view-appointment'),
    path('patient-discharge', views.patient_discharge_view,name='patient-discharge'),

]
