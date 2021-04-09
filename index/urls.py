from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('register/',views.register,name='register'),
    path('signup/', views.signup, name='signup'),
    path('handle_signup',views.handle_signup,name='handle_signup'),
    path('handle_signin',views.handle_signin,name='handle_signin'),
    path("heart_disease_inputs",views.heart_disease_inputs, name='heart_disease_inputs'),
    path('heart_predict',views.heart_predict,name='heart_predict'),
    path('handle_logout',views.handle_logout,name='handle_logout'),
    path('diabetes',views.diabetes,name='diabetes'),
    path('predict_diabetes',views.predict_diabetes,name='predict_diabetes'),
    path('kidney_disease',views.kidney_disease,name='kidney_disease'),
    path('kidney_predict',views.kidney_predict,name='kidney_predict'),
    path('symptoms_disease',views.symptoms_disease,name='symptoms_disease'),
    path('predict_using_symptoms',views.predict_using_symptoms,name='predict_using_symptoms'),#defining path to handle predictions using symptoms
    path('search',views.search,name='search'),
    path('doctors',views.doctors,name='doctors'),
    path('diseases',views.diseases,name='diseases'),
    path('donators_details',views.donators_details,name='donators_details'),
    path('donators_data',views.donators_data,name='donators_data'),
    path('esewa_verify',views.esewa_verify,name='esewa_verify'),
    path('appointment',views.appointment,name='appointment'),
    path('handle_appointment',views.handle_appointment,name='handle_appointment'),
    path('online_consultation',views.online_consultation,name='online_consultation'),
    path('handle_consultation',views.handle_consultation,name='handle_consultation'),
    path('doctor_login/',views.doctor_login,name='doctor_login'),
    path('doctor_login/handle_doctor_login',views.handle_doctor_login,name='handle_doctor_login'),
    path('doctor_login/doctor_signup',views.doctor_signup,name='doctor_signup'),
    path('doctor_login/handle_doctor_signup',views.handle_doctor_signup,name='handle_doctor_signup'),
    path('doctor_page',views.doctor_page,name='doctor_page'),
    path('doctor_message',views.doctor_message,name='doctor_message'),
    # path('doctor_appointments',views.doctor_appointments,name='doctor_appointments'),
    # path('doctor_profile',views.doctor_profile,name=doctor_profile)
    ]