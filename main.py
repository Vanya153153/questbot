import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import time
from Info import s, answ
from peremen import *
from Players import user_data, file_user_id



bot = telebot.TeleBot(API_TOKEN)

markup = ReplyKeyboardMarkup(resize_keyboard=True) # заготовка для клавиатуры
markup.add(KeyboardButton('/start'))
markup.add(KeyboardButton('/help'))
markup.add(KeyboardButton('/start_quest'))


tumb = False
knuz = False

#Обявление комманд
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.from_user.id
    user_nm = message.from_user.first_name
    file_user_id(user_nm, user_id)
    bot.send_message(message.chat.id, f'Приветствую {user_nm}! Я квест-бот с детективным сюжетом', reply_markup=markup)
    bot.send_message(message.chat.id, 'Что-бы начать используй команду "start_quest", или посмотри что могу через комманду "help"', reply_markup=markup)



@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Вот мои комманды: \n"
                     "/start: Комманда запускающая меня.\n"
                     "/help: Комманда показывающая что я могу.\n"
                     "/start_quest: Комманда запускающая квест.")


def next_txt(message, n):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)  # заготовка для клавиатуры
    for i in answ[n]:
        markup.add(KeyboardButton(i))

    bot.send_message(message.chat.id, s[n][f'ttx{n+1}'], reply_markup=markup)
    mesg = bot.send_message(message.chat.id, 'Выберете кнопку')

def yes_or_not(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)  # заготовка для клавиатуры
    markup.add(KeyboardButton("Да"))
    markup.add(KeyboardButton("Нет"))
    mesg = bot.send_message(message.chat.id, 'Выберете кнопку', reply_markup=markup)




@bot.message_handler(commands=['start_quest'])
def save_age(message):
    img = open('кабинет в начале.png', 'rb')
    bot.send_message(message.chat.id, "Начинаю квест:")
    time.sleep(2)
    bot.send_photo(message.chat.id, img)
    next_txt(message, 0)
    bot.register_next_step_handler(message, choise1)

def choise1(message):
    global take_tabl
    if message.text == "Брать":
        take_tabl = True
        bot.send_message(message.chat.id, "Вы решили взять снотворное, вдруг понадобятся...")
        time.sleep(1)
        img = open("Улица на подходе.png", 'rb')
        bot.send_photo(message.chat.id, img)
        next_txt(message, 1)
        bot.register_next_step_handler(message, choise2)
    elif message.text == "Не брать":
        take_tabl = False
        bot.send_message(message.chat.id, "Вы решили не брать снотворное, Зачем оно вам на работе ?")
        time.sleep(1)
        img = open("Улица на подходе.png", 'rb')
        bot.send_photo(message.chat.id, img)
        next_txt(message, 1)
        bot.register_next_step_handler(message, choise2)
    elif message.text == "/start_quest" or message.text == "/help" or message.text == "/start":
        bot.send_message(message.chat.id, "Нажмите на комманду ещё раз")
    else:
        bot.send_message(message.chat.id, f"Вы ввели что-то не то ")

def choise2(message):
    global trust
    global uliki

    if message.text == "Исключить показания 1-ого и 2-ого":
        trust = False
        bot.send_message(message.chat.id, "Вы решили исключить показания 1-ого и 2-ого соседа, может они сговорились ? "
                                          "Вы сказали своим коллегам Джону и Ларри исключить показания 1-ого и 2-ого соседа.")
        time.sleep(1)
        next_txt(message, 2)
        bot.register_next_step_handler(message, choise3)

    elif message.text == "Исключить показания 3-го":
        trust = True
        uliki += 1
        bot.send_message(message.chat.id, "Вы решили исключить показания 3-его соседа, уж слишком отличаются его показания от "
                                          "отчёта и других показаний. Вы сказали своим коллегам Джону и Ларри исключить "
                                          "показания 3-его соседа. Вы вспомнили слова 1-ого и 2-ого соседа о том что "
                                          "было слышно несколько криков, может это была какая-нибудь организация ?")
        time.sleep(1)
        next_txt(message, 2)
        bot.register_next_step_handler(message, choise3)
    elif message.text == "/start_quest" or message.text == "/help" or message.text == "/start":
        bot.send_message(message.chat.id, "Нажмите на комманду ещё раз")
    else:
        bot.send_message(message.chat.id, f"Вы ввели что-то не то ")

