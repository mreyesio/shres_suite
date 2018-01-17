from django.contrib import admin
from shnc.models import AccessRecord, LpnData,UserProfileInfo,Bills
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Bills)
admin.site.register(LpnData)
admin.site.register(UserProfileInfo)