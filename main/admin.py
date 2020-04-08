from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Users)
admin.site.register(Services)
admin.site.register(Packages)
admin.site.register(Hospitals)
admin.site.register(Medical_history)
admin.site.register(Financial_History)
admin.site.register(Purchase_details)
admin.site.register(Claim_History)
admin.site.register(Diseases)