from django.shortcuts import render,redirect
import requests
from django.http import HttpResponse
from index import models
from .models import Patients
from .models import Donator
from .models import Donator_success
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import User_type
from .models import Doctors
from .models import Appointment
from .models import Online_consultation
from .models import Diseases # importing diseases database to fetch datas
from django.contrib import messages
from sklearn.svm import SVC
# importing libaries
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.metrics import accuracy_score
from django.contrib.auth.decorators import login_required
from datetime import date

 #redirect when user is not logged in
# Create your views here
def index(request):
    doctors=Doctors.objects.all()
    all=User_type.objects.all()
    for user in doctors:
        for i in all:
            if i.email==user.email:
                doctor=User_type.objects.filter(user_type='doctor')
    return render(request,'index.html',{'doctor':doctor})
def register(request):
    return render(request,'register.html')
def signup(request):
    return render(request,'signup.html')

def handle_signup(request):
    if request.method=="POST":
        username=request.POST['username']
        name =request.POST['name']
        age = request.POST["age"]
        gender = request.POST["gender"]
        address = request.POST['address']
        email= request.POST['email']
        password= request.POST['password']
        if User.objects.filter(email=email).exists():
            messages.error(request, 'email already exists,try another email address')
            return redirect('signup')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'username should be unique , try another')
            return redirect('signup')
        elif (len(str(password)) < 4):
            messages.error(request, 'please enter strong password')
            return redirect('signup')
        else:
            patient=User.objects.create_user(username,email,password)
            patient.save()
            patient_details=Patients(name=name,age=age,gender=gender,address=address,email=email,password=password)
            patient_details.save()
            user_type='user'
            store_user_type=User_type(user_type=user_type,username=username,email=email)
            store_user_type.save()
            messages.success(request,'Your accounts has been created successfully')
            return redirect('index')
    else:
        return HttpResponse("404- page not found error")
def handle_signin(request):
    if request.method=="POST":
        email=request.POST['email']  # for email based login we take email as username
        password=request.POST['password']
        #authenticating user login from contrib.auth
        user=authenticate(request,username=email,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,'successfully loged in')
            return redirect('index')
        else:
            messages.error(request,'invalid credentials')
            return redirect('index')
    else:
        HttpResponse("404- page not found error")
@login_required(login_url='register')
def heart_disease_inputs(request):
    return render(request,'heart_disease_form.html')
def heart_predict(request):
    # loading dataset for heart disease predictions
    heart_data=pd.read_csv(r"C:\Users\Sushil\Desktop\predict_system\index\heart_disease.csv")
    heart_data=heart_data.drop("oldpeak",axis=1)
    #train test splitchronic
    X=heart_data.drop('target',axis=1)
    Y=heart_data['target']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
    model=LogisticRegression()
    model.fit(X_train,Y_train)
    age=float(request.GET['age'])
    sex=float(request.GET['sex'])
    typical_angina=float(request.GET['typical_angina'])
    resting_blood_pressure=float(request.GET['resting_blood_pressure'])
    cholestoral=float(request.GET['cholestoral'])
    fasting_blood_sugar=float(request.GET['fasting_blood_sugar'])
    electrocardiographic_results=float(request.GET['electrocardiographic_results'])
    heart_rate_maximum=float(request.GET['heart_rate_maximum'])
    induced_angina=float(request.GET['induced_angina'])
    st_segment=float(request.GET['st_segment'])
    major_vessels=float(request.GET['major_vessels'])
    thal=float(request.GET['thal'])
    pred=model.predict([[age,sex,typical_angina,resting_blood_pressure,cholestoral,fasting_blood_sugar,electrocardiographic_results,
                         heart_rate_maximum,induced_angina,st_segment,major_vessels,thal]])
    result=''
    if pred==[1]:
        result='Possitive'
    else:
        result='Negetive'
    return render(request,'heart_disease_form.html',{"result":result})

def handle_logout(request):
    logout(request)
    messages.success(request,'you have been successfully logged out')
    return redirect('index')
@login_required(login_url='register')
def diabetes(request):
    return render(request,'/diabetes.html')
