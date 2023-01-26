import vk_api  # Подключаем библиотеку Vk_Api
import os  # работа с файловой системой
from vk_api.utils import get_random_id  # использование VK API
from dotenv import load_dotenv  # загрузка переменных окружения из .env


class Bot:
    # Статус текущий сессии ВК
    vk_session = None

    # Статус доступа к APIvk
    vk_api_access = None

    # Статус авторизации
    authorized = False

    # id страницы
    main_user_id = None

    def __init__(self):
        # функция инициализации через доступ APIvk

        # Импорт переменных окружения (ключей и тп.)
        load_dotenv()

        # Авторизация
        self.vk_api_access = self.do_auth()

        if self.vk_api_access is not None:
            self.authorized = True

        # Импорт id страницы
        self.main_user_id = os.getenv("USER_ID")

    def do_auth(self):
        # функция Authorizations бота-пользователя
        """
        :return:
        """

        token = os.getenv("ACCESS_TOKEN")

        try:
            self.vk_session = vk_api.VkApi(token=token)
            return self.vk_session.get_api()
        except Exception as error:
            print(error)
            return None

    def send_message(self, receiver_user_id: str = None, message_text="тестовое сообщение"):
        # функция отправки сообщения
        """
        :param receiver_user_id: id получателя сообщения
        :param message_text: текст отправляемого сообщения
        :return:
        """

        #
        if not self.authorized:
            print("CriticalError; check ACCESS_TOKEN?")
            return

        # нет id - значение из окружения переменных
        if receiver_user_id is None:
            receiver_user_id = self.main_user_id

        try:
            self.vk_api_access.messages.send(user_id=receiver_user_id, message=message_text, random_id=get_random_id())
            print(f"Сообщение для ID {receiver_user_id} текст: {message_text}")
        except Exception as error:
            print(error)
