import pyodbc


CONNECTION_STRING = (
    r"DRIVER={ODBC Driver 18 for SQL Server};"
    r"SERVER=ROBERTO\SQLEXPRESS;"
    r"DATABASE=EmailSystemDB;"
    r"Trusted_Connection=yes;"
    r"TrustServerCertificate=yes;"
)


def get_connection():
    return pyodbc.connect(CONNECTION_STRING)

def get_users():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name
        FROM users
        ORDER BY id
    """)

    users = cursor.fetchall()
    cursor.close() 
    connection.close()

    return users

def create_user(name):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO users (name) VALUES (?)",
        name
    )

    connection.commit()

    cursor.close()
    connection.close()


def get_user_by_id(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, name FROM users WHERE id = ?"
        , user_id
    )

    user = cursor.fetchone()
    cursor.close()
    connection.close()

    return user


def create_email(sender_id, receiver_id, subject, body):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """INSERT INTO emails (sender_id, receiver_id, subject, body)
        VALUES (?, ?, ?, ?)""",
        sender_id, receiver_id, subject, body
    )

    connection.commit()

    cursor.close()
    connection.close()

def get_inbox(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """SELECT e.id, sender.name AS sender,
            receiver.name AS receiver,
            e.subject,
            e.body,
            e.sent_at,
            e.is_read
            FROM emails AS e 
            JOIN users AS sender ON e.sender_id = sender.id
            JOIN users AS receiver ON e.receiver_id = receiver.id
            WHERE e.receiver_id = ?
            ORDER BY e.sent_at DESC""",
            user_id
    )
    
    emails = cursor.fetchall()
    cursor.close()
    connection.close()

    return emails


def mark_email_as_read(email_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE emails SET is_read = 1 WHERE id = ?",
        email_id
    )

    connection.commit()
    cursor.close()
    connection.close()



def delete_email(email_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM emails WHERE id = ?",
        email_id
    )

    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    # 1. Listar usuários
    print("\n--- USERS ---")

    users = get_users()

    for user in users:
        print(user.id, user.name)


    # 2. Buscar usuários por ID
    print("\n--- GET USER BY ID ---")

    sender = get_user_by_id(1)
    receiver = get_user_by_id(2)

    print("Sender:", sender.id, sender.name)
    print("Receiver:", receiver.id, receiver.name)


    # 3. Criar email
    print("\n--- CREATE EMAIL ---")

    create_email(
        sender.id,
        receiver.id,
        "Database Test",
        "This email was created from Python."
    )

    print("Email created successfully.")


    # 4. Mostrar inbox
    print("\n--- INBOX ---")

    inbox = get_inbox(receiver.id)

    for email in inbox:
        print(
            email.id,
            email.sender,
            email.receiver,
            email.subject,
            email.is_read
        )


    # O primeiro é o mais recente porque usamos:
    # ORDER BY e.sent_at DESC
    email_id = inbox[0].id


    # 5. Marcar como lido
    print("\n--- MARK AS READ ---")

    mark_email_as_read(email_id)

    inbox = get_inbox(receiver.id)

    for email in inbox:
        if email.id == email_id:
            print(
                f"Email {email.id} - is_read: {email.is_read}"
            )


    # 6. Deletar email
    print("\n--- DELETE EMAIL ---")

    delete_email(email_id)

    print(f"Email {email_id} deleted.")


    # 7. Mostrar inbox depois da exclusão
    print("\n--- INBOX AFTER DELETE ---")

    inbox = get_inbox(receiver.id)

    for email in inbox:
        print(
            email.id,
            email.sender,
            email.subject
        )