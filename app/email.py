import datetime

class Email:
    def __init__(self, sender, receiver, subject, body):
        if not isinstance(subject, str):
            raise TypeError("Subject must be a string.")

        if not subject.strip():
            raise ValueError("Subject cannot be empty.")

        if not isinstance(body, str):
            raise TypeError("Body must be a string.")

        if not body.strip():
            raise ValueError("Body cannot be empty.")

        self.sender = sender
        self.receiver = receiver
        self.subject = subject.strip()
        self.body = body.strip()
        self.timestamp = datetime.datetime.now()
        self.read = False

    def mark_as_read(self):
        self.read = True


    def __str__(self):
        status = 'Read' if self.read else 'Unread'
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
