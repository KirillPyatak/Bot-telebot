from telebot import types

main_menu = types.InlineKeyboardMarkup(row_width=1)
robott = types.InlineKeyboardButton("🤖 Робот", callback_data="robot")
zadatvopor = types.InlineKeyboardButton("❓Задать вопрос", callback_data="Vopros")
main_menu.add(robott, zadatvopor)

# кнопка главное меню
Mainmenu = types.InlineKeyboardButton("🔝 В главное меню", callback_data="mainmenu")
# окно задать вопрос
zadatvopros = types.InlineKeyboardMarkup(row_width=1)
ChatPodder = types.InlineKeyboardButton("💬 Чат поддержки", callback_data="ChatPodd")
Kanaldrop = types.InlineKeyboardButton("™️ Канал ботоводов", callback_data="KanalDrop")
back_button = types.InlineKeyboardButton("🔙 Назад", callback_data="back")
zadatvopros.add(ChatPodder, Kanaldrop, back_button)

# окно робот
oknorobot = types.InlineKeyboardMarkup(row_width=2)
ystanovkasO = types.InlineKeyboardButton("🕹 Установка с 0", callback_data="ystanivkasO")
obnova = types.InlineKeyboardButton("♻ Обновление", callback_data="Obnova")
# back_button = types.InlineKeyboardButton("🔙 Назад", callback_data="back")
oknorobot.add(ystanovkasO, obnova, back_button)

#Okno obnova
oknoobnova = types.InlineKeyboardMarkup(row_width=1)
estsdelki = types.InlineKeyboardButton("👎🏻 У меня есть открытые сделки", callback_data="estsdelki")
netsdelok = types.InlineKeyboardButton("👍 У меня нет открытых сделок", callback_data="netsdelok")
back_robot = types.InlineKeyboardButton("🔙 Назад", callback_data="backRobot")
# back_button = types.InlineKeyboardButton("🔙 Назад", callback_data="back")
oknoobnova.add(estsdelki, netsdelok)
oknoobnova.add(back_robot)
oknoobnova.add(Mainmenu)

#
oknoestsdelki = types.InlineKeyboardMarkup(row_width=1)
vsesdelkizakriti = types.InlineKeyboardButton(" ✅ Все сделки закрыты", callback_data="vsesdelkizakriti")
backobnovlenie = types.InlineKeyboardButton("🔙 Назад", callback_data="backobnovlenie")
oknoestsdelki.add(vsesdelkizakriti, backobnovlenie, Mainmenu)

#
oknokakystanovit = types.InlineKeyboardMarkup(row_width=1)
nachatobnov = types.InlineKeyboardButton("🛠 Начать ОБНОВЛЕНИЕ", callback_data="nachatobnov")
gotovoobnov = types.InlineKeyboardButton("✅ Готово", callback_data="gotovoobnov")
oknokakystanovit.add(nachatobnov,gotovoobnov,backobnovlenie,Mainmenu)

# окно сервер
oknoserv = types.InlineKeyboardMarkup(row_width=1)
Ymenyaestserv = types.InlineKeyboardButton("✅ У меня есть сервер", callback_data="ymenyaestsrv")
Arendserv = types.InlineKeyboardButton("🛒 Арендовать сервер", callback_data="arendserver")
back_robot = types.InlineKeyboardButton("🔙 Назад", callback_data="backRobot")
oknoserv.add(Ymenyaestserv, Arendserv, back_robot)

# Окно Регистрация сервера

oknoregServer = types.InlineKeyboardMarkup(row_width=1)
nachatregbtn = types.InlineKeyboardButton("Начать регистрацию", callback_data="nachatreg")
backServ = types.InlineKeyboardButton("🔙 Назад", callback_data="backservrer")
oknoregServer.add(nachatregbtn, backServ, Mainmenu)

#
ooknovibor2 = types.InlineKeyboardMarkup(row_width=2)
MT42 = types.InlineKeyboardButton("📊GO' MT-4", callback_data="MT42")
MT52 = types.InlineKeyboardButton("📊GO' MT-5", callback_data="MT52")
backkakystanovitobnov = types.InlineKeyboardButton("🔙 Назад",callback_data="backkakystanovitobnov")
ooknovibor2.add(MT42,MT52)
ooknovibor2.add(backkakystanovitobnov)
ooknovibor2.add(Mainmenu)
#
OknonachatobnovMt4 = types.InlineKeyboardMarkup(row_width=1)
vsenastroenomt4 = types.InlineKeyboardButton("✅ Все настроено и работает", callback_data="vsenastroenomt4")
robotrygaetsyamt4 = types.InlineKeyboardButton("❌ Робот ругается", callback_data="robotrygaetsyamt4")
backooknovibor2 = types.InlineKeyboardButton("🔙 Назад", callback_data="backooknovibor2")
OknonachatobnovMt4.add(vsenastroenomt4,robotrygaetsyamt4,backooknovibor2,Mainmenu)

#
OknonachatobnovMt5 = types.InlineKeyboardMarkup(row_width=1)
vsenastroenomt5 = types.InlineKeyboardButton("✅ Все настроено и работает", callback_data="vsenastroenomt5")
robotrygaetsyamt5 = types.InlineKeyboardButton("❌ Робот ругается", callback_data="robotrygaetsyamt5")
backooknovibor2 = types.InlineKeyboardButton("🔙 Назад", callback_data="backooknovibor2")
OknonachatobnovMt5.add(vsenastroenomt5,robotrygaetsyamt5,backooknovibor2,Mainmenu)
#
regserver = types.InlineKeyboardMarkup(row_width=1)
regserverbtn = types.InlineKeyboardButton("✅ Я зарегистрировал(а) сервер", callback_data="regserverbtn")
regserver.add(regserverbtn, Mainmenu)

# окно ПО для удаленки
oknoPodlyaydalen = types.InlineKeyboardMarkup(row_width=2)
Windows = types.InlineKeyboardButton("🖥 Windows", callback_data="Windows")
MacOs = types.InlineKeyboardButton("🍏 macOS", callback_data="MacOs")
IOS = types.InlineKeyboardButton("🍎 IOS", callback_data="IOS")
Android = types.InlineKeyboardButton("📲 Android", callback_data="Android")
YaskachalPo = types.InlineKeyboardButton("✅ Я скачал(а) ПО", callback_data="YaskachalPo")
oknoPodlyaydalen.add(Windows, MacOs, IOS, Android)
oknoPodlyaydalen.add(YaskachalPo)
oknoPodlyaydalen.add(backServ)
oknoPodlyaydalen.add(Mainmenu)
# Назад к По удаленки
backystanovkapo = types.InlineKeyboardButton("🔙 Назад", callback_data="backystanovkapo")
# Установка УДАЛЕНКИ ДЛЯ СЕРВЕРА
ystanovkaydalenki = types.InlineKeyboardMarkup(row_width=1)
YaskachalPo = types.InlineKeyboardButton("✅ Я попал(а) на сервер", callback_data="Yapopalnaserv")
backServ = types.InlineKeyboardButton("🔙 Назад", callback_data="backPoydalenki")
ystanovkaydalenki.add(YaskachalPo)
ystanovkaydalenki.add(backServ)
ystanovkaydalenki.add(Mainmenu)

# Поле выбора Терминала
viborterm1 = types.InlineKeyboardMarkup(row_width=2)
Mt4 = types.InlineKeyboardButton("📊GO' MT-4", callback_data="MT4.1")
Mt5 = types.InlineKeyboardButton("📊GO' MT-5", callback_data="MT5.1")
viborterm1.add(Mt4, Mt5)
viborterm1.add(backystanovkapo)
viborterm1.add(Mainmenu)

#####################################-ВЫБОР МТ-4-##############################################################################
# Установка MT-4
YstanovkaMt4 = types.InlineKeyboardMarkup(row_width=1)
Forex4u = types.InlineKeyboardButton("📊 Forex4you", callback_data="Forex4u")
ystanovilbrokeramt4 = types.InlineKeyboardButton("✅ Я установил(а) терминал", callback_data="ystanovilbrokeramt4")
backviborterm4 = types.InlineKeyboardButton("🔙 Назад", callback_data="backviborterm4")
YstanovkaMt4.add(Forex4u, ystanovilbrokeramt4, backviborterm4, Mainmenu)
#
Forex4uvid = types.InlineKeyboardMarkup(row_width=1)
backviborterm4 = types.InlineKeyboardButton("🔙 Назад", callback_data="backystanovkaMT4")
Forex4uvid.add(backviborterm4, Mainmenu)
# Настройка терминала МТ-4
Nastroikamt4 = types.InlineKeyboardMarkup(row_width=1)
nastroittermmt4 = types.InlineKeyboardButton("👉 Настроить терминал", callback_data="nastroittermmt4")
termnastroenmt4 = types.InlineKeyboardButton("✅ Терминал настроен", callback_data="termnastroenmt4")
backystanovkaMT4 = types.InlineKeyboardButton("🔙 Назад", callback_data="backystanovkaMT4")
Nastroikamt4.add(nastroittermmt4, termnastroenmt4, backystanovkaMT4, Mainmenu)

