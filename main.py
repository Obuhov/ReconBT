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
