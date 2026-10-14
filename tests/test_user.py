from app.email import Email
from app.user import User
from app.inbox import Inbox

def test_user_initialization():
    user = User("Alice")

    assert user.name == "Alice"
    assert isinstance(user.inbox, Inbox)

def test_user_send_email_adds_email_to_receiver_inbox():
    sender = User("Alice")
    receiver = User("Bob")

    sender.send_email(receiver, "Test Subject", "Test Body")

    assert len(receiver.inbox.emails) == 1
    email = receiver.inbox.emails[0]

    assert email.sender == sender
    assert email.receiver == receiver
    assert email.subject == "Test Subject"
    assert email.body == "Test Body"


def test_user_reads_email_marks_email_as_read():
    sender = User("Alice")
    receiver = User("Bob")
    email = Email(sender, receiver, "Test Subject", "Test Body")
    receiver.inbox.receive_email(email)
    
    receiver.read_email(1)

    assert receiver.inbox.emails[0].read is True


def test_user_deletes_email_removes_email_from_inbox():
    sender = User("Alice")
    receiver = User("Bob")
    email = Email(sender, receiver, "Test Subject", "Test Body")
    receiver.inbox.receive_email(email)

    receiver.delete_email(1)

    assert len(receiver.inbox.emails) == 0