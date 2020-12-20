import config 
import logging 

import parser_test 
import bd2
import user_mus
import mymus

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions

import keyboard as kb

import time 
import asyncio
from datetime import datetime

from sqlighter import SQLighter

# задаем уровень логов
logging.basicConfig(level = logging.INFO)
# иниц бота 
bot = Bot(token = config.API_TOKEN)
dp = Dispatcher(bot)

# инициализируем соединение с БД
db = SQLighter('bd.db')

print('Start')
#Ответ на нажатие все кнопки Musbot
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'))
async def process_callback_btn(callback_query: types.CallbackQuery):
	ind = 5
	code = callback_query.data[-1]
	mus = bd2.sq()
	if code.isdigit():
		code = int(code)
	if code == 1:
		ind = 0
	elif code == 2:
		ind = 1
	elif code == 3:
		ind = 2 
	elif code == 4:
		ind = 3
	elif code == 5:
		ind = 4 
	if ind == 5:
		None
	else:
		us(mus[ind])
		inde = "user_"+str(callback_query.from_user.id)
		user_mus.m(inde,mus[ind])
		catain = emojize("Специально для вас:wink:")
		await bot.answer_callback_query(callback_query.id)
		try:
			captain = emojize("Подождите ,пожалуйста, немного:innocent:")
			await bot.send_message(callback_query.from_user.id,captain)
			with open("C:/Users/Шариповы/Downloads/"+parser_test.parser(mus[ind]), 'rb') as voise:
				time.sleep(5)
				await bot.send_audio(callback_query.from_user.id,voise,catain,reply_markup=kb.inline_kb_top_add)
		except:
			try:
				with open("C:/Users/Шариповы/Downloads/"+parser_test.main(mus[ind]), 'rb') as voise:
				 	time.sleep(20)
				 	await bot.send_audio(callback_query.from_user.id,voise,catain,reply_markup=kb.inline_kb_top_add)		
			except:
				captain = emojize("К сожелению ничего не найдено:weary:")
				await bot.send_message(callback_query.from_user.id,captain)

#Ответ на нажатие все кнопки VK
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('vk'))
async def process_callback_btn(callback_query: types.CallbackQuery):
	ind = 5
	code = callback_query.data[-1]
	mus = bd2.vk()
	if code.isdigit():
		code = int(code)
	if code == 1:
		ind = 0
	elif code == 2:
		ind = 1
	elif code == 3:
		ind = 2 
	elif code == 4:
		ind = 3
	elif code == 5:
		ind = 4 
	if ind == 5:
		None
	else:
		us(mus[ind])
		inde = "user_"+str(callback_query.from_user.id)
		user_mus.m(inde,mus[ind])
		catain = emojize("Специально для вас:wink:")
		await bot.answer_callback_query(callback_query.id)
		try:
			captain = emojize("Подождите ,пожалуйста, немного:innocent:")
			await bot.send_message(callback_query.from_user.id,captain)
			with open("C:/Users/Шариповы/Downloads/"+parser_test.parser(mus[ind]), 'rb') as voise:
				time.sleep(5)
				await bot.send_audio(callback_query.from_user.id,voise,catain,reply_markup=kb.inline_kb_top_add)
		except:
			try:
				with open("C:/Users/Шариповы/Downloads/"+parser_test.main(mus[ind]), 'rb') as voise:
				 	time.sleep(20)
				 	await bot.send_audio(callback_query.from_user.id,voise,catain,reply_markup=kb.inline_kb_top_add)		
			except:
				captain = emojize("К сожелению ничего не найдено:weary:")
				await bot.send_message(callback_query.from_user.id,captain)

