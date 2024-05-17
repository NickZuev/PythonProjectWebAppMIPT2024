import os
from pathlib import Path

import asyncio
from simpleeval import simple_eval
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from dotenv import load_dotenv

from .ordinal_numbers import OrdinalNumber
from .converter_to_image import latex_to_img


load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()
ADVICE = (
    "Напиши /add /mult /pow и потом два ординала в КНФ через @, "
    "чтобы получить результат\n"
    "Вот так например: /add w ^ {w ^ {1} + 7} * 9 + w + 1 @ w + 1\n"
    "А можешь написать /eval, а потом выражение с w, +, *, **"
    "(лучше чем ^ из-за того, как Python расставляет приоритеты для операций)"
    ", чтобы получить результат такого выражения\n"
)

async def send_ordinal_number(message, ordinal):
    file_path = f'./{message.from_user.full_name}.png'
    latex_to_img(r'' + ordinal.get_string('latex')).save(file_path)
    await message.answer_photo(FSInputFile(file_path))
    os.remove(file_path)

@dp.message(Command('start'))
async def command_start_handler(message):
    await message.answer(f"Здравствуй, {message.from_user.full_name}!")
    await message.answer(ADVICE)
    await message.answer(
        f"Ты можешь увидеть сообщение выше ещё раз, написав /help"
    )

@dp.message(Command('help'))
async def command_help_handler(message):
    await message.answer(ADVICE)

@dp.message(Command('add'))
async def add_handler(message, command):
    try:
        x, y = map(OrdinalNumber, command.args.split('@'))
    except:
        await message.answer("Упс, попробуй снова!")
        return
    await send_ordinal_number(message, x + y)

@dp.message(Command('mult'))
async def mult_handler(message, command):
    try:
        x, y = map(OrdinalNumber, command.args.split('@'))
    except:
        await message.answer("Упс, попробуй снова!")
        return
    await send_ordinal_number(message, x * y)

@dp.message(Command('pow'))
async def pow_handler(message, command):
    try:
        x, y = map(OrdinalNumber, command.args.split('@'))
    except:
        await message.answer("Упс, попробуй снова!")
        return
    await send_ordinal_number(message, x ^ y)

@dp.message(Command('eval'))
async def eval_handler(message, command):
    try:
        w = OrdinalNumber(1)
        w.deg = OrdinalNumber(1)
        result = simple_eval(command.args, names={'w':w})
    except:
        await message.answer("Упс, попробуй снова!")
        return
    await send_ordinal_number(message, result)

async def main():
    await dp.start_polling(bot)
