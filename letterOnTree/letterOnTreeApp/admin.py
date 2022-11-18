from django.contrib import admin
from .models import Letter
# Register your models here.

class LetterAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
admin.site.register(Letter, LetterAdmin)