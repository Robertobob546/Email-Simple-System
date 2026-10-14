from app.email import Email
from app.user import User
from app.inbox import Inbox

import pytest

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

    returned_email = inbox.read_email(1)

    assert inbox.emails[0].read is True
    assert returned_email == email

def test_delete_email_removes_email_from_inbox():
    inbox = Inbox()
    sender = User("Alice")
    receiver = User("Bob")
    email = Email(sender, receiver, "Test Subject", "Test Body")
    inbox.receive_email(email)

    deleted_email = inbox.delete_email(1)

    assert len(inbox.emails) == 0
    assert deleted_email == email


# Additional tests for error raises

def test_read_email_raises_value_error_for_empty_inbox():
    inbox = Inbox()

    with pytest.raises(ValueError, match='Inbox is empty.'):
        inbox.read_email(1)

def test_read_email_raises_index_error_for_invalid_index():
    inbox = Inbox()
    sender = User("Alice")
    receiver = User("Bob")
    email = Email(sender, receiver, "Test Subject", "Test Body")
    inbox.receive_email(email)

    with pytest.raises(IndexError, match='Invalid email number.'):
        inbox.read_email(2)  # Invalid index    

def test_delete_email_raises_value_error_for_empty_inbox():
    inbox = Inbox()

    with pytest.raises(ValueError, match='Inbox is empty.'):
        inbox.delete_email(1)

def test_delete_email_raises_index_error_for_invalid_index():
    inbox = Inbox()
    sender = User("Alice")
    receiver = User("Bob")
    email = Email(sender, receiver, "Test Subject", "Test Body")
    inbox.receive_email(email)

    with pytest.raises(IndexError, match='Invalid email number.'):
        inbox.delete_email(2)  # Invalid index

def test_list_emails_raises_value_error_for_empty_inbox():
    inbox = Inbox()

    with pytest.raises(ValueError, match='Inbox is empty.'):
        inbox.list_emails()