def predict_diabetes(request):
    # loading dataset
    diabetis_data = pd.read_csv(r'diabetes.csv')
    # train test split
    X = diabetis_data.drop("Outcome", axis=1)
    Y = diabetis_data['Outcome']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
    model = LogisticRegression()
    model.fit(X_train, Y_train)
    accuracy = accuracy_score(X_test, Y_test)
    pregnencies=float(request.GET['pregnencies'])
    glucose=float(request.GET['glucose'])
    blood_pressure=float(request.GET['blood_pressure'])
    skin_thickness=float(request.GET['skin_thickness'])
    insulin=float(request.GET['insulin'])
    bmi=float(request.GET['bmi'])
    diabetes_predegree_function=float(request.GET['diabetes_predegree_function'])
    age=float(request.GET['age'])
    pred=model.predict([[pregnencies,glucose,blood_pressure,skin_thickness,insulin,bmi,diabetes_predegree_function,age]])
    result1=''
    if pred==[1]:
        result1='Possitive'
    else:
        result1='Negetive'
    return render(request,'diabetes.html',{"result":result1})

@login_required(login_url='register')
def kidney_disease(request):
    return render(request,'chronic.html')
def kidney_predict(request):
    #reading dataset using pandas
    chronic_data = pd.read_csv(r'C:\Users\Sushil\Desktop\predict_system\index\kidney_disease.csv')

    #data cleaning using pandas
    #droping less correlated values
    chronic_data.drop('id', axis=1, inplace=True)
    chronic_data.drop(['pot', 'cad', 'bgr', 'ba', 'ane', 'pcc'], axis=1, inplace=True)
    chronic_data.drop(['pcv', 'appet'], inplace=True, axis=1)
    chronic_data.dropna(axis=0, inplace=True)
    #changing data to numeric values
    chronic_data[['htn', 'dm','pe',]] = chronic_data[['htn', 'dm','pe']].replace(
        to_replace={'yes': 1, 'no': 0})
    chronic_data[['rbc', 'pc']] = chronic_data[['rbc', 'pc']].replace(to_replace={'abnormal': 1, 'normal': 0})
    chronic_data['classification'] = chronic_data['classification'].replace(
        to_replace={'ckd': 1.0, 'ckd\t': 1.0, 'notckd': 0.0, 'no': 0.0})
    chronic_data.rename({'classification': 'target'}, axis=1, inplace=True)

    # spliting train and test data
    X = chronic_data.drop('target', axis=1)
    Y = chronic_data['target']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    # training our model
    model = LogisticRegression()
    model.fit(X_train, Y_train)
    #loading data from form
    age=float(request.GET['age'])
    bp=float(request.GET['bp'])
    sg=float(request.GET['sg'])
    al=float(request.GET['al'])
    su=float(request.GET['su'])
    rbc=float(request.GET['rbc'])
    pc=float(request.GET['pc'])
    bu=float(request.GET['bu'])
    sc=float(request.GET['sc'])
    sod=float(request.GET['sc'])
    hemo=float(request.GET['hemo'])
    wc=float(request.GET['wc'])
    rc=float(request.GET['rc'])
    htn=float(request.GET['htn'])
    dm=float(request.GET['dm'])
    pe=float(request.GET['pe'])
    #making predictions
    pred=model.predict([[age,bp,sg,al,su,rbc,pc,bu,sc,sod,hemo,wc,rc,htn,dm,pe]])
    result=''
    if pred==[1]:
        result='Possitive'
    else:
        result='Negetive'
    return render(request,'chronic.html',{"result":result})
@login_required(login_url='register')
def symptoms_disease(request):
    return render(request,'symptoms_predict.html')
