from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackQueryHandler
import requests
import re
import subprocess
import bme280


def cputemp(bot, update): #тепература Цп
    subprocess.call('vcgencmd measure_temp>rasp_cp_temp', shell=True)
    handle = open("rasp_cp_temp", "r") #получаем температуру и записываем в файл
    data = handle.read()
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=data)
    handle.close()
    
def housetemp(bot, update):
    chat_id = update.message.chat_id
    temperature,pressure,humidity = bme280.readBME280All()
    bot.send_message(chat_id=chat_id, text=temperature)


def help(bot, update): #список команд бота
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="/housetemp - температура воздуха")
    bot.send_message(chat_id=chat_id, text="/housevlag - влажность")
    bot.send_message(chat_id=chat_id, text="/housedavl - давление")
    bot.send_message(chat_id=chat_id, text="/cputemp - температура ЦП машины")


    
    
def housevlag(bot, update): #влажность
    chat_id = update.message.chat_id
    temperature,pressure,humidity = bme280.readBME280All()
    bot.send_message(chat_id=chat_id, text=humidity)
    
def housedavl(bot, update): #давление
    chat_id = update.message.chat_id
    temperature,pressure,humidity = bme280.readBME280All()
    pressure=pressure/1.33
    bot.send_message(chat_id=chat_id, text=pressure)



def main():
    updater = Updater('xxxxxxxxxxx') #токен
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('cputemp',cputemp))
    dp.add_handler(CommandHandler('housetemp',housetemp))
    dp.add_handler(CommandHandler('housevlag',housevlag))
    dp.add_handler(CommandHandler('housedavl',housedavl))
    dp.add_handler(CommandHandler('help',help))

    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()



