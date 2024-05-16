import os
import validators
import requests
import telebot
import yt_dlp
from dotenv import load_dotenv

load_dotenv()
bot_token = os.environ.get('BOT_TOKEN')

if not bot_token:
    raise ValueError("No BOT_TOKEN found.Please set it in the env file")

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['hi', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello, how are you doing?")

@bot.message_handler(commands=['image', 'photo'])
def check_url(message):
    if message.text.startswith('/image ') or message.text.startswith('/photo '):
        url = message.text.split(' ', 1)[1]
        if validators.url(url):

            img_data = requests.get(url).content
            with open('image_name.jpg', 'wb') as handler:
                handler.write(img_data)
            bot.send_photo(message.chat.id, img_data)
        else:
            bot.reply_to(message, "It is not a valid link.")
    else:
        bot.reply_to(message, "Invalid command. Please use /image or /photo followed by a valid URL.")



@bot.message_handler(commands=['video'])
def check_url_video(message):
    url = message.text[7:]
    if validators.url(url):
        options = {'outtmpl' : 'video.%(ext)s', 'format' : 'mp4'}
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
        bot.send_video(message.chat.id, open('video.mp4', 'rb'))
    else:
        bot.reply_to(message, "It is not a valid link.")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()


