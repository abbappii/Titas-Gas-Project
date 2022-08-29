from django.core.mail import EmailMessage


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        email.send()


# email_body = f'Hi {user.full_name},\n' \
#                      f'Were happy you signed up for Techforing Career. To start exploring the TechForing Career Please confirm your email address. \n' \
#                      f'Verification link: {absurl}'
#
#         data = {'email_body': email_body, 'to_email': user.email,
#                 'email_subject': 'Email Verification|TechForing'}
#
#         Util.send_email(data)