# Настроить треминал для МТ4
Nastroikamt4video = types.InlineKeyboardMarkup(row_width=1)
backnastroikatermmt4 = types.InlineKeyboardButton("🔙 Назад", callback_data="backnastroikatermmt4")
Nastroikamt4video.add(backnastroikatermmt4, Mainmenu)

# Установка робота МТ 4
YstanovkarobotaMt4 = types.InlineKeyboardMarkup(row_width=1)
nachatystanovkymt4 = types.InlineKeyboardButton("🛠 Начать установку", callback_data="nachatystanovkymt4")
gotovomt4 = types.InlineKeyboardButton("✅ Готово", callback_data="gotovomt4")
# backviborterm = types.InlineKeyboardButton("🔙 Назад", callback_data="backystanovkaMT4")
YstanovkarobotaMt4.add(nachatystanovkymt4, gotovomt4, backnastroikatermmt4, Mainmenu)

# Начать Установку ГО МТ4
YstanovkarobotaGoMt4 = types.InlineKeyboardMarkup(row_width=1)
vsenastroenoMT4 = types.InlineKeyboardButton("✅ Все настроено и работает", callback_data="vsenastroenoMT4")
robotrygaetsyaMT4 = types.InlineKeyboardButton("❌ Робот ругается", callback_data="robotrygaetsyaMT4")
backystanovkarobotamt4 = types.InlineKeyboardButton("🔙 Назад", callback_data="backystanovkarobotamt4")
YstanovkarobotaGoMt4.add(vsenastroenoMT4, robotrygaetsyaMT4, backystanovkarobotamt4, Mainmenu)

finalmt4 = types.InlineKeyboardMarkup(row_width=1)
backnachatystanovkyGomt4 = types.InlineKeyboardButton("🔙 Назад", callback_data="backnachatystanovkyGomt4")
finalmt4.add(backnachatystanovkyGomt4, Mainmenu)

robotrugaetsyaMt4 = types.InlineKeyboardMarkup(row_width=1)
robotrugaetsyaMt4.add(backnachatystanovkyGomt4, Mainmenu)
#####################################-ВЫБОР МТ-5-##############################################################################
# Установка MT-5
YstanovkaMt5 = types.InlineKeyboardMarkup(row_width=2)
Xm = types.InlineKeyboardButton("📊 XM", callback_data="Xm")
HF = types.InlineKeyboardButton("📊 HF", callback_data="HF")
roboforex = types.InlineKeyboardButton("📊 Робофорекс", callback_data="roboforex")
ystanovilbrokeramt5 = types.InlineKeyboardButton("✅ Я установил(а) терминал", callback_data="ystanovilbrokeramt5")
backviborterm = types.InlineKeyboardButton("🔙 Назад", callback_data="backviborterm")
YstanovkaMt5.add(Xm, HF)
YstanovkaMt5.add(roboforex)
YstanovkaMt5.add(ystanovilbrokeramt5)
YstanovkaMt5.add(backviborterm)
YstanovkaMt5.add(Mainmenu)
# Видео со скачивания и установкой терминала XM
Xmvid = types.InlineKeyboardMarkup(row_width=1)
backviborterm = types.InlineKeyboardButton("🔙 Назад", callback_data="backystanovkaMT5")
Xmvid.add(backviborterm, Mainmenu)
# Видео со скачивания и установкой терминала HF
HFvid = types.InlineKeyboardMarkup(row_width=1)
backviborterm = types.InlineKeyboardButton("🔙 Назад", callback_data="backystanovkaMT5")
HFvid.add(backviborterm, Mainmenu)
# Видео со скачивания и установкой терминала ROBOFOREX
roboforexvid = types.InlineKeyboardMarkup(row_width=1)
backviborterm = types.InlineKeyboardButton("🔙 Назад", callback_data="backystanovkaMT5")
roboforexvid.add(backviborterm, Mainmenu)

