from app.email import Email
from app.user import User
from app.inbox import Inbox

def test_initialize_inbox_with_empty_list():
    inbox = Inbox()

    assert inbox.emails == []

def test_receive_email_adds_email_to_inbox():
    inbox = Inbox()
    sender = User("Alice")
    receiver = User("Bob")
    email = Email(sender, receiver, "Test Subject", "Test Body")
    inbox.receive_email(email)

    assert len(inbox.emails) == 1
    assert inbox.emails[0] == email

def test_read_email_marks_email_as_read():
    inbox = Inbox()
    sender = User("Alice")
    receiver = User("Bob")
    email = Email(sender, receiver, "Test Subject", "Test Body")
    inbox.receive_email(email)

    inbox.read_email(1)
    assert inbox.emails[0].read is True

def test_delete_email_removes_email_from_inbox():
    inbox = Inbox()
    sender = User("Alice")
    receiver = User("Bob")
    email = Email(sender, receiver, "Test Subject", "Test Body")
    inbox.receive_email(email)

    inbox.delete_email(1)

    assert len(inbox.emails) == 0