def choise3(message):
    global take_tabl
    global uliki
    img = open("ванная.png", 'rb')
    bot.send_photo(message.chat.id, img)
    img2 = open("гостиная.png", 'rb')
    if take_tabl == True:
        bot.send_message(message.chat.id, tb1)
        bot.send_message(message.chat.id, "Выходя из ванной вы услышали как \"прыгает\" в вашем внутреннем кормане снотворное"
                                          "достав его что-бы переложить вдругой карман, вы вспомнили что видили что-то по"
                                          "хожее на полке в ванной. Осмотрев полку вы нашли такое-же снотворное, но как?"
                                          "Ведь его не выпускают уже около года, а в последний раз оно продавалось в аптеке"
                                          "которая заброшенна уже год, на даннй момент там база новой преступной организации."
                                          "Может Кевин был с ними связан ? Запомнив эту связь вы повернулись к выходу из неё")
        bot.send_message(message.chat.id, tabl_insedent)
        time.sleep(1)
        uliki += 1
        bot.send_photo(message.chat.id, img2)
        next_txt(message, 3)
        bot.register_next_step_handler(message, choise4)
    elif take_tabl == False:
        bot.send_message(message.chat.id, tb1)
        bot.send_message(message.chat.id, "Осмотрев всю ванную вы не нашли каких-либо улик и решили пойти к месту проишествия")
        time.sleep(3)
        bot.send_message(message.chat.id, tabl_insedent)
        time.sleep(1)
        bot.send_photo(message.chat.id, img2)
        next_txt(message, 3)
        bot.register_next_step_handler(message, choise4)
    elif message.text == "/start_quest" or message.text == "/help" or message.text == "/start":
        bot.send_message(message.chat.id, "Нажмите на комманду ещё раз")
    else:
        bot.send_message(message.chat.id, f"Вы ввели что-то не то ")

