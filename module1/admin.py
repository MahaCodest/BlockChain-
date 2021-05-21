from django.contrib import admin
from .models import register
from .models import login
from .models import Upload

admin.site.register(register)
admin.site.register(login)
admin.site.register(Upload)


