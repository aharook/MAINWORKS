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
  bot.send_message(message.chat.id,f'<b>Привіт ти {message.from_user.first_name}, я ахарук,  хочеш мене протестити?</b>' , parse_mode='HTML')
  

@bot.message_handler(commands=['help'])
def start_message(message):
  bot.send_message(message.chat.id,"Бот, тобто я, створений для тестування, можеш написати мені щось, я відповім на твоє повідомлення.")

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
  elif message.text.lower() == 'пока' or message.text.lower() == 'пака' or message.text.lower() == 'до побачення' or message.text.lower() == 'бувай':
    bot.send_message(message.chat.id, '<b>До побачення!</b>', parse_mode='HTML')
  elif message.text.lower() == 'як тебе звати?':
    bot.send_message(message.chat.id, '<b>Мене звати Ахарук!</b>', parse_mode='HTML')
  elif message.text.lower() == 'що ти вмієш?':
    bot.send_message(message.chat.id, '<b>Я можу відповідати на твої повідомлення та допомагати з різними запитаннями! жарт, тільки говорити, власник нічо не навчив ._.</b>', parse_mode='HTML')
  elif message.text.lower() == 'люблю тебе' or message.text.lower() == 'я тебе люблю' or message.text.lower() == 'ти мені подобаєшся':
    bot.send_message(message.chat.id, '<b>Я теж тебе люблю, але краще пиши автору</b>', parse_mode='HTML')
    bot.send_message(message.chat.id, '<b>Якщо хочеш поспілкуватись з автором, натисни кнопку нижче:</b>', reply_markup=markup, parse_mode='HTML')
  else:
    bot.send_message(message.chat.id, '<b>Я не розумію це повідомлення.</b>', parse_mode='HTML')

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

    bot.send_message(message.chat.id, '<b>Дякую за фото! Але я не можу його переглянути.</b>', parse_mode='HTML')

bot.polling(none_stop=True)