from django.contrib import admin

from .models import Profiles, Contact


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1  # Number of empty contact forms to show


class ProfilesAdmin(admin.ModelAdmin):
    inlines = [ContactInline]
    list_display = ('id', 'name', 'slogan', 'img')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('profile', 'name', 'link')
    list_filter = ('profile',)


admin.site.register(Profiles, ProfilesAdmin)
