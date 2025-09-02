import telebot 
import webbrowser
from telebot import types

token = '8194697566:AAGCldkl5smOaPjdxJOX4NYJlJdg_bKDelg'

bot =  telebot.TeleBot(token)

markup = types.InlineKeyboardMarkup()
w_avtor = types.InlineKeyboardButton('Автор', url='https://t.me/aharook')
hide_love = types.InlineKeyboardButton('Приховати закоханість?', callback_data='hide_love')
show_love = types.InlineKeyboardButton('Показати закоханість?', callback_data='show_love')
markup.row(w_avtor)
markup.row(hide_love, show_love)

speak = types.InlineKeyboardMarkup()
yes_button = types.InlineKeyboardButton('Так', callback_data='yes')
no_button = types.InlineKeyboardButton('Ні', callback_data='no')
speak.row(yes_button, no_button)
@bot.callback_query_handler(func=lambda callback: True)
def callback_query_handler(callback):
    if callback.data == 'yes':
        bot.answer_callback_query(callback.id, 'Ти натиснув "Так"!')
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='УРА! Давай поспілкуємось, запитай в мене щось)', reply_markup=None)
    elif callback.data == 'no':
        bot.answer_callback_query(callback.id, 'Ти натиснув "Ні"!')
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='Добре, якщо передумаєш, дай знати!', reply_markup=None)
@bot.callback_query_handler(func=lambda callback: True)
def callback_query_handler(callback):
    if callback.data == 'hide_love':
        bot.answer_callback_query(callback.id, 'Закоханість прихована!')
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='Закоханість прихована!', reply_markup=None)
    elif callback.data == 'show_love':
        bot.answer_callback_query(callback.id, 'Закоханість показана!')
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='Якщо хочеш поспілкуватись з автором, натисни кнопку нижче:', reply_markup=markup)

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,f'<b>Привіт ти {message.from_user.first_name}, я ахарук,  хочеш мене протестити?</b>',  reply_markup = speak , parse_mode='HTML')

@bot.message_handler(commands=['author'])
def author_message(message):
  bot.send_message(message.chat.id, '<b>Автор бота: Ахарук</b>', parse_mode='HTML')
  bot.send_message(message.chat.id, '<b>Якщо хочеш поспілкуватись з автором, натисни кнопку нижче:</b>', reply_markup=markup, parse_mode='HTML') 

@bot.message_handler(commands=['help'])
def start_message(message):
  bot.send_message(message.chat.id,"Бот, тобто я, створений для тестування, можеш написати мені щось, я відповім на твоє повідомлення.")
  bot.send_message(message.chat.id, '<b>Основні фрази, які розуміє бот:\n Привіт, \n Як справи, \n як тебе звати, \n що ти вмієш, \n столяр гей?</b>', reply_markup=markup, parse_mode='HTML')

@bot.message_handler(commands=['web', 'webbrowser','site', 'github'])
def webbrowser_message(message):
  bot.send_message(message.chat.id, '<b>Відкриваю сайт...</b>', parse_mode='HTML')
  webbrowser.open('https://github.com/aharook/MAINWORKS')

@bot.message_handler()
def text_user(message):
  if message.text.lower() == 'привіт':
    bot.send_message(message.chat.id, f'<b>Привіт, {message.from_user.first_name}!</b>', parse_mode='HTML')
  elif message.text.lower() == 'як справи?':
    bot.send_message(message.chat.id, '<b>Все добре, дякую!</b>', parse_mode='HTML')
  elif message.text.lower() == 'як настрій?' or message.text.lower() == 'як ти?' or message.text.lower() == 'як ти почуваєшся?' or message.text.lower() == 'як ти справи?':
    bot.send_message(message.chat.id, '<b>Все добре, почуваю себе прекрасно, як завжди впринципі, дякую!</b>', parse_mode='HTML')
  elif message.text.lower() == 'пока' or message.text.lower() == 'пака' or message.text.lower() == 'до побачення' or message.text.lower() == 'бувай':
    bot.send_message(message.chat.id, '<b>До побачення!</b>', parse_mode='HTML')
  elif message.text.lower() == 'як тебе звати?':
    bot.send_message(message.chat.id, '<b>Мене звати Ахарук!</b>', parse_mode='HTML')
  elif message.text.lower() == 'що ти вмієш?' or message.text.lower() == 'що ти можеш?' or message.text.lower() == 'що ти вмієш робити?':
    bot.send_message(message.chat.id, '<b>Я можу відповідати на твої повідомлення та допомагати з різними запитаннями! жарт, тільки говорити, власник нічо не навчив ._.</b>', parse_mode='HTML')
  elif message.text.lower() == 'люблю тебе' or message.text.lower() == 'я тебе люблю' or message.text.lower() == 'ти мені подобаєшся':
    bot.send_message(message.chat.id, '<b>Я теж тебе люблю, але краще пиши автору</b>', parse_mode='HTML')
    bot.send_message(message.chat.id, '<b>Якщо хочеш поспілкуватись з автором, натисни кнопку нижче:</b>', reply_markup=markup, parse_mode='HTML')
  elif message.text.lower() == 'хочу поспілкуватись з автором' or message.text.lower() == 'хочу поговорити з автором' or message.text.lower() == 'хочу зв\'язатись з автором':
    bot.send_message(message.chat.id, '<b>Якщо хочеш поспілкуватись з автором, натисни кнопку нижче:</b>', reply_markup=markup, parse_mode='HTML')
  elif message.text.lower() == 'хочу поговорити з тобою' or message.text.lower() == 'хочу поспілкуватись з тобою':
    bot.send_message(message.chat.id, '<b>Добре, давай поспілкуємось! Ти можеш запитати мене про що завгодно.</b>', parse_mode='HTML')
    bot.send_message(message.chat.id, '<b>Хочеш поговорити зі мною? Натисни "Так" або "Ні".</b>', reply_markup=speak, parse_mode='HTML')
  elif message.text.lower() == 'погода' or message.text.lower() == 'яка погода?' or message.text.lower() == 'погода сьогодні':
    bot.send_message(message.chat.id, '<b>На жаль, я не можу надати інформацію про погоду, але ти можеш перевірити її на сайті погоди.</b>', parse_mode='HTML')
  elif message.text.lower() == 'столяр гей?' or message.text.lower() == 'Столяр гей?':
    bot.send_message(message.chat.id, '<b>Це питання не зовсім коректне.(так) Краще запитай про щось інше.</b>', parse_mode='HTML')
  else:
    bot.send_message(message.chat.id, '<b>Я не розумію це повідомлення</b>', parse_mode='HTML')

@bot.message_handler(content_types=['photo', 'document', 'video', 'audio'])
def handle_media(message):
    if message.content_type == 'photo':
        bot.send_message(message.chat.id, '<b>Дякую за фото! Але я не можу його переглянути.</b>', parse_mode='HTML')
    elif message.content_type == 'document':
        bot.send_message(message.chat.id, '<b>Дякую за документ! Але я не можу його переглянути.</b>', parse_mode='HTML')
    elif message.content_type == 'video':
        bot.send_message(message.chat.id, '<b>Дякую за відео! Але я не можу його переглянути.</b>', parse_mode='HTML')
    elif message.content_type == 'audio':
        bot.send_message(message.chat.id, '<b>Дякую за аудіо! Але я не можу його прослухати.</b>', parse_mode='HTML')

bot.polling(none_stop=True)