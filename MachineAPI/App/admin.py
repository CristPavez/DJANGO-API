from django.contrib import admin

from App.models import DataFrame_Model, Test, Test2

# Register your models here.
admin.site.register(Test)
admin.site.register(Test2)
admin.site.register(DataFrame_Model)