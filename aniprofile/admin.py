from django.contrib import admin
from aniprofile.models import Exec, OfficeHours, Profile
# Register your models here.

class OfficeHoursInline(admin.TabularInline):
    model = OfficeHours

@admin.register(Exec)
class ExecAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'active')
    list_filter = ('active', 'position', 'user__is_staff')
    inlines = [OfficeHoursInline,]

@admin.register(Profile)
    list_display = ('user', 'user__is_staff', 'steam_account')
    list_filter = (''user__is_staff')

