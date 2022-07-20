from django.contrib import admin
from databases.models import EmailModel, Header, Footer

# Register your models here.
class EmailAdmin(admin.ModelAdmin):
    list_display = ['email_to', 'subject']

admin.site.register(EmailModel, EmailAdmin)
admin.site.register(Header)
admin.site.register(Footer)
