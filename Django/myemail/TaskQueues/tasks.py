from venv import create
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, BadHeaderError
from smtplib import SMTPServerDisconnected
from myemail.settings import EMAIL_HOST_USER, BASE_DIR
from TaskQueues.models import EmailModel


def send_mail_task():
    to_be_sent = EmailModel.objects.filter(status="queued")
    print(to_be_sent)
    for data in to_be_sent:
        subject = data.subject
        email_to = data.email_to
        cc = data.cc
        bcc = data.bcc
        message = data.message
        header = data.header
        footer = data.footer
        uploaded_file = data.file

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
                mail.attach_file(str(BASE_DIR)+"/media/"+str(uploaded_file.name))
            mail.content_subtype="html"
            mail.mixed_subtype = 'related'

            mail.send()

        except BadHeaderError:
            print('Invalid header found.')
        except SMTPServerDisconnected as e:
            print(e)
        # except:
        #     return HttpResponse("Sorry! Mail could not be sent.")
    to_be_sent.update(status="sent")
