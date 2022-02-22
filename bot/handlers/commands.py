from main import bot, dp, anti_flood
from aiogram.types import Message
from tools import sql
from config import admin_id
from tools.modeles import Answers


@dp.message_handler(commands=['start'])
@dp.throttled(anti_flood, rate=5)
async def start_message(message: Message):
    return await bot.send_message(message.from_user.id, text='Hello, world!')


@dp.message_handler(lambda x: x.from_user.id == admin_id, commands=['add'])
@dp.throttled(anti_flood, rate=5)
async def add_new_task(message: Message):
    text = message.text.replace('/add ', '')
    text = text.split('[r]')
    if 3 < len(text) < 2:
        return await bot.send_message(message.from_user.id, text="Разделение это - [r]")
    title, task = text[0], text[1]
    if len(text) == 2:
        sql.add_new_task(title, task)
    elif len(text) == 3:
        sql.add_new_task(title, task, text[2])
    return await bot.send_message(message.from_user.id, text="Ну все ок получается.")


@dp.message_handler(lambda x: x.from_user.id == admin_id, commands=['vis'])
@dp.throttled(anti_flood, rate=5)
async def change_vis(message: Message):
    text = message.text.replace('/vis ', '').split()
    if not len(text) == 2:
        return await bot.send_message(message.from_user.id, text="Тут надо таск id и 1 если в мэин 2 в архив 0 скрыть")
    task_id = text[0]
    visibility = text[1]
    sql.update_visibility(task_id, visibility)
    return await bot.send_message(message.from_user.id, text="Ну все ок получается.")


@dp.message_handler(lambda x: x.from_user.id == admin_id, commands=['ans'])
@dp.throttled(anti_flood, rate=5)
async def get_answers(message: Message):
    task_id = message.text.replace('/ans ', '')
    answers: list[Answers] = sql.get_tasks_by_id(task_id)
    text = f"Ответы на задачу #{task_id}\n\n"
    await bot.send_message(message.from_user.id, text=text)
    for i in answers:
        text = f'Ответ: {i.id} {i.first_name} {i.last_name}\n\n{i.answer}'
        try:
            await bot.send_message(message.from_user.id, text=text)
        except Exception as ex:
            print(ex)
    return await bot.send_message(message.from_user.id, text='Ответы закончились')


@dp.message_handler(lambda x: x.from_user.id == admin_id, commands=['ans_l'])
@dp.throttled(anti_flood, rate=5)
async def get_answers_by_last_name(message: Message):
    msg = message.text.replace('/ans_l ', '').split()

    if len(msg) == 2:
        answers: list[Answers] = sql.get_tasks_by_last_name(msg[0], int(msg[1]))
    else:
        answers: list[Answers] = sql.get_tasks_by_last_name(msg[0])

    text = f"Ответы {answers[0].first_name} {answers[0].last_name}\n\n"
    await bot.send_message(message.from_user.id, text=text)

    for i in answers:
        text = f'Ответ: {i.id} Задача: {i.task_id}\n\n{i.answer}'
        try:
            await bot.send_message(message.from_user.id, text=text)
        except Exception as ex:
            print(ex)
    return await bot.send_message(message.from_user.id, text='Ответы закончились')


@dp.message_handler(lambda x: x.from_user.id == admin_id, commands=['best'])
@dp.throttled(anti_flood, rate=5)
async def change_vis(message: Message):
    answer_id = message.text.replace('/best ', '')
    sql.update_best_answer(answer_id)
    return await bot.send_message(message.from_user.id, text="Ну все ок получается.")
