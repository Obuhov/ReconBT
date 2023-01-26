from handlers import Bot

if __name__ == '__main__':
    # создание и запуск бота
    bot = Bot()

    # отправка сообщения
    bot.send_message(message_text="hello world")