from selenium import webdriver


def parser():
	i = 0
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	browser = webdriver.Chrome(options=options)
	url = ["https://ruq.hotmo.org/songs/top-today","https://ruq.hotmo.org/chart/idc/1","https://ruq.hotmo.org/chart/idc/2","https://ruq.hotmo.org/chart/idc/3"
	,"https://ruq.hotmo.org/chart/idc/4"]
	music = []
	while i < 5:
		browser.get(url[i])
		btn_element = browser.find_element_by_class_name("track__title").text
		btn_element1 = browser.find_element_by_class_name("track__desc").text
		mus = str(btn_element1)+" - "+str(btn_element)
		if mus in music:
			None
			i +=1 
		else:
			music.append(mus)
			i += 1
	return music
def pr(music):
	if len(music) < 5:
		options = webdriver.ChromeOptions()
		options.add_argument('headless')
		browser = webdriver.Chrome(options=options)
		url = "https://ruq.hotmo.org/chart/idc/5"
		browser.get(url)
		btn_element = browser.find_element_by_class_name("track__title").text
		btn_element1 = browser.find_element_by_class_name("track__desc").text
		music.append(btn_element1+" - "+btn_element)
		music1 = music
		return music1
	elif len(music) == 5:
		music1 = music
		return music1
