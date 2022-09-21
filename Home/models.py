from django.db import models


# Create your models here.

class Contact(models.Model):
    Sno = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=100, default="", )
    Passout_year = models.IntegerField(null=True)
    company_name = models.CharField(max_length=100, default="", )
    job_role = models.CharField(max_length=100, default="", )
    linkedin_id = models.URLField(max_length=100, default="", )