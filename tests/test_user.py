from app.email import Email
from app.user import User
from app.inbox import Inbox

import pytest

def test_user_initialization():
    user = User("Alice")

    assert user.name == "Alice"
    assert isinstance(user.inbox, Inbox)

def test_user_send_email_adds_email_to_receiver_inbox():
    sender = User("Alice")
    receiver = User("Bob")

    sent_email = sender.send_email(receiver, "Test Subject", "Test Body")

    assert len(receiver.inbox.emails) == 1
    

    assert sent_email.sender == sender
    assert sent_email.receiver == receiver
    assert sent_email.subject == "Test Subject"
    assert sent_email.body == "Test Body"


def test_user_reads_email_marks_email_as_read():
    sender = User("Alice")
    receiver = User("Bob")
    email = Email(sender, receiver, "Test Subject", "Test Body")
    receiver.inbox.receive_email(email)

    returned_email = receiver.read_email(1)

    assert returned_email.read is True
    assert returned_email == email


def test_user_deletes_email_removes_email_from_inbox():
    sender = User("Alice")
    receiver = User("Bob")
    email = Email(sender, receiver, "Test Subject", "Test Body")
    receiver.inbox.receive_email(email)

    deleted_email = receiver.delete_email(1)

    assert len(receiver.inbox.emails) == 0
    assert deleted_email == email

def test_user_check_inbox_returns_emails():
    sender = User("Alice")
    receiver = User("Bob")
    email = Email(sender, receiver, "Test Subject", "Test Body")
    receiver.inbox.receive_email(email)

    emails = receiver.check_inbox()

    assert len(emails) == 1
    assert emails[0] == email