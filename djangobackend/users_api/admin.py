from django.contrib import admin
from .models import AppUser, DentalProfile


# Register your models here.
class AppUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'email', 'username',)
    search_fields = ('email', 'username')

class DentalProfileAdmin(admin.ModelAdmin):
    list_display = ('test_kit_id', 'title',)
    search_fields = ('test_lit_id', 'user__email',)

admin.site.register(AppUser, AppUserAdmin)
admin.site.register(DentalProfile, DentalProfileAdmin)