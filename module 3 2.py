def send_email(recipient, mail="Пустое сообщение", sender="myair.airlines@gmail.com"):

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

    print("От:", sender, "\nДля:",
          recipient, "\nПисьмо:\n",
          "///////////////////////////////////////////\n",
          mail,
          "\n///////////////////////////////////////////")
    return "Письмо успешно отправлено!"


result = send_email("genius.888@gmail.com", mail="Привет!")
print(result)