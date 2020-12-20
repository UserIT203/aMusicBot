from selenium import webdriver
import time

def main(a):
	browser = webdriver.Firefox()
	browser.get("https://ruq.hotmo.org/")
	element = browser.find_element_by_class_name("form-control")
	element.send_keys(a)
	btn_el = browser.find_element_by_class_name("search-btn")
	btn_el.click()
	time.sleep(4)
	btn_element = browser.find_element_by_class_name("track__download-btn")
	btn_element.click()
	a = btn_element.get_attribute("href")
	lst  = list(a)
	del lst[0:41]
	b = ''.join(lst)
	time.sleep(25)
	browser.quit()
	return b
def parser(a):
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	browser = webdriver.Chrome(options=options)
	browser.get("https://ruq.hotmo.org/")
	element = browser.find_element_by_class_name("form-control")
	element.send_keys(a)
	btn_el = browser.find_element_by_class_name("search-btn")
	btn_el.click()
	time.sleep(5)
	btn_element = browser.find_element_by_class_name("track__download-btn")
	a = btn_element.get_attribute("href")
	lst  = list(a)
	del lst[0:41]
	b = ''.join(lst)
	browser.close()
	return b

def pr(a):
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	browser = webdriver.Chrome(options=options)
	url = "https://ruq.hotmo.org/"
	browser.get(url)
	element = browser.find_element_by_class_name("form-control")
	element.send_keys(a)
	btn_el = browser.find_element_by_class_name("search-btn")
	btn_el.click()
	time.sleep(5)

	track = browser.find_elements_by_class_name("track__title")
	name = browser.find_elements_by_class_name("track__desc")

	texts = []
	for el in track:
		if el.text == "":
			None
		elif len(texts) == 3:
			break
		else:
			texts.append(el.text)

	text = []
	for tr in name:
		if tr.text == "":
			None
		elif len(text) == 3:
			break
		else:
			text.append(tr.text)

	i = 0
	mus = []
	while i <3:
		mus.append(text[i]+" - "+texts[i])
		i +=1
	return mus