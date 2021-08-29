from django.contrib import admin


from .models import ActiveData, DataTemplate, Data, Subject, Sub_Subject

admin.site.register(ActiveData)
admin.site.register(Data)
admin.site.register(DataTemplate)
admin.site.register(Subject)
admin.site.register(Sub_Subject)
# Register your models here.
