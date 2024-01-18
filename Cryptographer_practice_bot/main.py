import telebot

bot = telebot.TeleBot('6121894618:AAGAqXPFSuhceDaj2lmu2VcdQsjqy6iSs54')

def encrypt(text,key):
    encrypted_text = "Зашифрованное сообщение: "
    for i in text:
        if i.isalpha():
            shifted_i = chr(ord(i) + int(key))
            encrypted_text += shifted_i
        else:
            encrypted_text += i
    return encrypted_text

def decrypt(text,key):
    decrypted_text = "Расшифрованное сообщение: "
    for i in text:
        if i.isalpha():
            shifted_i = chr(ord(i) - int(key))
            decrypted_text += shifted_i
        else:
            decrypted_text += i
    return decrypted_text

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    text_list = message.text.split()

    if message.text == "/help":
        bot.send_message(message.from_user.id, 'Инструкция использования бота:')
        bot.send_message(message.from_user.id,'Вводим первый символ Ш или Р, далее слово для шифрования и ключ через пробел.')
        bot.send_message(message.from_user.id,'Шифрование происходит с помощью алгоритма Цезаря, каждая буква алфавита заменяется другой буквой на фиксированное количество позиций в алфавите.')
        bot.send_message(message.from_user.id,'Ключом, в свою очередь, как раз и является это фиксированное количество позиций.')

    elif message.text == '/start':
        bot.send_message(message.from_user.id,'Перед использованием ознакомся с моим функционалом с помощью команды /help')
    
    elif (text_list[0] == 'Ш') or (text_list[0] == 'Р'):
        if text_list[0] == 'Ш':
            bot.send_message(message.from_user.id, encrypt(text_list[1],text_list[2]))
        else:
            bot.send_message(message.from_user.id, decrypt(text_list[1],text_list[2]))
    else:
        bot.send_message(message.from_user.id, 'Извини, я те6я не понимаю, ознакомся с моим функционалом здесь 👉 /help')

bot.polling(none_stop=True)
