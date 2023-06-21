from django.contrib import admin

from .models import University, FAQ


# Register your models here.


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time', 'image')
    list_display_links = ('id',)
    prepopulated_fields = {'slug': ('title',), }


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'time', 'status')
    list_display_links = ('id',)


