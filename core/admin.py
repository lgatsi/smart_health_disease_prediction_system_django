from django.contrib import admin
from.models import User_manage,Profile,Medical,Ment

#registering models

models_list = [User_manage,Profile,Medical,Ment]
admin.site.register(models_list)
