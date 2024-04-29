from django.contrib import admin
from .models import Doctor,Patient,Appointment,PatientDischargeDetails
from .models import blogs, Room, Message
# Register your models here.

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(blogs)

class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)

class PatientDischargeDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatientDischargeDetails, PatientDischargeDetailsAdmin)


