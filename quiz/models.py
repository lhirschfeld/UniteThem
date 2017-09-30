from django.db import models
from django.core.mail import send_mail

class Fan(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    message = models.CharField(max_length=2000)

    # Quiz Choices
    form = models.CharField(max_length=50)
    oath = models.CharField(max_length=50)
    ally = models.CharField(max_length=50)

    def sendEmail(self, address):
        send_mail('UniteThem - Fan Match Found', 'We have matched you with another fan of the Stormlight Archives. Their information is below. Please reply to this email if you have any problems - thank you!\nEmail: ' + self.message + '\nMessage: ' + self.message + '\n', 'unitethemoathbringer@gmail.com', [address])
