def send_email(mail, recipient, sender="university.help@gmail.com"):
    if mail == None:
        mail = "Пустое сообщение"
    if recipient == sender:
        return "Нельзя отправить письмо самому себе!"

    if "@" not in recipient:
        return "Не верный формат почты получателя"

    if "@" not in sender:
        return "Не верный формат почты отправителя"

    recipient_mail_sections = recipient.split(".")
    sender_mail_sections = sender.split(".")

    if len(recipient_mail_sections) > 3 or len(recipient_mail_sections) < 2 or recipient_mail_sections[-1] not in ["com", "ru", "net"]:
        return "Не верный формат почты получателя"

    if len(sender_mail_sections) > 3 or len(sender_mail_sections) < 2 or sender_mail_sections[-1] not in ["com", "ru", "net"]:
        return "Не верный формат почты отправителя"
    if sender == "university.help@gmail.com":
        print("Письмо отправлено с адреса:", sender, "\nа адрес:",
            recipient, "\nПисьмо:\n",
            "///////////////////////////////////////////\n",
            mail,
            "\n///////////////////////////////////////////")
        return "Письмо успешно отправлено!"
    else:
        print("///НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ///\nПисьмо отправлено с адреса:", sender, "\nа адрес:",
              recipient, "\nПисьмо:\n",
              "///////////////////////////////////////////\n",
              mail,
              "\n///////////////////////////////////////////")
        return "Письмо успешно отправлено!"



result = send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
print(result)
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинар
