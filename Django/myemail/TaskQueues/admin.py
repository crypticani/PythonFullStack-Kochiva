from django.contrib import admin
from TaskQueues.models import EmailModel, Header, Footer

# Register your models here.
class EmailAdmin(admin.ModelAdmin):
    list_display = ['email_to', 'subject', 'status']
    list_filter = ['created_at', 'sent_at']

admin.site.register(EmailModel, EmailAdmin)
admin.site.register(Header)
admin.site.register(Footer)
