import sqlite3

import parset_test1
import Itpar

def sq():
	db = sqlite3.connect('mus.db')
	cursor = db.cursor()

	a = []

	b = parset_test1.pr(parset_test1.parser())

	for iq in cursor.execute("SELECT mus FROM music"):
		mus = ' '.join(str(x) for x in iq)
		a.append(mus)
	if a == b:
		return a 
	elif a != b:
		musi = b
		cursor.execute("DELETE FROM music")
		i = 0
		while i < len(musi):
			cursor.execute(f"INSERT INTO music VALUES (?)",(musi[i],))
			db.commit() 
			i +=1 
		for iq in cursor.execute("SELECT mus FROM music"):
			b = ' '.join(str(x) for x in iq)
			a.append(b)
		return a

def itunes():
	db = sqlite3.connect('itunes_mus.db')
	cursor = db.cursor()

	a = []

	b = Itpar.itunes_mus()

	for iq in cursor.execute("SELECT mus FROM music"):
		mus = ' '.join(str(x) for x in iq)
		a.append(mus)
	if a == b:
		return a 
	elif a != b:
		musi = b
		cursor.execute("DELETE FROM music")
		i = 0
		while i < len(musi):
			cursor.execute(f"INSERT INTO music VALUES (?)",(musi[i],))
			db.commit() 
			i +=1 
		for iq in cursor.execute("SELECT mus FROM music"):
			b = ' '.join(str(x) for x in iq)
			a.append(b)
		return a
	else:
		musi = b
		while i < len(musi):
			cursor.execute(f"INSERT INTO music VALUES (?)",(musi[i],))
			db.commit() 
			i +=1 
		for iq in cursor.execute("SELECT mus FROM music"):
			b = ' '.join(str(x) for x in iq)
			a.append(b)
		return a
def vk():
	db = sqlite3.connect('vk_mus.db')
	cursor = db.cursor()

	a = []

	b = Itpar.vk_mus()

	for iq in cursor.execute("SELECT mus FROM music"):
		mus = ' '.join(str(x) for x in iq)
		a.append(mus)
	if a == b:
		return a 
	elif a != b:
		musi = b
		cursor.execute("DELETE FROM music")
		i = 0
		while i < len(musi):
			cursor.execute(f"INSERT INTO music VALUES (?)",(musi[i],))
			db.commit() 
			i +=1 
		for iq in cursor.execute("SELECT mus FROM music"):
			b = ' '.join(str(x) for x in iq)
			a.append(b)
		return a
	else:
		musi = b
		while i < len(musi):
			cursor.execute(f"INSERT INTO music VALUES (?)",(musi[i],))
			db.commit() 
			i +=1 
		for iq in cursor.execute("SELECT mus FROM music"):
			b = ' '.join(str(x) for x in iq)
			a.append(b)
		return a
	