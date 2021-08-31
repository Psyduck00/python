from django.contrib import admin
from .models import Question, Choice, UserExtended

# Register your models here.
admin.site.register(Question)

admin.site.register(Choice)

admin.site.register(UserExtended)