# Настройка терминала МТ-5
Nastroikamt5 = types.InlineKeyboardMarkup(row_width=1)
nastroittermmt5 = types.InlineKeyboardButton("👉 Настроить терминал", callback_data="nastroitterm")
termnastroenmt5 = types.InlineKeyboardButton("✅ Терминал настроен", callback_data="termnastroen")
Nastroikamt5.add(nastroittermmt5, termnastroenmt5, backviborterm, Mainmenu)

# Настроить треминал для МТ5
Nastroikamt5video = types.InlineKeyboardMarkup(row_width=1)
backnastroikatermmt5 = types.InlineKeyboardButton("🔙 Назад", callback_data="backnastroikatermmt5")
Nastroikamt5video.add(backnastroikatermmt5, Mainmenu)

# Установка робота МТ 5
YstanovkarobotaMt5 = types.InlineKeyboardMarkup(row_width=1)
nachatystanovkymt5 = types.InlineKeyboardButton("🛠 Начать установку", callback_data="nachatystanovkymt5")
gotovomt5 = types.InlineKeyboardButton("✅ Готово", callback_data="gotovomt5")
# backviborterm = types.InlineKeyboardButton("🔙 Назад", callback_data="backystanovkaMT5")
YstanovkarobotaMt5.add(nachatystanovkymt5, gotovomt5, backnastroikatermmt5, Mainmenu)

#ВЫбор вашего типа счёта
vibortipascheta = types.InlineKeyboardMarkup(row_width=2)
Cent = types.InlineKeyboardButton("💲 Центовый", callback_data="Cent")
dollar = types.InlineKeyboardButton("💲 Долларовый", callback_data="dollar")
backystanovkarobotamt5 = types.InlineKeyboardButton("🔙 Назад", callback_data="backystanovkarobotamt5")
vibortipascheta.add(Cent,dollar)
vibortipascheta.add(backystanovkarobotamt5)
vibortipascheta.add(Mainmenu)

#vibrali cent
YstanovkarobotaGoMt5cent = types.InlineKeyboardMarkup(row_width=1)
vsenastroenoMT5cent = types.InlineKeyboardButton("✅ Все настроено и работает", callback_data="vsenastroenoMT5cent")
robotrygaetsyaMT5cent = types.InlineKeyboardButton("❌ Робот ругается", callback_data="robotrygaetsyaMT5cent")
backviborscheta = types.InlineKeyboardButton("🔙 Назад", callback_data="backviborscheta")
YstanovkarobotaGoMt5cent.add(vsenastroenoMT5cent, robotrygaetsyaMT5cent,backviborscheta, Mainmenu)
#
final1cent = types.InlineKeyboardMarkup(row_width=1)
backvibralicent = types.InlineKeyboardButton("🔙 Назад", callback_data="backvibralicent")
final1cent.add(backvibralicent, Mainmenu)

# робот ругается
robotrugaetsyaMt5cent = types.InlineKeyboardMarkup(row_width=1)
robotrugaetsyaMt5cent.add(backvibralicent, Mainmenu)

#vibrali dollar
YstanovkarobotaGoMt5dollar = types.InlineKeyboardMarkup(row_width=1)
vsenastroenoMT5dollar = types.InlineKeyboardButton("✅ Все настроено и работает", callback_data="vsenastroenoMT5dollar")
robotrygaetsyaMT5dollar = types.InlineKeyboardButton("❌ Робот ругается", callback_data="robotrygaetsyaMT5dollar")
YstanovkarobotaGoMt5dollar.add(vsenastroenoMT5dollar, robotrygaetsyaMT5dollar)
YstanovkarobotaGoMt5dollar.add(backviborscheta)
YstanovkarobotaGoMt5dollar.add(Mainmenu)

#
final1dollar = types.InlineKeyboardMarkup(row_width=1)
backvibralidollar = types.InlineKeyboardButton("🔙 Назад", callback_data="backvibralidollar")
final1dollar.add(backvibralidollar, Mainmenu)

# робот ругается
robotrugaetsyaMt5dollar1 = types.InlineKeyboardMarkup(row_width=1)
robotrugaetsyaMt5dollar1.add(backvibralidollar, Mainmenu)



