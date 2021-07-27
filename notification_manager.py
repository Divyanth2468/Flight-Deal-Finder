import smtplib
import os
my_email = os.getenv("email")
password = os.getenv("password")
SHEETY_API_ENDPOINT = os.getenv("sheety_API")
# from twilio.rest import Client
# account_ssid = os.getenv("account_ssid")
# auth_token = os.getenv("auth_token")
#
#
# class NotificationManager:
#     def __init__(self):
#         self.client = Client(account_ssid, auth_token)
#
#     def send_sms(self, message):
#         sent_message = self.client.messages \
#             .create(
#                 body=message,
#                 from_='+13475149656',
#                 to='+917013918815'
#         )
#         print(sent_message)


class NotificationManager:
    def __init__(self):
        pass

    def send_email(self, message, emails, link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            for mail in emails:
                connection.sendmail(from_addr=my_email, to_addrs={mail},
                                         msg=f'Subject:New Low Price Flight\n\n {message}\n{link}'.encode('utf-8'))
