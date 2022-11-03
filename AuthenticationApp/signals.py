

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from TitasPipelineGIS.email_send import Util

@receiver(user_logged_in)
def login_success(sender,request,user, **kwargs):

    print('user:',user)
    email = 'bappi142434@gmail.com'
    subject = 'User Login Alert'
    email_body = f"A user has been log in"

    try:
        data = {'email_body': email_body, 'to_email': email,'email_subject':subject}
        Util.send_email(data)
        print('email send done')
        
    except:
        pass

# user_logged_in.connect(login_success,sender=User)