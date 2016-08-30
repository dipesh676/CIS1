from django.db import models


# Create your models here.
class Criminal(models.Model):
    Name = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    ctznno = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)

    def __str__(self):
        return self.Name




class crime (models.Model):
    criminal = models.ForeignKey(Criminal, related_name='crime')
    crime_type = models.CharField(max_length=50)
    crime_desc = models.CharField(max_length=200)
    crime_date = models.DateTimeField()
    crime_addr = models.CharField(max_length=50)
    case_no = models.CharField(max_length=30, primary_key=True)


    def __str__(self):
        return self.case_no


class Victim (models.Model):
    case_no = models.ForeignKey(crime)
    victim_name = models.CharField(max_length=50)
    victim_desc = models.CharField(max_length=200)
    victim_addr = models.CharField(max_length=50)
    victim_age = models.IntegerField()

    def __str__(self):
        return self.victim_name

class FIR (models.Model):
    crime_type = models.CharField(max_length=50)
    crime_addr = models.CharField(max_length=50)
    full_report = models.CharField(max_length=200)
    reported_by = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)

    def __str__(self):
        return self.reported_by


