from app.email import Email
from app.user import User


def test_email_starts_unread():
    sender = User("Roberto")
    receiver = User("Joao")

    email = Email(
        sender=sender,
        receiver=receiver,
        subject="Hello",
        body="Hello Joao!"
    )

    assert email.read is False


def test_mark_email_as_read():
    sender = User("Roberto")
    receiver = User("Joao")

    email = Email(
        sender=sender,
        receiver=receiver,
        subject="Hello",
        body="Hello Joao!"
    )

    email.mark_as_read()

    assert email.read is True


def test_email_stores_information_correctly():
    sender = User("Roberto")
    receiver = User("Joao")

    email = Email(
        sender=sender,
        receiver=receiver,
        subject="Test Subject",
        body="Test Body"
    )

    assert email.sender == sender
    assert email.receiver == receiver
    assert email.subject == "Test Subject"
    assert email.body == "Test Body"