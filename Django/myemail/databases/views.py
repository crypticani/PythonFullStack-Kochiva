from email import header
from smtplib import SMTPServerDisconnected
# from django.forms import ValidationError
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage, BadHeaderError, EmailMultiAlternatives
from databases.forms import ContactForm
from myemail.settings import EMAIL_HOST_USER
from django.contrib import messages
from databases.models import EmailModel
from django.template.loader import render_to_string


# Create your views here.
def EmailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email_to = form.cleaned_data['email_to']
            cc = form.cleaned_data['cc']
            bcc = form.cleaned_data['bcc']
            message = form.cleaned_data['message']
            header = form.cleaned_data['header']
            footer = form.cleaned_data['footer']
            uploaded_file = ""
            if 'file' in request.FILES:
                uploaded_file = request.FILES['file']
                if uploaded_file.size > 1048576:
                    messages.error(
                        request, 'File Size should be less than 1 MB')
                    return render(request, "form.html", {'form': form})
                    # raise ValidationError(('File Size should be less than 1 MB'), code='invalid')
            db_obj = EmailModel()
            db_obj.subject = subject
            db_obj.email_to = email_to
            db_obj.cc = cc
            db_obj.bcc = bcc
            db_obj.message = message
            db_obj.file = uploaded_file
            db_obj.header = header
            db_obj.footer = footer
            db_obj.save()
        
            try:
                # send_mail(subject, message, EMAIL_HOST_USER, [email], fail_silently=False)
                hdr = ""
                ftr = ""
                if header is not None:
                    hdr = "<br />".join(header.content.split("\n"))
                if footer is not None:
                    ftr = "<br />".join(footer.content.split("\n"))
                context = {
                    'message': "<br />".join(message.split("\n")),
                    'header': hdr,
                    'footer': ftr
                }
                # print(message.replace("\\r\\n", "<br/>"))
                html_message = render_to_string('email_template.html', context)
                mail = EmailMessage(subject, html_message, EMAIL_HOST_USER, [email_to], cc=[cc], bcc=[bcc])
                if uploaded_file:
                    mail.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)
                mail.content_subtype="html"
                mail.mixed_subtype = 'related'

                mail.send()


            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            except SMTPServerDisconnected as e:
                return HttpResponse(e)
            # except:
            #     return HttpResponse("Sorry! Mail could not be sent.")

            return HttpResponse('Success! Thank you for your message.')
            # return render(request, 'email_template.html', context)
    return render(request, "form.html", {'form': form})
