class Notification:
    def send(self, message):
        print("Notification:", message)


class EmailNotification(Notification):
    def send(self, message):
        print("Sending Email:", message)


class SMSNotification(Notification):
    def send(self, message):
        print("Sending SMS:", message)


n1 = EmailNotification()
n2 = SMSNotification()

n1.send("Your order is confirmed")
n2.send("Your order is confirmed")