def choise4(message):
    global ch_good
    global uliki
    global conv
    global tumb
    global knuz
    img1 = open("шкаф.png", 'rb')
    img2 = open("конверт.png", 'rb')
    img3 = open("конверт без змеи.png", 'rb')
    img4 = open("тумбочка.png", 'rb')
    if message.text == "Попросить Джона осмотреть тумбочку":
        if uliki == 2:
            conv = True
            tumb = True
            ch_good = True
            uliki += 2
            bot.send_message(message.chat.id,
                             "Вы сказали Джону, что надо всё внимательно осмотреть, не упуская ни единой детали")
            bot.send_photo(message.chat.id, img1)
            bot.send_message(message.chat.id, convert_answer)
            bot.send_photo(message.chat.id, img2)
            bot.send_message(message.chat.id,
                             "но пока вам пришла на ум одна организация \"Клык\", это та самая организация "
                             "которая занила заброшенное здание аптеки. Кевин был из этой организации ? "
                             "И если, то его убили из-за внутренней разборки ? или что-то ещё ? Но надо узнать что "
                             "выяснил Джон.")
            time.sleep(4)
            next_txt(message, 4)
            bot.register_next_step_handler(message, choise5)
        elif uliki == 1:
            uliki += 1
            tumb = True
            bot.send_photo(message.chat.id, img1)
            bot.send_message(message.chat.id, """Джон кивнув начинает осматривать тумбочку, а вы в свои очередь пошли осматривать книжную полку. 
Пододходя к ней вы заметили что она довольно пыльная, будто она явно указывала на то что её давно не трогали. 
Начав её изучать вы поняли, что из всех полок только на одной полке нехватает книги, изучая это место вы просунули руку 
вглубь и нащупали конверт где были пакетиков запрещенных, поставки в этом районе осуществляет только одна 
организация - \"Клык\". Осмотрев дальше вы больше ничего не нашли и вы решили узнать как там дела у Джона""")
            bot.send_photo(message.chat.id, img3)
            next_txt(message, 4)
            bot.register_next_step_handler(message, choise5)
        elif uliki == 0:
            ch_good = False
            tumb = True
            bot.send_message(message.chat.id,
                             "Джон кивнув начинает осматривать тумбочку, а вы в свои очередь пошли осматривать "
                             "книжную полку. пододходя к ней вы заметили что она довольно пыльная, будто она "
                             "явно указывала на то что её давно не трогали. Начав её изучать вы поняли, что из "
                             "всех полок только на одной полке нехватает книги, изучая это место вы ничего не нашли "
                             "осмотерв всю полку вы ничего не нашли и решили узнать что там у Джона")
            time.sleep(4)
            next_txt(message, 4)
            bot.register_next_step_handler(message, choise5)

        else:
            bot.send_message(message.chat.id, f"Вы ввели что-то не то ")

    elif message.text == "Попросить Джона осмотреть книжную полку":
        knuz = True
        if uliki == 2:
            uliki += 1
            bot.send_message(message.chat.id, tumb_secret)
            bot.send_photo(message.chat.id, img4)
            bot.send_message(message.chat.id,
                             "Но из-за подозрений в связи Кевина с какой-либо организацией вы решили осмотреть "
                             "всё по внимательней, и открыв 2 ящика сразу вы опять услышали щелчёк, и внимательно "
                             "осмотрев последний открытый ящик вы заметили у ящика сверху 2-ое дно ! Посмотрев "
                             "что там вы нашли небольшой пакетик с запрещенными веществами с знаком змеи, такие знаки"
                             "оставляет, та новая организация \"Клык\", это явно передача для продажи, но... здесь ? Может"
                             "умерший был связанн с этой организацией ? осмотрев всё что можно"
                             "было вы больше ничего не нашли, и вы решили посмотреть, как там дела у Джона ")
            ch_good = True
            time.sleep(4)
            bot.send_photo(message.chat.id, img2)
            next_txt(message, 4)
            bot.register_next_step_handler(message, choise5)
        elif uliki == 1:
            uliki += 1
            bot.send_photo(message.chat.id, img4)
            bot.send_message(message.chat.id, tumb_secret)
            bot.send_photo(message.chat.id, img3)
            bot.send_message(message.chat.id, """Ещё вы нашли конверт где были пакетиков запрещенных, поставки в этом 
            районе осуществляет только одна организация - \"Клык\". Осмотрев дальше вы больше ничего не нашли и вы 
            решили узнать как там дела у Джона""")
            next_txt(message, 4)
            bot.register_next_step_handler(message, choise5)
        elif uliki == 0:
            bot.send_photo(message.chat.id, img4)
            bot.send_message(message.chat.id, tumb_secret)
            ch_good = False
            time.sleep(4)
            next_txt(message, 4)
            bot.register_next_step_handler(message, choise5)
        else:
            bot.send_message(message.chat.id, f"Вы ввели что-то не то ")
    elif message.text == "/start_quest" or message.text == "/help" or message.text == "/start":
        bot.send_message(message.chat.id, "Нажмите на комманду ещё раз")
    else:
        bot.send_message(message.chat.id, f"Вы ввели что-то не то ")


