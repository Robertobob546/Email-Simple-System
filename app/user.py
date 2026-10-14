from app.inbox import Inbox
from app.email import Email

class User:
    def __init__(self, name : str):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")

        if not name.strip():
            raise ValueError("Name cannot be empty.")
        
        self.name = name.strip()
        self.inbox = Inbox()

    def send_email(self, receiver, subject, body):
        if not isinstance(receiver, User):
            raise TypeError("Receiver must be a User.")

        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)
        return email

    def check_inbox(self):
        return self.inbox.list_emails()

    def read_email(self, index):
        return self.inbox.read_email(index)

    def delete_email(self, index):
        return self.inbox.delete_email(index)
