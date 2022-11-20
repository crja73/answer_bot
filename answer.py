from aiogram import Bot, Dispatcher, executor, types
from aiogram import *
from aiogram.types import *


TOKEN = "5331287660:AAEc1XKveaIxM_1l1UeaQtkAGS6ItEpLZTY"
admin_id = 1017470547


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    if message['from'].id == admin_id:
        await message.answer(f"Hi, admin")
    else:
        await message.answer(f"✋Здравствуйте, {message['from'].first_name}, напишите нам ваш вопрос и мы ответим вам в ближайшее время!")

        
@dp.message_handler()
async def process_start_command(message: types.Message):
    if message.reply_to_message == None:
        if '/start' not in message.text:
            await bot.forward_message(admin_id, message.from_user.id, message.message_id)
            f = open('users.txt', "a")
            sms = message.text + ":" + str(message.from_user.id)
            f.write(sms + '\n')
    else:
        try:
            if message.from_user.id == admin_id:
                f = open('users.txt', 'r')
                for i in f.readlines():
                    if message.reply_to_message.text in i:
                        u_id = i.split(':')[1]
                        print(u_id)
                await bot.send_message(u_id, message.text)
            else:
                await message.answer('Нельзя отвечать на сообщения.')
        except Exception as e:
            await bot.send_message(admin_id, e)

            
@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message):
    await bot.forward_message(admin_id, message.from_user.id, message.message_id)

    
@dp.message_handler(content_types=['document'])
async def handle_docs_photo(message):
    await bot.forward_message(admin_id, message.from_user.id, message.message_id)

    
if __name__ == '__main__':
    print("starting")
    executor.start_polling(dp)