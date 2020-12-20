import bd2
import mymus
import user_mus
import parser_test

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

mus = bd2.sq()
itunes_mus = bd2.itunes()
vk_mus = bd2.vk()

#Настройка
inline_kb_full = InlineKeyboardMarkup(row_width=1).add()
inline_kb_sub = InlineKeyboardMarkup(row_width=2).add()
inline_kb_pl = InlineKeyboardMarkup(row_width=1).add()
inline_kb_vk_mus = InlineKeyboardMarkup(row_width=1).add()
inline_kb_itunes_mus = InlineKeyboardMarkup(row_width=1).add()
inline_kb_top = InlineKeyboardMarkup(row_width=1).add()
inline_kb_top_add = InlineKeyboardMarkup(row_width=1).add()
#
def music(mus):
	inline_kb_mus = InlineKeyboardMarkup(row_width=1).add()
	mu = parser_test.pr(mus)
	i = 0
	for track in mu:
		inline_btn_tr = InlineKeyboardButton("Cкачать: "+track, callback_data='serch'+str(i))
		inline_kb_mus.add(inline_btn_tr)
		i += 1
	return inline_kb_mus
#Playlist
def mym(user_id):
	inline_kb_track = InlineKeyboardMarkup(row_width=1).add()
	mymu = mymus.pr(user_id)
	i = 0
	for track in mymu:
		inline_kb_del = InlineKeyboardButton("Удалить", callback_data = 'del'+str(i))
		inline_btn_trc = InlineKeyboardButton(track +"- Слушать", callback_data='mus'+str(i))
		inline_kb_track.add(inline_btn_trc,inline_kb_del)
		i += 1
	return inline_kb_track
#История музыки 
def mytrack(user_id):
	inline_kb_mymus = InlineKeyboardMarkup(row_width=1).add()
	track = user_mus.pr(user_id)
	i = 0
	inline_kb_sb_fl = InlineKeyboardButton("Очистить историю", callback_data = "delet")
	inline_kb_mymus.add(inline_kb_sb_fl)
	for mus in track:
		inline_btn_mytrc = InlineKeyboardButton(mus +"- Слушать", callback_data='track'+str(i))
		inline_kb_mymus.add(inline_btn_mytrc)
		i += 1
	return inline_kb_mymus
	#Кнопка добавить в плейлист
inline_kb_add = InlineKeyboardButton("Добавить в плейлист", callback_data = "add")
#Музыка vk
inline_btn_vk_1 = InlineKeyboardButton("1️⃣ - "+vk_mus[0], callback_data='vk1')
inline_btn_vk_2 = InlineKeyboardButton("2️⃣ - "+vk_mus[1], callback_data='vk2')
inline_btn_vk_3 = InlineKeyboardButton("3️⃣ - "+vk_mus[2], callback_data='vk3')
inline_btn_vk_4 = InlineKeyboardButton("4️⃣ - "+vk_mus[3], callback_data='vk4')
inline_btn_vk_5 = InlineKeyboardButton("5️⃣ - "+vk_mus[4], callback_data='vk5')
#Музыка Itunes
inline_btn_itunes_1 = InlineKeyboardButton("1️⃣ - "+itunes_mus[0], callback_data='it1')
inline_btn_itunes_2 = InlineKeyboardButton("2️⃣ - "+itunes_mus[1], callback_data='it2')
inline_btn_itunes_3 = InlineKeyboardButton("3️⃣ - "+itunes_mus[2], callback_data='it3')
inline_btn_itunes_4 = InlineKeyboardButton("4️⃣ - "+itunes_mus[3], callback_data='it4')
inline_btn_itunes_5 = InlineKeyboardButton("5️⃣ - "+itunes_mus[4], callback_data='it5')
#Музыка свой 
inline_btn_1 = InlineKeyboardButton("1️⃣ - "+mus[0], callback_data='btn1')
inline_btn_2 = InlineKeyboardButton("2️⃣ - "+mus[1], callback_data='btn2')
inline_btn_3 = InlineKeyboardButton("3️⃣ - "+mus[2], callback_data='btn3')
inline_btn_4 = InlineKeyboardButton("4️⃣ - "+mus[3], callback_data='btn4')
inline_btn_5 = InlineKeyboardButton("5️⃣ - "+mus[4], callback_data='btn5')
#Подтвердждение и отказ
inline_btn_fl = InlineKeyboardButton('❌', callback_data='fal')
inline_btn_tr = InlineKeyboardButton('✔️', callback_data='tr')
#Плейлисты
inline_btn_playlist = InlineKeyboardButton("Плейлист",callback_data="playlist")
inline_btn_top = InlineKeyboardButton("Топ 5 треков недели",callback_data="top")
inline_btn_mymus = InlineKeyboardButton("История скачивания",callback_data="mymus")
inline_btn_offer = InlineKeyboardButton("Наши предложения",callback_data="offer")
#Плейлисты в плейлистах
inline_btn_top_own = InlineKeyboardButton("По версии MusBota",callback_data="top_own")
inline_btn_top_itunes = InlineKeyboardButton("По версии Itunes",callback_data="top_itunes")
inline_btn_top_vk = InlineKeyboardButton("По версии VK",callback_data="top_vk")
#Группы
inline_kb_top_add.add(inline_kb_add)
inline_kb_vk_mus.add(inline_btn_vk_1,inline_btn_vk_2,inline_btn_vk_3,inline_btn_vk_4,inline_btn_vk_5)
inline_kb_itunes_mus.add(inline_btn_itunes_1,inline_btn_itunes_2,inline_btn_itunes_3,inline_btn_itunes_4,inline_btn_itunes_5)
inline_kb_full.add(inline_btn_1, inline_btn_2, inline_btn_3, inline_btn_4,inline_btn_5)
inline_kb_sub.add(inline_btn_tr,inline_btn_fl)
inline_kb_pl.add(inline_btn_top,inline_btn_mymus,inline_btn_offer,inline_btn_playlist)
inline_kb_top.add(inline_btn_top_own,inline_btn_top_itunes,inline_btn_top_vk)
