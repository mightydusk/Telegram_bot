from telegram.ext import Updater,CommandHandler
from Adafruit_IO import Client, Data
import os
x = os.getenv('x') # ADAFRUIT_IO_USERNAME
y = os.getenv('y') # ADAFRUIT_IO_KEY
z = os.getenv('z')  # TELEGRAM_BOT_TOKEN


def on(bot,update):
    chat_id=update.message.chat_id
    bot.send_photo(chat_id,photo='https://stilettodreams.files.wordpress.com/2012/05/light-bulb.jpg')
    bot.send_message(chat_id,text="Led is on")
    aio = Client(x,y)
    value=Data(value=1)
    value_send=aio.create_data('lightbot',value)


def off(bot,update):
    chat_id=update.message.chat_id
    bot.send_photo(chat_id,photo='https://toppng.com/uploads/preview/light-bulb-on-off-png-11553940208oq66nq8jew.png')
    bot.send_message(chat_id,text="Led is off")
    aio = Client(x,y)
    value=Data(value=0)
    value_send=aio.create_data('lightbot',value)

u=Updater(z)
dp=u.dispatcher
dp.add_handler(CommandHandler('turnon',on))
dp.add_handler(CommandHandler('turnoff',off))
u.start_polling()
u.idle()