#defining views to handle prediction from symptoms
def predict_using_symptoms(request):
  #readig dataset using pandas
  df=pd.read_csv(r'C:\Users\Sushil\Desktop\predict_system\index\training.csv')
  df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
  'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
  'Migraine':11,'Cervical spondylosis':12,
  'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
  'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
  'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
  'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
  '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
  'Impetigo':40}},inplace=True)
  l1=['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition'
   ,'spotting_ urination','fatigue','weight_gain','anxiety','cold_hands_and_feets','weight_loss','restlessness','lethargy','patches_in_throat','irregular_sugar_level','cough','high_fever','sunken_eyes'
   ,'breathlessness','sweating','dehydration','indigestion','headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever'
   ,'yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation','redness_of_eyes','sinus_pressure','runny_nose'
   ,'congestion','chest_pain','weakness_in_limbs','fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs','swollen_blood_vessels'
   ,'puffy_face_and_eyes','enlarged_thyroid','brittle_nails','swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints','movement_stiffness'
   ,'spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side','loss_of_smell','bladder_discomfort','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)','depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body'
   ,'belly_pain','abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf'
   ,'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling','silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']
  #list of disease
  disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']
  #spliting training and testing datas
  X= df[l1]
  Y = df[["prognosis"]]
  Y=np.ravel(Y)
  X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)

  l2=[]
  for x in range(0,len(l1)):
    l2.append(0)
  #taking entered symptoms from the form
  symptom1=request.GET['symptom1']
  symptom2=request.GET['symptom2']
  symptom3=request.GET['symptom3']
  symptom4=request.GET['symptom4']
  symptom5=request.GET['symptom5']


  # list of entered symptoms
  symptoms=[symptom1,symptom2,symptom3,symptom4,symptom5]
  for i in range(len(symptoms)): 
        for i1 in range(len(symptoms)): 
            if i != i1: 
                if symptoms[i] == symptoms[i1]:
                    messages.error(request,'Please select different symptom for each options')
                    return redirect('index')
                else:
                  #making empty list with all elements 0 with the same lenght as the list of disease
                  for k in range(0,len(l1)):
                    for z in symptoms:
                        if(z==l1[k]):
                            l2[k]=1

                  inputed_symptoms=[l2]
                  # using algorithm random forest to train model and make predictions
                  from sklearn.ensemble import RandomForestClassifier
                  clf = RandomForestClassifier()
                  clf = clf.fit(X_train,Y_train)

                    # calculating accuracy-------------------------------------------------------------------
                  Y_pred=clf.predict(inputed_symptoms)
                  # accuracy=accuracy_score(Y_test, Y_pred)
                  if Y_pred is None:
                    messages.warning(request,'No disease found according to your symptoms, try different symptoms')
                    return redirect('index')
                  else:
                    result=int(Y_pred)
                    output_final=disease[result]
                    return render(request,'symptoms_predict.html',{'Y_pred':output_final})
                  



def search(request):
  search=request.GET['search']
  search_result0=Patient.objects.filter(name__icontains=search)
  search_result1=Doctors.objects.filter(name__icontains=search)
  search_result2=Doctors.objects.filter(qualification__icontains=search)
  search_result3=Doctors.objects.filter(discription__icontains=search)
  search_result4=Diseases.objects.filter(name__icontains=search)
  search_result5=Diseases.objects.filter(preventive_measures__icontains=search)
  search_result6=Diseases.objects.filter(symptoms__icontains=search)
  search_result7=Diseases.objects.filter(causes__icontains=search)
  search_result8=Diseases.objects.filter(discription__icontains=search)
  search_result=set()
  search_result=search_result.union(search_result1,search_result2,search_result3,search_result4,search_result5,search_result6,search_result7,search_result8)
  params={'search_result':search_result,'search':search}
  return render(request,'search_result.html',params)
def doctors(request):
  doctors=Doctors.objects.all()
  return render(request,'doctors.html',{'doctors':doctors})

def diseases(request):
  diseases=Diseases.objects.all()
  return render(request,'diseases.html',{'diseases':diseases})# to display the disease details

def donators_details(request):
  return render(request,'donators_details.html')

def donators_data(request):
  name=request.GET['name']
  address=request.GET['address']
  email=request.GET['email']
  amounts=request.GET['amounts']
  comment=request.GET['comment']
  donator_details=Donator(name=name,address=address,email=email,amounts=amounts,comment=comment)
  donator_details.save()
  amount=Donator.objects.last()
  amount=int(amount.amounts)
  return render(request,'esewa-request.html',{'amount':amount})

def esewa_verify(request):
  amount=request.GET.get('amt')
  import xml.etree.ElementTree as ET
  donator=Donator.objects.last() #getting all last datas from database donator

  url ="https://uat.esewa.com.np/epay/transrec"
  d = {
      'amt': '{{amount}}',
      'scd': 'EPAYTEST',
      'rid': '000AE01',
      'pid':'{{donator.name}}',
  }
  resp = requests.post(url, d)
  root= ET.fromstring(resp.content)
  status=root[0].text.strip()
  if status =='Success':
    payment_status='Success'
    amount=donator.amounts
    name=donator.name
    details=Donator_success(name=name,amount=amount,payment_status=payment_status)
    details.save()
    messages.success(request,'Transaction succefull, Thanks for supporting us')
    return redirect('index')
  else:
    payment_status='failed'
    name=donator.name
    amount=donator.amounts
    details=Donator_success(name=name,amount=amount,payment_status=payment_status)
    details.save()
    messages.error(request,'Transaction failed , Try again')
    return redirect('index')
    
