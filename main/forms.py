from django.forms import ModelForm
from django import forms
from . import models



class UserForm(ModelForm):
    class Meta:
        model = models.Users
        exclude = ['user']

class MedicalHistoryForm(ModelForm):
    class Meta:
        model = models.Medical_history
        exclude = ['user_id']
    
class FinancialHistoryForm(ModelForm):
    class Meta:
        model = models.Financial_History
        exclude = ['user_id', 'bank_statement']