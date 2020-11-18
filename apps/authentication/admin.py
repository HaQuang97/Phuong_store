from django.contrib import admin

# Register your models here.
from apps.authentication.models import *

# user
admin.site.register(User)
admin.site.register(Token)