#Ответ на нажатие все кнопки Itunes
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('it'))
async def process_callback_btn(callback_query: types.CallbackQuery):
	ind = 5
	code = callback_query.data[-1]
	mus = bd2.itunes()
	if code.isdigit():
		code = int(code)
	if code == 1:
		ind = 0
	elif code == 2:
		ind = 1
	elif code == 3:
		ind = 2 
	elif code == 4:
		ind = 3
	elif code == 5:
		ind = 4 
	if ind == 5:
		None
	else:
		us(mus[ind])
		inde = "user_"+str(callback_query.from_user.id)
		user_mus.m(inde,mus[ind])
		catain = emojize("Специально для вас:wink:")
		await bot.answer_callback_query(callback_query.id)
		try:
			captain = emojize("Подождите ,пожалуйста, немного:innocent:")
			await bot.send_message(callback_query.from_user.id,captain)
			with open("C:/Users/Шариповы/Downloads/"+parser_test.parser(mus[ind]), 'rb') as voise:
				time.sleep(5)
				await bot.send_audio(callback_query.from_user.id,voise,catain,reply_markup=kb.inline_kb_top_add)
		except:
			try:
				with open("C:/Users/Шариповы/Downloads/"+parser_test.main(mus[ind]), 'rb') as voise:
				 	time.sleep(20)
				 	await bot.send_audio(callback_query.from_user.id,voise,catain,reply_markup=kb.inline_kb_top_add)		
			except:
				captain = emojize("К сожелению ничего не найдено:weary:")
				await bot.send_message(callback_query.from_user.id,captain)

#Ответ на нажатие History
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('track'))
async def process_callback_btn(callback_query: types.CallbackQuery):
	code = callback_query.data[-1]
	user_id = "user_"+str(callback_query.from_user.id)
	mus = user_mus.pr(user_id)
	if code.isdigit():
		code = int(code)
	catain = emojize("Специально для вас:wink:")
	await bot.answer_callback_query(callback_query.id)
	us(mus[code][:-16])
	try:
		captain = emojize("Подождите ,пожалуйста, немного:innocent:")
		await bot.send_message(callback_query.from_user.id,captain)
		with open("C:/Users/Шариповы/Downloads/"+parser_test.parser(mus[code][:-16]), 'rb') as voise:
			time.sleep(5)
			await bot.send_audio(callback_query.from_user.id,voise,catain,reply_markup=kb.inline_kb_top_add)
	except:
		try:
			with open("C:/Users/Шариповы/Downloads/"+parser_test.main(mus[code][:-16]), 'rb') as voise:
			 	time.sleep(20)
			 	await bot.send_audio(callback_query.from_user.id,voise,catain,reply_markup=kb.inline_kb_top_add)		
		except:
			captain = emojize("К сожелению ничего не найдено:weary:")
			await bot.send_message(callback_query.from_user.id,captain)

#Ответ на нажатие Playlist
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('mus'))
async def process_callback_btn(callback_query: types.CallbackQuery):
	code = callback_query.data[-1]
	user_id = "user_"+str(callback_query.from_user.id)
	mus = mymus.pr(user_id)
	if code.isdigit():
		code = int(code)
	catain = emojize("Специально для вас:wink:")
	await bot.answer_callback_query(callback_query.id)
	await bot.send_message(callback_query.from_user.id,captain)
	with open("C:/Users/Шариповы/Downloads/"+mymus.parser(mus[code]), 'rb') as voise:
		await bot.send_audio(callback_query.from_user.id,voise,catain)
