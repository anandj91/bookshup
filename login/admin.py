from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from login.models import UserDetails

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserDetailsInline(admin.StackedInline):
    model = UserDetails
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserDetailsInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)