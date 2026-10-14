from app.user import User


def display_full_email(email):
    print('\n--- Email ---')
    print(f'From: {email.sender.name}')
    print(f'To: {email.receiver.name}')
    print(f'Subject: {email.subject}')
    print(f"Received: {email.timestamp.strftime('%Y-%m-%d %H:%M')}")
    print(f'Body: {email.body}')
    print('-------------\n')


def display_inbox(user):
    print(f"\n{user.name}'s Inbox:")

    try:
        emails = user.check_inbox()

        for i, email in enumerate(emails, start=1):
            print(f'{i}. {email}')

    except ValueError as error:
        print(error)


def main():
    tory = User('Tory')
    ramy = User('Ramy')

    # Send emails
    sent_email = tory.send_email(
        ramy,
        'Hello',
        'Hi Ramy, just saying hello!'
    )

    print(
        f'Email sent from {sent_email.sender.name} '
        f'to {sent_email.receiver.name}!'
    )

    sent_email = ramy.send_email(
        tory,
        'Re: Hello',
        'Hi Tory, hope you are fine.'
    )

    print(
        f'Email sent from {sent_email.sender.name} '
        f'to {sent_email.receiver.name}!'
    )

    # List Ramy's inbox
    display_inbox(ramy)

    # Read an email
    try:
        email = ramy.read_email(1)
        display_full_email(email)

    except (ValueError, IndexError) as error:
        print(error)

    # Delete an email
    try:
        deleted_email = ramy.delete_email(1)
        print(f'Email "{deleted_email.subject}" deleted.')

    except (ValueError, IndexError) as error:
        print(error)

    # List inbox again
    display_inbox(ramy)


if __name__ == '__main__':
    main()