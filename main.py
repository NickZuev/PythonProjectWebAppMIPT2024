from src.ordinal_numbers import OrdinalNumber
import nest_asyncio
import asyncio
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold


TOKEN = "6838501730:AAFx20s9slB4FZfIb9Yd6k0ZaUEGznljdPc"


bot = Bot(token=TOKEN)
dp = Dispatcher()
current_ordinals = []

@dp.message(Command('start'))
async def command_start_handler(message):
    await message.answer(f"Здравствуй, {message.from_user.full_name}!")

@dp.message(Command('help'))
async def command_help_handler(message):
    await message.answer(
        "Введи ординалы в правильном формате через запятую, "
        "а потом выбери действие"
    )

@dp.message(Command('add'))
async def add_handler(message):
    print("Addition was called with parameters:")
    print("First: " + str(current_ordinals[0]))
    print("Second: " + str(current_ordinals[1]))
    print("Result: " + str(current_ordinals[0] + current_ordinals[1]))
    await message.answer(str(current_ordinals[0] + current_ordinals[1]))

@dp.message(Command('mult'))
async def mult_handler(message):
    print("Multiplince was called with parameters:")
    print("First: " + str(current_ordinals[0]))
    print("Second: " + str(current_ordinals[1]))
    print("Result: " + str(current_ordinals[0] * current_ordinals[1]))
    await message.answer(str(current_ordinals[0] * current_ordinals[1]))

@dp.message(Command('pow'))
async def pow_handler(message):
    print("Power was called with parameters:")
    print("First: " + str(current_ordinals[0]))
    print("Second: " + str(current_ordinals[1]))
    print("Result: " + str(current_ordinals[0] ^ current_ordinals[1]))
    await message.answer(str(current_ordinals[0] ^ current_ordinals[1]))

@dp.message(Command('current'))
async def echo_handler(message):
    await message.answer(
        str(current_ordinals[0]) + '\n' + str(current_ordinals[1])
    )

@dp.message()
async def setting_on_handler(message):
    try:
        global current_ordinals
        current_ordinals = list(map(OrdinalNumber, message.text.split(',')))
        await message.answer(
            str(current_ordinals[0]) + '\n' + str(current_ordinals[1])
        )
    except:
        await message.answer("Упс, что-то пошло не так, попробуй снова!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())