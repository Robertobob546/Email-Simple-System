from app.inbox import Inbox
from app.email import Email

class User:
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()

    def send_email(self, receiver, subject, body):
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)
        return email

    def check_inbox(self):
        return self.inbox.list_emails()

    def read_email(self, index):
        return self.inbox.read_email(index)

    def delete_email(self, index):
        return self.inbox.delete_email(index)
