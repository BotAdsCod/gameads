# GameAds API
Интеграция сервиса по автоматической покупке/продаже Telegram трафика - <a href="https://t.me/GamesAdsBot">``GameAds``</a>



## Установка

```bash
pip install git+https://github.com/BotAdsCod/gameads.git
```

## Зависимости

 - ``Python 3.7+``
 - ``aiohttp``

## Как это работает?
Перед выполнением определенных действий ваш бот отправляет запрос на проверку подписок с помощью метода ``get_subs_list``. Результатом этого запроса будет возвращен список всех спонсорских заданий для вашего бота.


## Пример использования с фреймворком aiogram 3

```python
from gameadsapi import GameAds

from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app import bot, dp

router = Router(name="example_router")
dp.include_router(router)

gameads = GameAds(API_KEY) #Для каждого бота уникальный API-ключ, который можно получить в настройках бота, в разделе "Интеграция".

#Пример генерации клавиатуры со списком спонсоров
def subs_kb(subs_list: list) -> InlineKeyboardMarkup:
    markup = InlineKeyboardBuilder()

    for i, sub in enumerate(subs_list, 1):
        text = '❌ {}. запустить бота' if 'bot' in sub['link'].lower() else '❌ {}. подписаться на канал'
        markup.button(text=text.format(i), url=sub['link'])

    markup.button(text='✅ Я подписался', callback_data='check_follow')
    return markup.as_markup()

async def is_unfollow(_):
    subs_list = await gameads.get_subs_list(_.from_user.id)
    return {'subs': subs_list} if subs_list else False

#Вызывается при нажатии кнопки проверки подписки
@router.callback_query(F.data == 'check_follow', is_unfollow) 
async def check_follow(call: CallbackQuery, subs: list):
    await call.message.edit_reply_markup(reply_markup=subs_kb(subs)) #Обновление списка спонроских заданий в сообщении
    await call.answer("❌ Подпишитесь на все каналы!", show_alert=True)

#Ваша функция в которой необходима проверка на подписку
@router.callback_query(is_unfollow) 
@router.message(is_unfollow) 
async def cm_handler(cm: CallbackQuery | Message, subs: list):
    msg = cm.message if isinstance(cm, CallbackQuery) else cm
    await msg.answer("👇Чтобы получить доступ к функциям бота выполните задания и нажмите кнопку «✅ Я подписался»👇", 
                      reply_markup=subs_kb(subs),
                      show_alert=True)
    
@router.callback_query(F.data == 'check_follow')
async def check_follow(call: CallbackQuery):
    ...
    #Ваш код который выполняется если для пользователя нет спонсорских заданий (или он подписан на все каналы)
```

Если у вас возникли вопросы по подключению, обращайтесь по контактам, указанным в описании <a href="https://t.me/GamesAdsBot">``GameAds``</a>
