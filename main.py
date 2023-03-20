import telebot
from telebot import types
from Keyboard import *

token = 'Ваш токен'


bot = telebot.TeleBot(token)

# id Канала
channel_id = 'ваш id канала'

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # Получите ID пользователя
    user_id = message.from_user.id
    print(user_id)

    # Проверьте, подписался ли пользователь на ваш канал
    subscribed = bot.get_chat_member(channel_id, user_id).status in['member','administrator','creator']
    # Если пользователь не подписался на ваш канал, отправьте ему сообщение с просьбой подписаться
    if not subscribed:
        bot.reply_to(message, "Вы должны быть участником группы Ботоводов, чтобы получить доступ к боту.")
        return
    else:
        bot.send_photo(message.chat.id, photo=open('1.jpg', 'rb'), caption="""*Привет*,👋
        \nЯ твой помощник *Gena*!
        \nВо мне заложена вся необходимая информация, которая поможет тебе с работой/настройкой твоего робота *GO*'.""",
                       reply_markup=main_menu, parse_mode='Markdown')

    # Если пользователь подписался на ваш канал, разрешите ему доступ к вашей функциональности

###################################################################################################################
# окно Сообщение винда
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    user_id = call.from_user.id
    print(user_id)
    subscribed = bot.get_chat_member(channel_id, user_id).status in ['member','administrator', 'creator']
        #https://t.me/+-an39HtwpBliNTZi
    # func oknororbot
    if call.data == "robot" and subscribed:
        bot.edit_message_media(media=types.InputMediaPhoto(open('2.jpg', 'rb')),chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="Для того что бы приступить к работе выберете вариант который Вам подходит ﻿👇﻿",
                              reply_markup=oknorobot)
    elif call.data == 'ystanivkasO':
        bot.edit_message_media(media=types.InputMediaPhoto(open('3.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="Для того, чтобы приступить к установке робота - нам нужен сервер",
                                 reply_markup=oknoserv)
    # func oknoVopro
    elif call.data == "Vopros" and not subscribed:
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="Заблокировано", reply_markup=zadatvopros)
    elif call.data == "Vopros" and subscribed:
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="Если у Вас появились какие-либо вопросы, то можете написать нам в *Чат поддержки* и задать их там, а еще возможно вопросы отпадут после подписки на *Канал ботоводов*ℹ﻿", reply_markup=zadatvopros)
    # Funk backmainmenu
    elif call.data == "back":
        bot.edit_message_media(media=types.InputMediaPhoto(open('1.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption="""*Привет*, 👋Я твой помощник *Gena*!
        \nВо мне заложена вся необходимая информация, которая поможет тебе с работой/настройкой твоего робота *GO*'.""",
                              reply_markup=main_menu, parse_mode='Markdown')
    # Funk
    elif call.data == 'backRobot':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""Для того чтобы преступить к работе выберете вариант который Вам подходит ﻿👇﻿""",
                              reply_markup=oknorobot)
    # Funk
    elif call.data == 'mainmenu':
        bot.edit_message_media(media=types.InputMediaPhoto(open('1.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""*Привет*,👋 Я твой помощник *Gena*! 
                              \nВо мне заложена вся необходимая информация, которая поможет тебе с работой/настройкой твоего робота *GO*'.""",
                              reply_markup=main_menu, parse_mode='Markdown')

    elif call.data == 'MT42' :
        bot.edit_message_media(media=types.InputMediaPhoto(open('20.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""Предупреждение!
                              \nПосле установки и настройки робота необходимо связаться с администратором @Choojoy1 для проверки правильности проделанных настроек и ТОЛЬКО ПОСЛЕ ЭТОГО запускать работу робота!
                              \n☝ При пренебрежении этим пунктом Вы полностью берете все риски на себя в случае непредвиденной ситуации.""",
                              reply_markup=OknonachatobnovMt4, parse_mode='Markdown')
    elif call.data == 'MT52':
        bot.edit_message_media(media=types.InputMediaPhoto(open('19.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""Предупреждение!
                              \nПосле установки и настройки робота необходимо связаться с администратором @Choojoy1 для проверки правильности проделанных настроек и ТОЛЬКО ПОСЛЕ ЭТОГО запускать работу робота!
                              \n☝ При пренебрежении этим пунктом Вы полностью берете все риски на себя в случае непредвиденной ситуации.""",
                              reply_markup=OknonachatobnovMt5, parse_mode='Markdown')
    elif call.data == 'backooknovibor2':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""Выберите терминал""",
                              reply_markup=ooknovibor2, parse_mode='Markdown')
    # Funk

    # Funk
    elif call.data == 'ymenyaestsrv':
        bot.edit_message_media(media=types.InputMediaPhoto(open('5.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption=
                              """Для того что бы подключиться к нашему удаленному серверу нам нужно установить необходимое ПО.
                              \nНиже Вы найдете ссылки для установки ПО для вашего устройства. ﻿👇﻿""",
                              reply_markup=oknoPodlyaydalen, parse_mode='Markdown')
    elif call.data == 'arendserver':
        bot.edit_message_media(media=types.InputMediaPhoto(open('4.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""📍РЕГИСТРАЦИЯ СЕРВЕРА
                              \nДля постоянной работы робота GO' нам необходим сервер, что бы поддерживать работу терминала 24/7.
                              \nМы подготовили *пошаговое обучающее видео* по регистрации и аренде сервера, а также рассказали про *тарифы и их различия*, чтобы Вы могли выбрать максимально подходящий тариф под Ваши нужды из соображения кол-во/цена/качество. 
                              \n👉 Жми кнопку *"Начать регистрацию"* - чтобы получить видео и все необходимые ссылки для регистрации.""",
                              reply_markup=oknoregServer, parse_mode='Markdown')

    elif call.data == 'nachatreg':
        video = 'BAACAgIAAxkBAAIQ7GQTjjPDbh6Qs50rhL6f_XvlGt7BAAJRLAACLZaYSAm87v3i8dDSLwQ'
        bot.edit_message_media(media=types.InputMediaVideo(video), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)


        # bot.edit_message_media(media=types.InputMediaPhoto(open('4.jpg', 'rb')), chat_id=call.message.chat.id,
        #                        message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""Ссылка для регистрации: 
                              \nhttps://zomro.com/vds?from=305137
                              \nПромокод:""",
                              reply_markup=regserver, parse_mode='Markdown')
    elif call.data == 'regserverbtn':
        bot.edit_message_media(media=types.InputMediaPhoto(open('5.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption=
                              """Для того что бы подключиться к нашему удаленному серверу нам нужно установить необходимое ПО.
                              \nНиже Вы найдете ссылки для установки ПО для вашего устройства. ﻿👇﻿""",
                              reply_markup=oknoPodlyaydalen, parse_mode='Markdown')

    # Funk
    elif call.data == 'backservrer':
        bot.edit_message_media(media=types.InputMediaPhoto(open('3.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""Для того, чтобы приступить к установке робота - нам нужен сервер""",
                              reply_markup=oknoserv, parse_mode='Markdown')
    # Funk
    elif call.data == 'backPoydalenki':
        bot.edit_message_media(media=types.InputMediaPhoto(open('5.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""Для того что бы подключиться к нашему удаленному серверу нам нужно установить необходимое ПО.
                              \nНиже Вы найдете ссылки для установки ПО для вашего устройства. ﻿👇﻿""",
                              reply_markup=oknoPodlyaydalen, parse_mode='Markdown')
    # Funk
    elif call.data == 'YaskachalPo':
        bot.edit_message_media(media=types.InputMediaPhoto(open('6.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""📍*УСТАНОВКА УДАЛЕНКИ ДЛЯ СЕРВЕРА*
                              \nПосле того, как мы скачали программу для удаленного подключения к нашему серверу нам необходимо "залогинить" наш сервер.
                              \n👇 Как это сделать мы показали в видео уроке ниже:
                              \nВидео установка для пк+как попасть на сервер
                              \nВидео установка для смартфона""",
                              reply_markup=ystanovkaydalenki, parse_mode='Markdown')
    # Funk ya popal na server
    elif call.data == 'Yapopalnaserv':
        bot.edit_message_media(media=types.InputMediaPhoto(open('2.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""Выберите терминал ﻿👇﻿""",
                              reply_markup=viborterm1, parse_mode='Markdown')
    elif call.data == 'backystanovkapo':
        bot.edit_message_media(media=types.InputMediaPhoto(open('6.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""📍*УСТАНОВКА УДАЛЕНКИ ДЛЯ СЕРВЕРА*
                              \nПосле того, как мы скачали программу для удаленного подключения к нашему серверу нам необходимо "залогинить" наш сервер.
                              \n👇 Как это сделать мы показали в видео уроке ниже:
                              \nВидео установка для пк+как попасть на сервер
                              \nВидео установка для смартфона""",
                              reply_markup=ystanovkaydalenki, parse_mode='Markdown')
    elif call.data == 'Windows':
        Windows = types.InlineKeyboardMarkup(row_width=1)
        Windows.add(backServ)
        Windows.add(Mainmenu)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""Для удаленного доступа на 🖥 *Windows* мы рекомендуем использовать *mRemoteNG* - версию *Stable.*
                              \n👇 *Ссылка для скачивания актуальной версии* :
                              \nhttps://mremoteng.org/download""",
                              reply_markup=Windows, parse_mode='Markdown')
    elif call.data == 'Android':
        Android = types.InlineKeyboardMarkup(row_width=1)
        Android.add(backServ)
        Android.add(Mainmenu)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""Для удаленного доступа на  📲 *Android* мы рекомендуем использовать RD Client.
                              \n👇 *Ссылка для скачивания актуальной версии* :
                              \nhttps://play.google.com/store/apps/details?id=com.microsoft.rdc.androidx&hl=ru&gl=US&pli=1""",
                              reply_markup=Android, parse_mode='Markdown')
    elif call.data == 'MacOs':
        MacOs = types.InlineKeyboardMarkup(row_width=1)
        MacOs.add(backServ)
        MacOs.add(Mainmenu)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""Для удаленного доступа на  🍏 *macOS* мы рекомендуем использовать RD Client.
                              \n👇 *Ссылка для скачивания актуальной версии* :
                              \n*https://apps.apple.com/ru/app/microsoft-remote-desktop/id1295203466?mt=12*""",
                              reply_markup=MacOs, parse_mode='Markdown')
    elif call.data == 'IOS':
        IOS = types.InlineKeyboardMarkup(row_width=1)
        IOS.add(backServ)
        IOS.add(Mainmenu)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""Для удаленного доступа на  🍎 *IOS* мы рекомендуем использовать RD Client.
\n👇 *Ссылка для скачивания актуальной версии* :
\n*https://apps.apple.com/ru/app/%D1%83%D0%B4%D0%B0%D0%BB%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9-%D1%80%D0%B0%D0%B1%D0%BE%D1%87%D0%B8%D0%B9-%D1%81%D1%82%D0%BE%D0%BB/id714464092*""",
                              reply_markup=IOS, parse_mode='Markdown')

    ###################################################################################################################-MT-5-
    # fUNC
    elif call.data == 'MT4.1':
        bot.edit_message_media(media=types.InputMediaPhoto(open('24.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""*После того, как мы установили все необходимое ПО* и подключились к нашему удаленному серверу далее нам *необходимо установить торговый терминал.
                              \nУ каждого брокера есть свои торговые терминалы*, которые уже настроены под их сервера нужно лишь скачать их и авторизоваться со своим торговым счетом.
                              \n*Ниже представлены брокеры, с которыми мы работаем.*
                              \nКликнув по одному из них Вы получите все необходимые ссылки для скачивания.
                              \nP.S. Если какие-то ссылки не открываются используйте VPN.""",
                              reply_markup=YstanovkaMt4, parse_mode='Markdown')
    elif call.data == 'backviborterm4':
        bot.edit_message_media(media=types.InputMediaPhoto(open('2.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""Выберите терминал ﻿👇﻿""",
                              reply_markup=viborterm1, parse_mode='Markdown')
    elif call.data == 'Forex4u':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""texttext""",
                              reply_markup=Forex4uvid, parse_mode='Markdown')
    elif call.data == 'backystanovkaMT4':
        bot.edit_message_media(media=types.InputMediaPhoto(open('24.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""*После того, как мы установили все необходимое ПО* и подключились к нашему удаленному серверу далее нам *необходимо установить торговый терминал.
                              \nУ каждого брокера есть свои торговые терминалы*, которые уже настроены под их сервера нужно лишь скачать их и авторизоваться со своим торговым счетом.
                              \n*Ниже представлены брокеры, с которыми мы работаем.*
                              \nКликнув по одному из них Вы получите все необходимые ссылки для скачивания.
                              \nP.S. Если какие-то ссылки не открываются используйте VPN.""",
                              reply_markup=YstanovkaMt4, parse_mode='Markdown')
    elif call.data == 'ystanovilbrokeramt4':
        bot.edit_message_media(media=types.InputMediaPhoto(open('8.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""📍 *НАСТРОЙКА ТЕРМИНАЛА* 
                              \nПосле того как мы установили терминал нам необходимо авторизоваться и произвести базовую настройку.
                              \nМы записали для Вас видео урок, в котором показали как подготовить/настроить терминал для дальнейшей работы с ним.
                              \n👉 Жми *"Настроить терминал"*, что бы получить видео со всеми необходимыми инструкциями. 
                              \nВидео для удобства разбито таймкодами, чтобы быстро вернутся к простру определенной части настроек.""",
                              reply_markup=Nastroikamt4, parse_mode='Markdown')
    elif call.data == 'nastroittermmt4':
        nastroikaterminalamt4 = types.InlineKeyboardMarkup(row_width=1)
        nastroikaterminalamt4.add(backnastroikatermmt4, Mainmenu)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""text""",
                              reply_markup=nastroikaterminalamt4, parse_mode='Markdown')
    elif call.data == 'backnastroikatermmt4':
        bot.edit_message_media(media=types.InputMediaPhoto(open('8.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""📍 *НАСТРОЙКА ТЕРМИНАЛА* 
                              \nПосле того как мы установили терминал нам необходимо авторизоваться и произвести базовую настройку.
                              \nМы записали для Вас видео урок, в котором показали как подготовить/настроить терминал для дальнейшей работы с ним.
                              \n👉 Жми *"Настроить терминал"*, что бы получить видео со всеми необходимыми инструкциями. 
                              \nВидео для удобства разбито таймкодами, чтобы быстро вернутся к простру определенной части настроек.""",
                              reply_markup=Nastroikamt4, parse_mode='Markdown')

    elif call.data == 'termnastroenmt4':
        bot.edit_message_media(media=types.InputMediaPhoto(open('12.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""📍 *УСТАНОВКА РОБОТА* GO' MT-4 
                              \nЭто самый ответственный этап!
                              \nОтнеситесь к нему максимально ответственно!!!
                              \nПеред тем как перейти к просмотру урока убедитесь, что Вы скачали актуальную версию робота GO’ - получить её можно в канале ботоводов, либо у администратора: @Choojoy1
                              \nДля установки робота мы также подготовили видео урок. 
                              \n👉 Жми *"Начать установку"*, чтобы получить все необходимые инструкции!""",
                              reply_markup=YstanovkarobotaMt4, parse_mode='Markdown')

    elif call.data == 'nachatystanovkymt4':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""Предупреждение!
                              \nПосле установки и настройки робота необходимо связаться *с администратором @Choojoy1 для проверки правильности 
                              \nпроделанных настроек* и ТОЛЬКО ПОСЛЕ ЭТОГО запускать работу робота! 
                              \n☝️ При пренебрежении этим пунктом, вы полностью берете все риски на себя в случае непредвиденной ситуации.""",
                              reply_markup=YstanovkarobotaGoMt4, parse_mode='Markdown')
    elif call.data == 'gotovomt4':
        gotovoystanovkamt4 = types.InlineKeyboardMarkup(row_width=1)
        gotovoystanovkamt4.add(backystanovkarobotamt4, Mainmenu)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""texttext""",
                              reply_markup=gotovoystanovkamt4, parse_mode='Markdown')
    elif call.data == 'backystanovkarobotamt4':
        bot.edit_message_media(media=types.InputMediaPhoto(open('12.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""📍 *УСТАНОВКА РОБОТА* GO' MT-4 
                              \nЭто самый ответственный этап!
                              \nОтнеситесь к нему максимально ответственно!!!
                              \nПеред тем как перейти к просмотру урока убедитесь, что Вы скачали актуальную версию робота GO’ - получить её можно в канале ботоводов, либо у администратора: @Choojoy1
                              \nДля установки робота мы также подготовили видео урок. 
                              \n👉 Жми *"Начать установку"*, чтобы получить все необходимые инструкции!""",
                              reply_markup=YstanovkarobotaMt4, parse_mode='Markdown')
    elif call.data == 'vsenastroenoMT4':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""text""",
                              reply_markup=finalmt4, parse_mode='Markdown')
    elif call.data == 'robotrygaetsyaMT4':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              caption="""Свяжитесь с администратором: @Choojoy1""",
                              reply_markup=robotrugaetsyaMt4, parse_mode='Markdown')
    ###################################################################################################################-MT-5-
    elif call.data == 'MT5.1':
        bot.edit_message_media(media=types.InputMediaPhoto(open('24.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""*После того, как мы установили все необходимое ПО* и подключились к нашему удаленному серверу далее нам *необходимо установить торговый терминал.
        \nУ каждого брокера есть свои торговые терминалы*, которые уже настроены под их сервера нужно лишь скачать их и авторизоваться со своим торговым счетом.
        \n*Ниже представлены брокеры, с которыми мы работаем.*
        \nКликнув по одному из них Вы получите все необходимые ссылки для скачивания.
        \nP.S. Если какие-то ссылки не открываются используйте VPN.""",
                                 reply_markup=YstanovkaMt5, parse_mode='Markdown')
    elif call.data == 'backviborterm':
        bot.edit_message_media(media=types.InputMediaPhoto(open('2.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""Выберите терминал ﻿👇﻿""",
                                 reply_markup=viborterm1, parse_mode='Markdown')
    # fUNC
    elif call.data == 'ystanovilbrokeramt5': #termnastroen
        bot.edit_message_media(media=types.InputMediaPhoto(open('9.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""📍 *НАСТРОЙКА ТЕРМИНАЛА* 
        \nПосле того как мы установили терминал нам необходимо авторизоваться и произвести базовую настройку.
        \nМы записали для Вас видео урок, в котором показали как подготовить/настроить терминал для дальнейшей работы с ним.
        \n👉 Жми *"Настроить терминал"*, что бы получить видео со всеми необходимыми инструкциями. 
        \nВидео для удобства разбито таймкодами, чтобы быстро вернутся к простру определенной части настроек.""",
                                 reply_markup=Nastroikamt5, parse_mode='Markdown')
    elif call.data == 'nastroitterm': #nastroitterm
        nastroikaterminalamt5 = types.InlineKeyboardMarkup(row_width=1)
        nastroikaterminalamt5.add(backnastroikatermmt5, Mainmenu)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""video s nastroikoi terminala""",
                                 reply_markup=nastroikaterminalamt5, parse_mode='Markdown')


    elif call.data == 'termnastroen': #termnastroen
        bot.edit_message_media(media=types.InputMediaPhoto(open('13.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""📍 *УСТАНОВКА РОБОТА* GO' MT-5
        \nЭто самый ответственный этап!
        \nОтнеситесь к нему максимально ответственно!!!
        \nПеред тем как перейти к просмотру урока убедитесь, что Вы скачали актуальную версию робота GO’ - получить её можно в канале ботоводов, либо у администратора: @Choojoy1
        \nДля установки робота мы также подготовили видео урок. 
        \n👉 Жми *"Начать установку"*, чтобы получить все необходимые инструкции!""",
                                 reply_markup=YstanovkarobotaMt5, parse_mode='Markdown')
    elif call.data == 'backnastroikatermmt5':
        bot.edit_message_media(media=types.InputMediaPhoto(open('9.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""📍 *НАСТРОЙКА ТЕРМИНАЛА*  GO' MT-5
        \nПосле того как мы установили терминал нам необходимо авторизоваться и произвести базовую настройку.
        \nМы записали для Вас видео урок, в котором показали как подготовить/настроить терминал для дальнейшей работы с ним.
        \n👉 Жми *"Настроить терминал"*, что бы получить видео со всеми необходимыми инструкциями. 
        \nВидео для удобства разбито таймкодами, чтобы быстро вернутся к простру определенной части настроек.""",
                                 reply_markup=Nastroikamt5, parse_mode='Markdown')
    # elif call.data == 'nachatystanovkymt5':
    #     bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
    #                              caption="""Предупреждение!
    #     \nПосле установки и настройки робота необходимо связаться *с администратором @Choojoy1 для проверки правильности
    #     \nпроделанных настроек* и ТОЛЬКО ПОСЛЕ ЭТОГО запускать работу робота!
    #     \n\n ☝️ При пренебрежении этим пунктом, вы полностью берете все риски на себя в случае непредвиденной ситуации.""",
    #                              reply_markup=YstanovkarobotaGoMt5, parse_mode='Markdown')
    elif call.data =='Cent':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""Предупреждение!
                \nПосле установки и настройки робота необходимо связаться *с администратором @Choojoy1 для проверки правильности
                \nпроделанных настроек* и ТОЛЬКО ПОСЛЕ ЭТОГО запускать работу робота!
                \n\n ☝️ При пренебрежении этим пунктом, вы полностью берете все риски на себя в случае непредвиденной ситуации.""",
                                 reply_markup=YstanovkarobotaGoMt5cent, parse_mode='Markdown')
    elif call.data == 'dollar':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""Предупреждение!
                    \nПосле установки и настройки робота необходимо связаться *с администратором @Choojoy1 для проверки правильности
                    \nпроделанных настроек* и ТОЛЬКО ПОСЛЕ ЭТОГО запускать работу робота!
                    \n\n ☝️ При пренебрежении этим пунктом, вы полностью берете все риски на себя в случае непредвиденной ситуации.""",
                                 reply_markup=YstanovkarobotaGoMt5dollar, parse_mode='Markdown')

    elif call.data == 'backviborscheta':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""Выберите тип своего счета""",
                                 reply_markup=vibortipascheta, parse_mode='Markdown')

        # vibor scheta
    elif call.data == 'nachatystanovkymt5':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""Выберите тип своего счета""",
                                 reply_markup=vibortipascheta, parse_mode='Markdown')

    elif call.data == 'backystanovkarobotamt5':
        bot.edit_message_media(media=types.InputMediaPhoto(open('13.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""📍 *УСТАНОВКА РОБОТА* GO' MT-5
        \nЭто самый ответственный этап!
        \nОтнеситесь к нему максимально ответственно!!!
        \nПеред тем как перейти к просмотру урока убедитесь, что Вы скачали актуальную версию робота GO’ - получить её можно в канале ботоводов, либо у администратора: @Choojoy1
        \nДля установки робота мы также подготовили видео урок. 
        \n👉 Жми *"Начать установку"*, чтобы получить все необходимые инструкции!""",
                                 reply_markup=YstanovkarobotaMt5, parse_mode='Markdown')
    elif call.data == 'gotovomt5':
        gotovoystanovka = types.InlineKeyboardMarkup(row_width=1)
        gotovoystanovka.add(backystanovkarobotamt5, Mainmenu)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""text""",
                                 reply_markup=gotovoystanovka, parse_mode='Markdown')

    elif call.data == 'roboforex':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""text""",
                                 reply_markup=roboforexvid, parse_mode='Markdown')
    elif call.data == 'Xm':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""text""",
                                 reply_markup=Xmvid, parse_mode='Markdown')
    elif call.data == 'HF':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""text""",
                                 reply_markup=HFvid, parse_mode='Markdown')
    elif call.data == 'backystanovkaMT5':
        bot.edit_message_media(media=types.InputMediaPhoto(open('24.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""*После того, как мы установили все необходимое ПО* и подключились к нашему удаленному серверу далее нам *необходимо установить торговый терминал.
        \nУ каждого брокера есть свои торговые терминалы*, которые уже настроены под их сервера нужно лишь скачать их и авторизоваться со своим торговым счетом.
        \n*Ниже представлены брокеры, с которыми мы работаем.*
        \nКликнув по одному из них Вы получите все необходимые ссылки для скачивания.
        \nP.S. Если какие-то ссылки не открываются используйте VPN.""",
                                 reply_markup=YstanovkaMt5, parse_mode='Markdown')

    elif call.data == 'vsenastroenoMT5cent':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""text""",
                                 reply_markup=final1cent, parse_mode='Markdown')
    elif call.data == 'vsenastroenoMT5dollar':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""text""",
                                 reply_markup=final1dollar, parse_mode='Markdown')
    elif call.data == 'robotrygaetsyaMT5cent':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""Свяжитесь с администратором: @Choojoy1""",
                                 reply_markup=robotrugaetsyaMt5cent, parse_mode='Markdown')

    elif call.data == 'robotrygaetsyaMT5dollar':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""Свяжитесь с администратором: @Choojoy1""",
                                 reply_markup=robotrugaetsyaMt5dollar1, parse_mode='Markdown')
    elif call.data == 'backvibralicent':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""Предупреждение!
                \nПосле установки и настройки робота необходимо связаться *с администратором @Choojoy1 для проверки правильности
                \nпроделанных настроек* и ТОЛЬКО ПОСЛЕ ЭТОГО запускать работу робота!
                \n☝️ При пренебрежении этим пунктом, вы полностью берете все риски на себя в случае непредвиденной ситуации.""",
                                 reply_markup=YstanovkarobotaGoMt5cent, parse_mode='Markdown')
    elif call.data == 'backvibralidollar':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""Предупреждение!
                        \nПосле установки и настройки робота необходимо связаться *с администратором @Choojoy1 для проверки правильности
                        \nпроделанных настроек* и ТОЛЬКО ПОСЛЕ ЭТОГО запускать работу робота!
                        \n\n ☝️ При пренебрежении этим пунктом, вы полностью берете все риски на себя в случае непредвиденной ситуации.""",
                                 reply_markup=YstanovkarobotaGoMt5dollar, parse_mode='Markdown')
    # обновление
    elif call.data == 'Obnova':
        bot.edit_message_media(media=types.InputMediaPhoto(open('18.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""*📍ОБНОВЛЕНИЕ РОБОТА*
    \nДля того  чтобы приступить к обновлению, требуется выполнить ряд обязательных действий. 
    \nСперва нам нужно понять, *готов ли наш счет* к этому или нет? 
    \nВыберете вариант, который соответствует Вашей ситуации, для того чтобы перейти к следующему шагу""",
                                 reply_markup=oknoobnova, parse_mode='Markdown')
    #
    elif call.data == 'nachatobnov':
        bot.edit_message_media(media=types.InputMediaPhoto(open('18.jpg', 'rb')), chat_id=call.message.chat.id,
                               message_id=call.message.message_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""Выберите терминал""",
                                 reply_markup=ooknovibor2, parse_mode='Markdown')
    #
    elif call.data == 'estsdelki':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""❗ *Для установки обновления* нам нужно высушить нашего робота - простыми словами дождаться закрытия всех открытых сделок по паре.
    \n👇 Какие шаги нужно предпринять рассказали в видео.
    \nВидео - как высушить робота""",
                                 reply_markup=oknoestsdelki, parse_mode='Markdown')
    elif call.data == 'backobnovlenie':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""❗*Для установки обновления* нам нужно высушить нашего робота - простыми словами дождаться закрытия всех открытых сделок по паре.
    \n👇 Какие шаги нужно предпринять рассказали в видео.
    \nВидео - как высушить робота""",
                                 reply_markup=oknoobnova, parse_mode='Markdown')
    elif call.data == 'vsesdelkizakriti':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""❗ Перед тем как перейти к просмотру урока убедитесь, что Вы скачали *актуальную версию робота GO’* - получить её можно в канале ботоводов, либо у администратора: @Choojoy1
    \nДля установки робота мы также подготовили видео урок. 
    \nДля того, *что бы установить обновление* нам необходимо заменить старую версию робота.
    \nВидео: где и как менять робота""",
                                 reply_markup=oknokakystanovit, parse_mode='Markdown')
    elif call.data == 'backkakystanovitobnov':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""❗ Перед тем как перейти к просмотру урока убедитесь, что Вы скачали *актуальную версию робота GO’* - получить её можно в канале ботоводов, либо у администратора: @Choojoy1
            \nДля установки робота мы также подготовили видео урок. 
            \nДля того, *что бы установить обновление* нам необходимо заменить старую версию робота.
            \nВидео: где и как менять робота""",
                                 reply_markup=oknokakystanovit, parse_mode='Markdown')

    #
    elif call.data == 'netsdelok':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""❗ Перед тем как перейти к просмотру урока убедитесь, что Вы скачали *актуальную версию робота GO’* - получить её можно в канале ботоводов, либо у администратора: @Choojoy1
    \nДля установки робота мы также подготовили видео урок. 
    \nДля того, *что бы установить обновление* нам необходимо заменить старую версию робота.
    \nВидео: где и как менять робота""",
                                 reply_markup=oknokakystanovit, parse_mode='Markdown')

    elif call.data == 'backnachatystanovkyGomt4':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""Предупреждение!\n
        \nПосле установки и настройки робота необходимо связаться *с администратором @Choojoy1 для проверки правильности 
        \nпроделанных настроек* и ТОЛЬКО ПОСЛЕ ЭТОГО запускать работу робота! 
        \n☝ При пренебрежении этим пунктом Вы полностью 
        \nберете все риски на себя в случае непредвиденной ситуации.""",
                                 reply_markup=YstanovkarobotaGoMt4, parse_mode='Markdown')
    elif call.data == 'backnachatystanovkyGomt5':
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 caption="""Предупреждение!\n
            \nПосле установки и настройки робота необходимо связаться *с администратором @Choojoy1 для проверки правильности 
            \nпроделанных настроек* и ТОЛЬКО ПОСЛЕ ЭТОГО запускать работу робота! 
            \n☝ При пренебрежении этим пунктом Вы полностью 
            \nберете все риски на себя в случае непредвиденной ситуации.""",
                                 reply_markup=vibortipascheta, parse_mode='Markdown')

    ###################################################################################################################

    # elif call.data == None:
    #     bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
    #                           text="""""",
    #                           reply_markup=None, parse_mode='Markdown')
    # elif call.data == '':

    # elif call.data:
    # bot.edit_message_text()
    else:
        # bot.send_message(chat_id=call.message.chat.id, text="Вам запрещен доступ")
        # bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id,timeout=3)
        # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id+1, timeout=3)

        bot.send_message(chat_id=call.message.chat.id, text="Option selected: " + call.data)



# @bot.message_handler(commands=["startbotblyat"])
# def start(message):
#     # # keyboard1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     # # keyboard1.row('Старт')
#     # bot.send_message(chat_id=message.chat.id, text='Вам было выведено меню', reply_markup=keyboard1)
#     bot.send_photo(message.chat.id, photo=open('1.jpg', 'rb'), caption ="""*Привет*,👋
# Я твой помощник *Gena*!
# Во мне заложена вся необходимая информация, которая поможет тебе с работой/настройкой твоего робота *GO*'.""",
#                      reply_markup=main_menu, parse_mode='Markdown')
    # video = open('RegServ.mp4','rb')
    # bot.send_video(message.chat.id, video)
    # video.close()
    # time.sleep(3600)

bot.polling(none_stop=True)

