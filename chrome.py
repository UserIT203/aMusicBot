from selenium import webdriver
def chrom():
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	browser = webdriver.Chrome(options=options)
	return browser