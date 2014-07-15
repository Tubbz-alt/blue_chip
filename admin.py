from django.contrib import admin
from blue_chip.models import NewBusiness

class NewBusinessAdmin(admin.ModelAdmin):
    pass

admin.site.register(NewBusiness, NewBusinessAdmin)