# <........appoint part here...>
def appointment(request):
  doctors=Doctors.objects.all()
  return render(request,'appointment.html',{'doctors':doctors})

def handle_appointment(request):

    patient_name=request.GET['patient_name']
    email=request.GET['email']
    phone=request.GET['phone']
    address=request.GET['address']
    appointment_date=request.GET['date']
    time=request.GET['time']
    gender=request.GET['gender']
    doctor_name=request.GET['doctor_name']
    message=request.GET['message']
    #validating date for avoiding invalid date inputs
    from datetime import datetime
    appointment_date = datetime.strptime(appointment_date, "%Y-%m-%d")
    present = datetime.now()
    if(appointment_date.date() < present.date()):
        messages.warning(request,'Please Enter valid Dates')
        return redirect('appointment')
    elif Appointment.objects.filter(doctor_name=doctor_name).exists() and Appointment.objects.filter(appointment_date=appointment_date).exists() and Appointment.objects.filter(time=time).exists():
        messages.error(request,'Sorry, Appointment are already booked for that Date and Time, Change Your Time')
        return redirect('appointment')
    else:
        appointment_details=Appointment(patient_name=patient_name,email=email,phone=phone,address=address,appointment_date=appointment_date,time=time,gender=gender,doctor_name=doctor_name,message=message)
        appointment_details.save()
        messages.success(request,'Your Appointments is Booked , Successfully')
        return redirect('index')
# <!..................end of Book appointment...........>

#.........code for online consultation...............
def online_consultation(request):
    doctors = Doctors.objects.all()
    return render(request,'online_consultation.html',{'doctors':doctors})

def handle_consultation(request):
    patient_name = request.GET['patient_name']
    email = request.GET['email']
    phone = request.GET['phone']
    address = request.GET['address']
    problem_start_date = request.GET['date']
    age = request.GET['age']
    gender = request.GET['gender']
    doctor_name = request.GET['doctor_name']
    issue = request.GET['message']
    consultation_details=Online_consultation(patient_name=patient_name,email=email,phone=phone,address=address,problem_start_date=problem_start_date,age=age,gender=gender,doctor_name=doctor_name,issue=issue)
    consultation_details.save()
    messages.success(request,'your message is sent to doctors ,you will get advice soon')
    return redirect('index')

# ........end of onliine consultation ........

#.....start of doctor login and signup ..................
def doctor_signup(request):
    return render(request,'doctors_signup.html')

def handle_doctor_signup(request):
    if request.method=='POST':
        name=request.POST['name']
        qualification=request.POST['qualification']
        specialist=request.POST['specialist']
        description = request.POST['description']
        username = request.POST['username']
        contact_no=request.POST['contactno']
        image=request.FILES['image']
        email=request.POST['email']
        address=request.POST['address']
        password=request.POST['password']
        if User.objects.filter(email=email).exists():
            messages.error(request, 'email already exists,try another email address')
            return redirect('index')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'username should be unique , try another')
            return redirect('index')
        elif (len(str(password)) < 4):
            messages.error(request, 'please enter strong password')
            return redirect('index')
        else:
            doctors_data=Doctors(name=name,qualification=qualification,specialist=specialist,description=description,username=username,contact_no=contact_no
                                 ,image=image,email=email,address=address)
            doctors_data.save()
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            user_type='doctor'
            store_user_type=User_type(user_type=user_type,username=username,email=email)
            store_user_type.save()
            return redirect('index')



def doctor_login(request):
    return render(request,'doctors_login.html')

def handle_doctor_login(request):
    if request.method == 'POST':
        email = request.POST['email']#Get email value from form
        password = request.POST['password'] #Get password value from form
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            if user.is_authenticated and User_type.objects.filter(username=email).exists():
                return redirect('doctor_page')
            else:
                messages.error(request,'Authentication Failed')
                return redirect('index')
        else:
            # Invalid email or password. Handle as you wish
            messages.error(request,'invalid username and password')
            return redirect('index')

def doctor_page(request):
  return render(request,'doctor_page.html')

def doctor_message(request):
  doctor=Doctors.objects.get(username=request.user.username)
  name=doctor.name
  patients=Online_consultation.objects.filter(doctor_name=name)
  return render(request,'doctor_message.html',{'patients':patients})

