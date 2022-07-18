from django.db import models

# Create your models here.
class Header(models.Model):
    name = models.CharField(max_length=30)
    content = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to ='headers/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Headers"

    def __str__(self):
        return self.name

class Footer(models.Model):
    name = models.CharField(max_length=30)
    content = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to ='footers/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Footers"

    def __str__(self):
        return self.name


class EmailModel(models.Model):
    email_to = models.EmailField()
    cc = models.EmailField(blank=True, null=True)
    bcc = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=250)
    file = models.FileField(upload_to='files/')
    header = models.ForeignKey(to=Header, on_delete=models.SET_NULL, blank=True, null=True)
    footer = models.ForeignKey(to=Footer, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Emails"

    def __str__(self):
        return self.subject