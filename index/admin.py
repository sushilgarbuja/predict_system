from django.contrib import admin
from .models import Patients
from .models import Doctors
from .models import Diseases
from .models import Donator
from .models import Donator_success
from .models import Appointment
from.models import Online_consultation
from .models import User_type

# Register your models here.
admin.site.register(Patients)
admin.site.register(Doctors)
admin.site.register(Diseases)# register Diseases database table in admin site
admin.site.register(Donator)
admin.site.register(Donator_success)
admin.site.register(Appointment)
admin.site.register(Online_consultation)
admin.site.register(User_type)