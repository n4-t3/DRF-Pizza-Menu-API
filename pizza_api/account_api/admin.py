from django.contrib import admin
from .models import User,Order
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email"
    )


admin.site.register(User)
admin.site.register(Order)
