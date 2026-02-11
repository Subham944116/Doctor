from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,time,timedelta
from django.core.exceptions import ValidationError
# Create your models here.

class Appointment(models.Model):
    patient=models.ForeignKey(User,
        on_delete=models.CASCADE,
        related_name="patient_appointments")
    doctor=models.ForeignKey(User,
        on_delete=models.CASCADE,
        related_name="doctor_appointments")
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def clean(self):
        from datetime import date
        
        if self.date != date.today() + timedelta(days=1):
            raise ValidationError("Appointment can only be booked for tomorrow.")
        
        if not (time(9, 0) <= self.start_time < time(13, 0)):
            raise ValidationError("Appointments allowed only between 9 AM and 1 PM.")
        
        expected_end = (
            datetime.combine(self.date, self.start_time)
            + timedelta(minutes=30)
        ).time()
        
        
        if self.end_time != expected_end:
            raise ValidationError("Appointment must be exactly 30 minutes.")
        
        
        if Appointment.objects.filter(
            doctor=self.doctor,
            date=self.date,
            start_time=self.start_time
        ).exists():
            raise ValidationError("This time slot is already booked.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.patient.username} -> {self.doctor.username} ({self.date})"