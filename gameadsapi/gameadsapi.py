import aiohttp


class GameAds:

    def __init__(self, api_key: str, count_places: int = 8):
        self.api_key = api_key
        self.count_places = count_places
        self._timeout = 5

    def __preset_args(self, user_id: int, count_places: int):
        if count_places == -1:
            count_places = self.count_places

        headers = {'Content-Type': 'application/json'}
        json = {'api_key': self.api_key, 'user_id': user_id, 'count_places': count_places}
        return {'headers': headers, 'json': json, 'timeout': self._timeout}

    @staticmethod
    async def __api_post(url, args):
        async with aiohttp.ClientSession() as session:
            async with session.post(url, **args) as response:
                if response.ok:
                    return await response.json()
        return False

    async def get_subs_list(self, user_id: int, count_places: int = -1):
        """
        Используйте этот метод, чтобы получить список спонсорских заданий и самостоятельно отправлять сообщение пользователям.

        Source: https://api.gameads.pro/docs#/default/get_subs_list_bot_get_subs_list_post

        :param language_code: Необходимо передавать язык клиента
        :param first_name: Необходимо передавать Имя пользователя
        :param user_id: Идентификатор пользователя, которому необходимо отправить сообщение.
        :param count_places: Максимальное количество мест на ОП, если значение не указано, будет установлено по умолчанию при инициализации экземпляра класса GameAds.
        :return: Возвращает список спонсорских заданий в формате [{"id": 123456, "link": "https://t.me/examplelink", "title": "Заголовок канала"}]
        """
        if not self.api_key:
            return []

        args = self.__preset_args(user_id, count_places)
        if res_req := await self.__api_post('https://api.gameads.pro/bot/get_subs_list', args):
            return res_req.get('unfollow_subs')
        return []
