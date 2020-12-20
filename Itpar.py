from selenium import webdriver
import time
#Itunes
def itunes_mus():
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	browser = webdriver.Chrome(options=options)

	url = "https://music.apple.com/ru/playlist/%D1%82%D0%BE%D0%BF-100-%D1%80%D0%BE%D1%81%D1%81%D0%B8%D0%B8/pl.728bd30a9247487c80a483f4168a9dcd"

	browser.get(url)

	track = browser.find_elements_by_class_name("song-name.typography-label")

	name = browser.find_elements_by_class_name("by-line.typography-caption")

	texts = []
	for el in track:
		if el.text == "":
			None
		elif len(texts) == 5:
			break
		else:
			texts.append(el.text)
	text = []
	for tr in name:
		if tr.text == "":
			None
		elif len(text) == 5:
			break
		else:
			text.append(tr.text)
	i = 0
	mus = []
	while i <5:
		mus.append(text[i]+" - "+texts[i])
		i +=1
	return mus

#Vk
def vk_mus():
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	browser = webdriver.Chrome(options=options)

	url = "https://zvooq.pro/collections/any/%D0%B2%D0%BA-8570"
	browser.get(url)

	art = browser.find_elements_by_class_name("artist")
	tra = browser.find_elements_by_class_name("track")

	artist = []
	for ar in art:
		if ar.text == "":
			None
		elif len(artist) == 5:
			break
		else:
			artist.append(ar.text)

	track = []
	for tr in tra:
		if tr.text == "":
			None
		elif len(track) == 5:
			break
		else:
			track.append(tr.text[:-21])

	i = 0
	mus = []
	while i <5:
		mus.append(artist[i]+" - "+track[i])
		i +=1
	return mus	


