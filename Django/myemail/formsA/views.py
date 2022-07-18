from smtplib import SMTPServerDisconnected
# from django.forms import ValidationError
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage,BadHeaderError
from formsA.forms import ContactForm
from myemail.settings import EMAIL_HOST_USER
from django.contrib import messages


# Create your views here.
def EmailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            cc = form.cleaned_data['cc']
            bcc = form.cleaned_data['bcc']
            message = form.cleaned_data['message']
            uploaded_file = ""
            if 'file' in request.FILES:
                uploaded_file = request.FILES['file']
                if uploaded_file.size > 1048576:
                    messages.error(request,'File Size should be less than 1 MB')
                    return render(request, "form.html", {'form': form})
                    # raise ValidationError(('File Size should be less than 1 MB'), code='invalid')
                    
            try:
                # send_mail(subject, message, EMAIL_HOST_USER, [email], fail_silently=False)
                mail = EmailMessage(subject, message, EMAIL_HOST_USER, [email], cc=[cc], bcc=[bcc])
                if uploaded_file:
                    mail.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)
                mail.send()

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            except SMTPServerDisconnected as e:
                return HttpResponse(e)
            # except:
            #     return HttpResponse("Sorry! Mail could not be sent.")
            return HttpResponse('Success! Thank you for your message.')
    return render(request, "form.html", {'form': form})   