#Ответ на нажатие кнопки подписки
@dp.callback_query_handler(lambda c: c.data == "tr")
async def process_callback_btn(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	if(not db.subscriber_exists(callback_query.from_user.id)):
		# если юзера нет в базе, добавляем его
		db.add_subscriber(callback_query.from_user.id)
	else:
		# если он уже есть, то просто обновляем ему статус подписки
		db.update_subscription(callback_query.from_user.id, True)
	await bot.send_message(callback_query.from_user.id,"Вы успешно подписались на рассылку!\nЖдите, скоро вы узнаете о новых новинках недели.")

#Ответ на нажатие кнопки отписки
@dp.callback_query_handler(lambda c: c.data == 'fal')
async def process_callback_btn(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	if(not db.subscriber_exists(callback_query.from_user.id)):
		# если юзера нет в базе, добавляем его с неактивной подпиской (запоминаем)
		db.add_subscriber(callback_query.id, False)
		await bot.send_message(callback_query.from_user.id,"Вы итак не подписаны.")
	else:
		# если он уже есть, то просто обновляем ему статус подписки
		db.update_subscription(callback_query.from_user.id, False)
		await bot.send_message(callback_query.from_user.id,"Вы успешно отписаны от рассылки.")

#Ответ на нажатие кнопки топ 
@dp.callback_query_handler(lambda c: c.data == "top")
async def process_callback_btn(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	captain = emojize("Топ 5 треков этой недели:")
	await bot.send_message(callback_query.from_user.id,captain,reply_markup=kb.inline_kb_top)

#Ответ на нажатие кнопки топ по MusBot
@dp.callback_query_handler(lambda c: c.data == "top_own")
async def process_callback_btn(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	captain = emojize("Топ треков по версии MusBot:")
	await bot.send_message(callback_query.from_user.id,captain,reply_markup=kb.inline_kb_full)

#Ответ на нажитие кнопки топ по вк
@dp.callback_query_handler(lambda c: c.data == "top_vk")
async def process_callback_btn(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	captain = emojize("Топ треков по версии VK:")
	await bot.send_message(callback_query.from_user.id,captain,reply_markup=kb.inline_kb_vk_mus)

#Ответ на нажатие кнопки топ по itunes
@dp.callback_query_handler(lambda c: c.data == "top_itunes")
async def process_callback_btn(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	captain = emojize("Топ треков по версии Itunes:")
	await bot.send_message(callback_query.from_user.id,captain,reply_markup=kb.inline_kb_itunes_mus)

#Ответ на нажатие кнопки истории
@dp.callback_query_handler(lambda c: c.data == "mymus")
async def process_callback_btn(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	ind = "user_"+str(callback_query.from_user.id)
	kb.mytrack(ind)
	dele(ind)
	try:
		capta = "Трек | Время"
		await bot.send_message(callback_query.from_user.id,capta,reply_markup=kb.mytrack(ind))
	except:
		captains = "История пуста.Напишите  /music  'Название музыки' для поиска трека"
		await bot.send_message(callback_query.from_user.id,captains)

def dele(user):
	#Ответ на нажатие кнопки топ 
	@dp.callback_query_handler(lambda c: c.data == "delet")
	async def process_callback_btn(callback_query: types.CallbackQuery):
		await bot.answer_callback_query(callback_query.id)
		user_mus.dele(user)
		captain = emojize("История успешно очищена")
		await bot.send_message(callback_query.from_user.id,captain)

#Ответ на нажатие кнопки топ по playlist
@dp.callback_query_handler(lambda c: c.data == "playlist")
async def process_callback_btn(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	try:
		captain = emojize("Ваш плейлист:")
		user_id = "user_"+str(callback_query.from_user.id)
		kb.mym(user_id)
		await bot.send_message(callback_query.from_user.id,captain,reply_markup=kb.mym(user_id))
	except:
		captains = "Ваш плейлист пуст"
		await bot.send_message(callback_query.from_user.id,captains)

#Ответ на нажатие Playlist
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('del'))
async def process_callback_btn(callback_query: types.CallbackQuery):
	code = callback_query.data[-1]
	user_id = "user_"+str(callback_query.from_user.id)
	mus = mymus.pr(user_id)
	if code.isdigit():
		code = int(code)
	await bot.answer_callback_query(callback_query.id)
	mymus.dele(user_id,mus[code])
	captains = "Успешно удалено"
	await bot.send_message(callback_query.from_user.id,captains)
		

# Команда активации подписки
@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
	if(not db.subscriber_exists(message.from_user.id)):
		# если юзера нет в базе, добавляем его
		db.add_subscriber(message.from_user.id)
	else:
		# если он уже есть, то просто обновляем ему статус подписки
		db.update_subscription(message.from_user.id, True)
	
	await message.answer("""Вы успешно подписались на рассылку!\n
		Ждите, скоро вы узнаете о новых новинках недели.""")

# Команда отписки
@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
	if(not db.subscriber_exists(message.from_user.id)):
		# если юзера нет в базе, добавляем его с неактивной подпиской (запоминаем)
		db.add_subscriber(message.from_user.id, False)
		await message.answer("Вы итак не подписаны.")
	else:
		# если он уже есть, то просто обновляем ему статус подписки
		db.update_subscription(message.from_user.id, False)
		await message.answer("Вы успешно отписаны от рассылки.")

#Приветствие
@dp.message_handler(commands =['start'])
async def welcome(message:types.Message):
	await message.answer(emojize("Добро пожаловать в MusBot-a :wave:\nДля большей информации напишите  /help"))

#Помощник 
@dp.message_handler(commands = ['help'])
async def help_message(message:types.Message):
	await message.reply(emojize("/music - /music(название музыки):musical_note:\n/subscribe - для подписки на уведомления:white_check_mark:\n/unsubscribe - для отписки от уведомлений:negative_squared_cross_mark:\n/chart - для просмотра плейлистов:collision:"))

#Плелисты
@dp.message_handler(commands = ['chart'])
async def help_message(message:types.Message):
	await message.answer("Плейлисты: ",reply_markup=kb.inline_kb_pl)

#Отправка музыки 
@dp.message_handler(commands = ['music'])
async def mus(message:types.Message):
	a = message.text
	a = a.replace("/music","")
	if (a == ""):
		await message.answer(emojize("Введите название музыки:anguished:"))
	else:
		catain = emojize("Специально для вас:wink:")
		try:
			await message.answer(emojize("Подождите пожалуйста немного:innocent:"))
			await bot.send_message(message.from_user.id,catain,reply_markup=kb.music(a))
			@dp.callback_query_handler(lambda c: c.data and c.data.startswith('serch'))
			async def process_callback_btn(callback_query: types.CallbackQuery):
				code = callback_query.data[-1]
				user_id = "user_"+str(callback_query.from_user.id)
				if code.isdigit():
					code = int(code)
				catain = emojize("Специально для вас:wink:")
				await bot.answer_callback_query(callback_query.id)
				try:
					user_mus.m(user_id,parser_test.pr(a)[code])
					us(parser_test.pr(a)[code])
					captain = emojize("Подождите ,пожалуйста, немного:innocent:")
					await bot.send_message(callback_query.from_user.id,captain)
					with open("C:/Users/Шариповы/Downloads/"+parser_test.parser(parser_test.pr(a)[code]), 'rb') as voise:
						time.sleep(25)
						await bot.send_audio(callback_query.from_user.id,voise,catain,reply_markup=kb.inline_kb_top_add)
				except:
					try:
						with open("C:/Users/Шариповы/Downloads/"+parser_test.main(parser_test.pr(a)[code]), 'rb') as voise:
						 	time.sleep(20)
						 	await bot.send_audio(callback_query.from_user.id,voise,catain,reply_markup=kb.inline_kb_top_add)		
					except:
						captain = emojize("К сожелению ничего не найдено:weary:")
						await bot.send_message(callback_query.from_user.id,captain)
		except:
			await message.answer(emojize("К сожелению ничего не найдено:weary:"))
			
#Ответ на нажатие кнопки топ по add
def us(voise):
	@dp.callback_query_handler(lambda c: c.data == "add")
	async def process_callback_btn(callback_query: types.CallbackQuery):
		vois = voise
		await bot.answer_callback_query(callback_query.id)
		captain = emojize("Успешно добавлено.")
		ind = "user_"+str(callback_query.from_user.id)
		mymus.ma(ind,vois)
		await bot.send_message(callback_query.from_user.id,captain)
		vois = None

#Подписка 
async def scheduled(wait_for):
	while True:	
		await asyncio.sleep(wait_for)
		# получаем список подписчиков бота
		subscriptions = db.get_subscriptions_t()
		for s in subscriptions:
			captain = emojize("Топ 5 треков этой недели:")
			await bot.send_message(s[1],captain,reply_markup=kb.inline_kb_full)

#Рассылка о подписки
async def sub(wait_fo):
	while True:	
		await asyncio.sleep(wait_fo)
		# получаем список подписчиков бота
		subscription = db.get_subscriptions_f()
		for i in subscription:
			captains = "Советуем вам подписаться на рассылку для получения больше хорошей музыки:"
			await bot.send_message(i[1],captains,reply_markup=kb.inline_kb_sub)


# запусе лонг-полинга
if __name__ =='__main__':
	dp.loop.create_task(scheduled(604))
	dp.loop.create_task(sub(604))
	executor.start_polling(dp, skip_updates = True)

