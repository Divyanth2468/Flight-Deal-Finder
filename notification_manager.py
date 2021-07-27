import smtplib
my_email = 'divyanthsatya86@gmail.com'
password = 'Dash240608'
SHEETY_API_ENDPOINT = 'https://api.sheety.co/c82ed300dae3f4bf5d1bae411e9e3038/flightSearch/users'
# from twilio.rest import Client
# account_ssid = 'ACc74852565a8a262a1ee9e8f8d9852899'
# auth_token = 'cfdecdf26c09fd59091bdd274750f344'
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
