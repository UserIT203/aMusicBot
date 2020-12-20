import sqlite3
import datetime
def m(name,mus):
	db = sqlite3.connect('member.db')
	cursor = db.cursor()
	print(name)
	cursor.execute("CREATE TABLE IF NOT EXISTS %s (musi TEXT,datet DATETIME)" % (name))

	db.commit()

	now = datetime.datetime.now()
	d = now.strftime("%H:%M %d-%m-%Y")

	cursor.execute(f"INSERT INTO %s (`musi`,`datet`) VALUES('{mus}','{d}')"%(name))

	db.commit()

def pr(user_id):
	a = []
	db = sqlite3.connect('member.db')
	cursor = db.cursor()
	for iq in cursor.execute("SELECT * FROM %s "% (user_id)):
		b = '|'.join(str(x) for x in iq)
		a.append(b)
	return a 
	
def dele(user_id):
	db = sqlite3.connect('member.db')
	cursor = db.cursor()
	cursor.execute("DELETE FROM %s " % (user_id))
	db.commit()