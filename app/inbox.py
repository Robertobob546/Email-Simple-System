class Inbox:
    def __init__(self):
        self.emails = []

    def receive_email(self, email):
        self.emails.append(email)

    def list_emails(self):
        if not self.emails:
            raise ValueError('Inbox is empty.')
        
        return self.emails

    def read_email(self, index):
        if not self.emails:
            raise ValueError('Inbox is empty.')
            
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            raise IndexError('Invalid email number.')

        email = self.emails[actual_index]
        email.mark_as_read()

        return email

    def delete_email(self, index):
        if not self.emails:
            raise ValueError('Inbox is empty.')
            
        actual_index = index - 1

        if actual_index < 0 or actual_index >= len(self.emails):
            raise IndexError('Invalid email number.')
            
        return self.emails.pop(actual_index)
        