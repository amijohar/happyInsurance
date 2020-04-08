from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Users(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Contact_num = models.IntegerField(null=False)
    Address = models.CharField(max_length=50, null=False)
    ID_proof = models.CharField(max_length=25)
    Address_proof = models.CharField(max_length=25)

    def __str__(self): 
         return self.user.username

class Packages(models.Model):

    package_id = models.AutoField(primary_key=True)
    base_amt = models.FloatField(null=False)
    package_type = models.CharField(max_length=10, null=False)

    def __str__(self): 
         return self.package_type



class Services(models.Model):

    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length = 50)
    package_id = models.ForeignKey(Packages,on_delete=models.CASCADE)

    def __str__(self): 
         return self.service_name


class Hospitals(models.Model):

    hospital_id = models.AutoField(primary_key=True)
    hospital_name = models.CharField(max_length=20)
    package_id = models.ForeignKey(Packages,on_delete=models.CASCADE)

class Diseases(models.Model):

    disease_id = models.AutoField(primary_key=True)
    disease_name = models.CharField(max_length=20)
    service_id = models.ForeignKey(Services,on_delete=models.CASCADE)

class Medical_history(models.Model):

    user_id = models.ForeignKey(Users,null=False,on_delete=models.CASCADE)
    disease_id = models.ForeignKey(Diseases,null=False,on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user_id','disease_id'),)

class Claim_History(models.Model):

    user_id = models.ForeignKey(Users,null=False,on_delete=models.CASCADE)
    service_id = models.ForeignKey(Services,on_delete=models.CASCADE)
    claim_amount = models.IntegerField(null=False)
    status = models.BooleanField(null=False)


class Financial_History(models.Model):

    user_id = models.ForeignKey(Users,null=False,on_delete=models.CASCADE)
    monthly_income = models.FloatField(null=False)
    monthly_expenses = models.FloatField(null=False)
    bank_statement = models.CharField(null=False,max_length=20)

class Purchase_details(models.Model):

    user_id = models.ForeignKey(Users,null=False,on_delete=models.CASCADE)
    package_id = models.ForeignKey(Packages,on_delete=models.CASCADE)
    premium_amount = models.FloatField(null=False)
    date = models.DateField(null=False,auto_now_add=True)



