class Notification:
    def send_message(self, message):
        print("Sending notification:", message)

class EmailNotification(Notification):
    def send_message(self, message):
        print("Sending Email.")
        print("Email Message:", message)
        print("Email Sent Successfully!\n")

class SMSNotification(Notification):
    def send_message(self, message):
        print("Sending SMS.")
        print("SMS Message:", message)
        print("SMS Sent Successfully!\n")

class AppNotification(Notification):
    def send_message(self, message):
        print("Sending App Notification.")
        print("App Message:", message)
        print("Notification Sent Successfully!\n")

email = EmailNotification()
sms = SMSNotification()
app = AppNotification()
message = "Tomorrow is a holiday."

notifications = [email, sms, app]

for notify in notifications:
    notify.send_message(message)