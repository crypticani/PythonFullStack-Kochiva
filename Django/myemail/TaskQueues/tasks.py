from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from myemail.settings import EMAIL_HOST_USER


def send_mail_task(subject, email_to, cc, bcc, message, uploaded_file, header, footer):
    context = {
        'message': "<br />".join(message.split("\n")),
        'header': "<br />".join(header.content.split("\n")),
        'footer': "<br />".join(footer.content.split("\n"))
    }
     # print(message.replace("\\r\\n", "<br/>"))
    html_message = render_to_string('email_template.html', context)
    mail = EmailMessage(subject, html_message, EMAIL_HOST_USER, [email_to], cc=[cc], bcc=[bcc])
    if uploaded_file:
        mail.attach(uploaded_file.name, uploaded_file.read(),uploaded_file.content_type)
    mail.content_subtype = "html"
    mail.mixed_subtype = 'related'

    # mail.send()
