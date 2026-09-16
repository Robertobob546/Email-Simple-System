# Python Email System

A simple email management system built in Python using Object-Oriented Programming concepts.

This project was developed as a practice exercise to reinforce Python fundamentals and OOP concepts such as classes, objects, composition, methods, and special methods.

## Features

- Create users
- Send emails between users
- Store received emails in an inbox
- List received emails
- Read full email content
- Mark emails as read
- Delete emails
- Track email creation time
- Display read/unread status

## Technologies

- Python 3
- `datetime` module

## Object-Oriented Programming Concepts

This project uses three main classes:

### `Email`

Represents an email message.

Each email contains:

- Sender
- Receiver
- Subject
- Body
- Timestamp
- Read/unread status

The class also provides methods to:

- Mark an email as read
- Display the full email
- Format the email preview using `__str__`

### `User`

Represents a user of the email system.

A user can:

- Send emails
- Check their inbox
- Read emails
- Delete emails

Each user has their own `Inbox`.

### `Inbox`

Stores and manages received emails.

The inbox can:

- Receive emails
- List emails
- Read a specific email
- Delete a specific email
- Validate email indexes

## Example

```python
tory = User('Tory')
ramy = User('Ramy')

tory.send_email(
    ramy,
    'Hello',
    'Hi Ramy, just saying hello!'
)

ramy.send_email(
    tory,
    'Re: Hello',
    'Hi Tory, hope you are fine.'
)

ramy.check_inbox()
ramy.read_email(1)
ramy.delete_email(1)