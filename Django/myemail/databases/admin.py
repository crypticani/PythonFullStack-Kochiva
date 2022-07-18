from django.contrib import admin
from databases.models import EmailModel, Header, Footer

# Register your models here.
admin.site.register(EmailModel)
admin.site.register(Header)
admin.site.register(Footer)