def choise5(message):
    img = open("разговор.png", 'rb')
    bot.send_photo(message.chat.id, img)
    if tumb == True:
        if uliki == 4:
            bot.send_message(message.chat.id, answ_jhon)
            bot.send_message(message.chat.id, "Вы сразу же хотели начать говорить о найденных уликах, но... стоит ли ?"
                                              "Из-за найденных улик и того конверта и той подписи на нём - \"Д.\"..."
                                              "Нужно ли спросить Джона об конверете ?")
            time.sleep(4)
            yes_or_not(message)
            bot.register_next_step_handler(message, tell_jhon_good)
        elif uliki == 2:
            bot.send_message(message.chat.id, answ_jhon)
            bot.send_message(message.chat.id, "Вы рассказали Джону, что нашли несколько улик указывающих на то, что это"
                                              "могла быть организация \"Клык\", и скорее всего это была междуусобица"
                                              "между членами организации.")
            good_end(message)
        elif uliki == 0:
            bot.send_message(message.chat.id, answ_jhon)
            bot.send_message(message.chat.id, "Вы рассказали Джону, что ничего не смогли выяснить, он сказал , что вас вызывают"
                                              "начал ещё раз осмотрить комнату. ВЫ вышли из квартиры")
            bad_end(message)
        elif message.text == "/start_quest" or message.text == "/help" or message.text == "/start":
            bot.send_message(message.chat.id, "Нажмите на комманду ещё раз")
        else:
            bot.send_message(message.chat.id, f"Вы ввели что-то не то ")
    elif knuz == True:
        if uliki == 3:
            bot.send_message(message.chat.id, answ_jhon)
            bot.send_message(message.chat.id, "Вы рассказали Джону, что нашли несколько улик указывающих на то, что это"
                                              "могла быть организация \"Клык\", и скорее всего это была междуусобица"
                                              "между членами организации.")
            good_end(message)
        elif uliki == 2:
            bot.send_message(message.chat.id, answ_jhon)
            bot.send_message(message.chat.id, "Вы рассказали Джону, что нашли несколько улик указывающих на то, что это"
                                              "могла быть организация \"Клык\", и скорее всего это была междуусобица"
                                              "между членами организации.")
            good_end(message)
        elif uliki == 0:
            bot.send_message(message.chat.id, answ_jhon)
            bot.send_message(message.chat.id, "Вы рассказали Джону, что ничего не смогли выяснить, он сказал , что вас вызывают"
                                              "начал ещё раз осмотрить комнату. ВЫ вышли из квартиры")
            bad_end(message)
        elif message.text == "/start_quest" or message.text == "/help" or message.text == "/start":
            bot.send_message(message.chat.id, "Нажмите на комманду ещё раз")
        else:
            bot.send_message(message.chat.id, f"Вы ввели что-то не то ")
    elif message.text == "/start_quest" or message.text == "/help" or message.text == "/start":
        bot.send_message(message.chat.id, "Нажмите на комманду ещё раз")
    else:
        bot.send_message(message.chat.id, f"Вы ввели что-то не то ")

#Варианты с шкафом
def tell_jhon_good(message):
    if message.text == "Да":
        bot.send_message(message.chat.id, answ_yes)
        vbad_end(message)
    elif message.text == "Нет":
        bot.send_message(message.chat.id, answ_no)
        vgood_end(message)
    elif message.text == "/start_quest" or message.text == "/help" or message.text == "/start":
        bot.send_message(message.chat.id, "Нажмите на комманду ещё раз")
    else:
        bot.send_message(message.chat.id, f"Вы ввели что-то не то ")



#Концовки
def vbad_end(message):
    #Вас убили
    bot.send_message(message.chat.id, """Вы умерли - Плохая концовка, а ведь вы добрались до тайны, но не смогли 
    ничего сделать..., как резко раздался сильный звук часов, и вы были поглащенны бездной и отправленны на день назад 
    забыв об этом и вчерашнем дне... . Спасибо, что поиграли в мой квест !""")
    global uliki
    uliki = 0



def bad_end(message):
    #Вы не нашли улик
    global uliki
    uliki = 0
    bot.send_message(message.chat.id, answ_jhon)
    img = open("кабинет после.png", 'rb')
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id,  """Выйдя из квартиры вы сообщили Ларри и Джону о том, что пойдёте в участок и отсчитаетесь.
    Пойдя в участок и отсчитавшись вам заплатили, но вам всё равно было гадко от того
    что вы не смогли выяснить хоть что-нибудь. Идя обратно в офис под громкий звук всё ещё усиливующегося дождя вы 
    подумали - что следующее дело будет гораздо лучше ! Зайдя в кабинет он казался другим , но из-за слишком сильной усталости вы это не заметили, 
    скинули своё пальто и село подремать в кресло, 
    ожидаемо вы быстро уснули и решили посмотреть как велось это дело, как резко раздался щелчёк со стороны дверы, 
    нахмурив брови вы подумали ,что это всё просто случайно всё повторилось и нахмурив брови вы спросили "Опять ?", ваш 
    помошник молча кивнув положил вам на стол папку о только поступившем деле о найденном трупе. Это было тоже самое дело 
    ,что и вчера... Непоняв что происходит вы посмотрели на своего помошника, но его уже не было на месте, как резко 
    раздался сильный звук часов, подумав - \"Что происходит ?\" - вы были поглащенны бездной и отправленны на день назад 
    забыв об этом и вчерашнем дне...""")
    bot.send_message(message.chat.id, """Вы ничего не выяснили - Плохая концовка, может на следующем кругу будет лучше ?
    Спасибо, что поиграли в мой квест !""")

