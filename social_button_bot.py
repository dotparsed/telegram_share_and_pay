import telebot
import telebot.types as types
import time

token = "*****"

bot = telebot.TeleBot(token)
share = 0

smile_letter = b'\xE2\x9C\x89'.decode('utf-8')
smile_arrow = b'\xE2\x9E\xA1'.decode('utf-8')
smile_wait = b'\xE2\x8F\xB3'.decode('utf-8')



@bot.message_handler(commands=['start'])
def send_welcome(message):
    id = message.chat.id
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Поделиться с другом " + smile_arrow, url="https://t.me/share/url?url=https://t.me/bot_name***?start=" + str(id) + "&text=список%20чатов%20по%20нетворкингу")

    url_pay = types.InlineKeyboardButton(text="Оплатить 2 руб", url='https://money.yandex.ru/quickpay/shop-widget?********')

    keyboard.add(url_button, url_pay)

    keyboard_to_me = types.InlineKeyboardMarkup()
    send_button = types.InlineKeyboardButton(text="написать мне " + smile_letter, url="https://t.me/dotparsed")
    keyboard_to_me.add(send_button)

    img = open("1.png", 'rb')
    bot.send_photo(message.chat.id, photo=img, reply_markup=keyboard_to_me)
    bot.send_message(message.chat.id, "Привет! Меня зовут Дмитрий\nя разработчик ботов на python\n\nХочу поделиться с тобой списком чатов в telegram для нетворкинга!\n")
    time.sleep(6)

    file1 = open("File1.txt", "rb")
    bot.send_document(message.chat.id, file1, caption="Список чатов telegram")
    time.sleep(6)

    bot.send_message(message.chat.id, "Поделись этим списком c другом и получи еще \n1000 чатов телеграмм и вк для нетворкинга", reply_markup=keyboard)
    time.sleep(15)

    bot.send_message(message.chat.id,"Ждем вашего друга...\n"+smile_wait)


    if len(message.text) > 8:
        share =+ 1
        print("Поделились ", share)
        bot.send_message(str(message.text).split(" ")[1], "Ваш список номер 2!")
        file2 = open("File2.txt", "rb")
        bot.send_document(str(message.text).split(" ")[1], file2, caption="Список чатов 2 telegram")


@bot.message_handler(commands=['pay'])
def send_welcome(message):
    if len(message.text) > 5:
        if str(message.text).split(" ")[1] == "0001":
            bot.send_message(message.chat.id, "Заказ оплачен!")
            bot.send_message(str(message.text).split(" ")[1], "Ваш список номер 2!")
            file2 = open("File2.txt", "rb")
            bot.send_document(str(message.text).split(" ")[1], file2, caption="Список чатов 2 telegram")

while True:
    try:
        bot.polling(none_stop=True, timeout=1)
    except:
      print('Ожидание Api telegram')
      time.sleep(10)