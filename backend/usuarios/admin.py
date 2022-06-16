from django.contrib import admin
#from django.contrib.auth.admin import User as Ba
from  .models import User

# Register your models here.
admin.site.register(User)