def good_end(message):
    #Вы нашли все или почти все улики ,но не нашли предателя
    global uliki
    uliki = 0
    img = open("кабинет после.png", 'rb')
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id,  """Выйдя из квартиры вы сообщили Ларри и Джону о том, что пойдёте в участок и отсчитаетесь.
    Когда вы шли под дождём вы всё ещё продолжали думать об этом деле, может вы что-то упустили ?, или чего-то не поняли ?
    Думая об этом вы незаметно для себя пришли к участку. Зайдя вы быстро написали отчёт о том что это дело рук \"Клыка\"
    , и дождавшись его одобрения вы получили свою награду. Идя обратно в офис под громкий звук всё ещё усиливующегося дождя вы 
    подумали - \"Я сделал всё что мог ? Или были другие варианты ?\" -отметая эти мысли в сторону вы дошли до офиса. Зайдя
    в кабинет вы скинули своё пальто и село подремать в кресло, ожидаемо вы быстро уснули и решили посмотреть как велось это дело
    , как резко раздался щелчёк со стороны дверы, нахмурив брови вы подумали ,что это всё просто случайно всё повторилось 
    и нахмурив брови вы спросили "Опять ?", ваш помошник молча кивнув положил вам на стол папку о только поступившем 
    деле о найденном трупе. Это было тоже самое дело ,что и вчера... Непоняв что происходит вы посмотрели на своего помошника
    , но его уже не было на месте, как резко раздался сильный звук часов, подумав - \"Что происходит ?\" - вы были поглащенны бездной
    и отправленны на день назад забыв об этом и вчерашнем дне...""")
    bot.send_message(message.chat.id, "Вы раскрыли дело, но поняв, что все это время вы были в петле времени, вас затянуло на новый круг"
                                      "- Хорошая концовка. Спасибо, что поиграли в мой квест !")


def vgood_end(message):
    # Вы нашли все улики и предателя
    global uliki
    uliki = 0
    img = open("кабинет после.png", 'rb')
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, """Выйдя из квартиры вы сообщили Ларри и Джону о том, что пойдёте в участок и отсчитаетесь.
    Поняв, что в этом деле Джон может быть, убийцей, вы сказали ему , что ничего не нашли, из-за этого вы решили уйти 
    из квартиры как можно быстрее. Быстро дойдя до полицейского отделения вы объяснили всю ситуацию и показав достаточное 
    количество улик, поверив вам полиция взяла Джону под стражу, и как позже выяснилось это всё оказалось правдой попращавшись 
    со всеми в участке вы пошли обратно в офис под громкий звук всё ещё усиливующегося дождя. Зайдя в кабинет вы скинули 
    своё пальто и село подремать в кресло, ожидаемо вы быстро уснули и решили посмотреть как велось это дело, как резко 
    раздался щелчёк со стороны дверы, нахмурив брови вы подумали ,что это всё просто случайно всё повторилось и нахмурив 
    брови вы спросили "Опять ?", ваш помошник молча кивнув положил вам на стол папку о только поступившем деле о найденном 
    трупе. Это было тоже самое дело ,что и вчера... Непоняв что происходит вы посмотрели на своего помошника, но его уже 
    не было на месте, как резко раздался сильный звук часов, подумав - \"Что происходит ?\" - вы были поглащенны бездной
    и отправленны на день назад забыв об этом и вчерашнем дне...""")
    bot.send_message(message.chat.id, """Поздравляю вы нашли все улики и вычеслили предателя, но вас всё равно затянуло в петлю
    - Лучшая концовка. Спасибо, что поиграли в мой квест !""")

#Реакция на весь остальной текст
@bot.message_handler(content_types=['text'])
def say_hello(message):
    bot.send_message(message.chat.id, "Здравствуйте ! Я пока не знаю что вы хотите сказать мне, но вы можете вызвать эти комманд\n"
                                      "/start\n"
                                      "/help\n"
                                      "/start_quest")

bot.polling(none_stop=True)