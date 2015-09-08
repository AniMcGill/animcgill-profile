from django.contrib import admin
from aniprofile.models import Exec, OfficeHours, Profile
# Register your models here.


class OfficeHoursInline(admin.TabularInline):
    model = OfficeHours


@admin.register(Exec)
class ExecAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'active')
    list_filter = ('active', 'position', 'user__is_staff')
    fields = ('user', ('position', 'active'), 'about')
    inlines = [OfficeHoursInline, ]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'id__is_staff', 'steam_account')
    list_filter = ('id__is_staff')

