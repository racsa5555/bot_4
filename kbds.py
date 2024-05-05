from aiogram.utils.keyboard import InlineKeyboardBuilder,InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton

def get_lang_kb(current_lang):
    if current_lang == 'RU':
        flag = '🇰🇬'
        new_lang = 'KG'
    else:
        flag = '🇷🇺'
        new_lang = 'RU'
    kb = InlineKeyboardButton(text = f'Переключить язык на {flag}',callback_data = f'switch_language_{new_lang}')
    return kb

login_or_register_ru = ReplyKeyboardMarkup(
    keyboard= [
        [
        KeyboardButton(text = 'Войти'),
        KeyboardButton(text = 'Пройти регистрацию')
        ]
    ],
    resize_keyboard=True
)

login_or_register_kg = ReplyKeyboardMarkup(
    keyboard= [
        [
        KeyboardButton(text = 'Кируу'),
        KeyboardButton(text = 'Катталуу')
        ]
    ],
    resize_keyboard=True
)

set_city_kb = InlineKeyboardBuilder(
    markup= [
        [InlineKeyboardButton(text = 'Бишкек',callback_data='city_set_bish')],
        [InlineKeyboardButton(text = 'Ош',callback_data='city_set_osh')],
        [InlineKeyboardButton(text = 'Гулчо',callback_data='city_set_gulcho')],
        [InlineKeyboardButton(text = 'Сокулук',callback_data='city_set_sokuluk')],
        [InlineKeyboardButton(text = 'Токмок',callback_data='city_set_tokmok')]
        ]
)
profile_kb_ru = InlineKeyboardBuilder(
    markup=[
        [InlineKeyboardButton(text = 'Изменить профиль',callback_data='update_profile')],
        [get_lang_kb('RU')]
    ]
)
profile_kb_kg = InlineKeyboardBuilder(
    markup=[
        [InlineKeyboardButton(text = 'Профилди өзгөртүү',callback_data='update_profile')],
        [get_lang_kb('KG')]
    ]
)
default_kb_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = '🔎Отслеживание'),
            KeyboardButton(text = '👤Профиль'),
            
        ],
        [
            KeyboardButton(text = '⚙️Поддержка'),
            KeyboardButton(text = '📬Адреса'),
        ],
        [
            KeyboardButton(text = '📏Калькулятор'),
            KeyboardButton(text = '📕Инструкция'),
        ]
    ],
    resize_keyboard=True
)

default_kb_kg = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = '🔎Издөө'),
            KeyboardButton(text = '👤Профиль'),
            
        ],
        [
            KeyboardButton(text = '⚙️Колдоо'),
            KeyboardButton(text = '📬Дарек'),
        ],
        [
            KeyboardButton(text = '📏Эсептөөчү'),
            KeyboardButton(text = '📕Нускама'),
        ]
    ],
    resize_keyboard=True
)
cancel_calc_ru = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text = 'Отмена')
        ]
    ],
    resize_keyboard=True
)
cancel_calc_kg = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text = 'Артка')
        ]
    ],
    resize_keyboard=True
)


tracking_kb_ru = InlineKeyboardBuilder(
    markup=[
        [InlineKeyboardButton(text = 'По трек-коду',callback_data = 'track-code')],
        [InlineKeyboardButton(text = 'По коду клиента',callback_data='client_id')]
    ]
)


tracking_kb_kg = InlineKeyboardBuilder(
    markup=[
        [InlineKeyboardButton(text = 'Трек код боюнча',callback_data = 'track-code')],
        [InlineKeyboardButton(text = 'Жеке id боюнча',callback_data='client_id')]
    ]
)

instruction_kb = InlineKeyboardBuilder(
    markup=[
        [InlineKeyboardButton(text = 'Pinduoduo',callback_data = 'choose_pin')],
        [InlineKeyboardButton(text = 'Taobao',callback_data = 'choose_tao')],
        [InlineKeyboardButton(text = '1688',callback_data = 'choose_1688')],
        [InlineKeyboardButton(text = 'Poizon',callback_data = 'choose_poi')]
    ]
)

set_variables_kbds = InlineKeyboardBuilder(
    markup = [
        [InlineKeyboardButton(text = 'Поменять цены',callback_data='set_prices')],
        [InlineKeyboardButton(text = 'Поменять ссылку для поддержки',callback_data = 're_whatsapp')],
        [InlineKeyboardButton(text = 'Поменять маркетплейсы',callback_data='set_marketplace')],
        [InlineKeyboardButton(text = 'Рассылка новостей',callback_data = 'send_broadcast')],
        [InlineKeyboardButton(text = 'Сменить пароль админа',callback_data = 'reset_password')],
        [InlineKeyboardButton(text = 'Сменить адрес Бишкек',callback_data = 'reset_city_bish')],
        [InlineKeyboardButton(text = 'Сменить адрес Ош',callback_data = 'reset_city_osh')],
        [InlineKeyboardButton(text = 'Сменить адрес Гулчо',callback_data = 'reset_city_gulcho')],
        [InlineKeyboardButton(text = 'Сменить адрес Сокулук',callback_data = 'reset_city_sokuluk')],
        [InlineKeyboardButton(text = 'Сменить адрес Токмок',callback_data = 'reset_city_tokmok')],
        [InlineKeyboardButton(text = 'Выйти',callback_data='logout_admin')]
    ]
)

set_marketplace = InlineKeyboardBuilder(
    markup=[
        [InlineKeyboardButton(text = 'Pinduoduo',callback_data = 'r_pinduoduo')],
        [InlineKeyboardButton(text = 'TAOBAO',callback_data = 'r_taobao')],
        [InlineKeyboardButton(text = '1688',callback_data = 'r_1688')],
        [InlineKeyboardButton(text = 'POIZON',callback_data = 'r_poizon')]
    ]
)

set_price = InlineKeyboardBuilder(
    markup=[
        [InlineKeyboardButton(text = 'Цена по весу в Бишкеке',callback_data = 'p_price_weight_bish')],
        [InlineKeyboardButton(text = 'Цена по обьему в Бишкеке',callback_data = 'p_price_volume_bish')],
        [InlineKeyboardButton(text = 'Цена по весу в Оше',callback_data = 'p_price_weight_osh')],
        [InlineKeyboardButton(text = 'Цена по обьему в Оше',callback_data = 'p_price_volume_osh')],
        [InlineKeyboardButton(text = 'Цена по весу в Гулчо',callback_data = 'p_price_weight_gulcho')],
        [InlineKeyboardButton(text = 'Цена по обьему в Гулчо',callback_data = 'p_price_volume_gulcho')],
        [InlineKeyboardButton(text = 'Цена по весу в Токмок',callback_data = 'p_price_weight_tokmok')],
        [InlineKeyboardButton(text = 'Цена по обьему в Токмок',callback_data = 'p_price_volume_tokmok')],
        [InlineKeyboardButton(text = 'Цена по весу в Сокулук',callback_data = 'p_price_weight_sokuluk')],
        [InlineKeyboardButton(text = 'Цена по обьему в Сокулук',callback_data = 'p_price_volume_sokuluk')]
    ]
)
        