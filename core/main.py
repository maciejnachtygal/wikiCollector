#!/Program Files (x86)/Python37-32
import urllib
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from functions import *

os.system("cls")

driver = webdriver.Firefox()


requestFile = openFile("source.txt", 'rb')
request = requestFile.read()
requestFile.close()
buffer = request.decode("utf-8")

requestItems = buffer.split("\n")

for item in range (len(requestItems)):
	os.system("cls")
	progress = item*100/len(requestItems)
	print("Postep wynosi :\t%.2f%%" % progress)
	print("Zagadnienia :\t%i z %i" % (item+1,len(requestItems)))
	print("-----> Opracowuje zagadnienie %s." % requestItems[item])

	driver.get("https://pl.wikipedia.org/w/index.php?search=&title=Specjalna%%3ASzukaj&go=Przejd%%C5%%BA&ns0=1")
	assert "Szukaj – Wikipedia, wolna encyklopedia" in driver.title
	elem = driver.find_element_by_name("search")
	elem.clear()
	elem.send_keys(requestItems[item])
	time.sleep(1)
	elem.send_keys(Keys.RETURN)
	time.sleep(2)

	try:
		suggestion = driver.find_elements_by_css_selector(
			"#mw-content-text > div.searchresults > ul.mw-search-results > li:nth-child(1) > div.mw-search-result-heading > a")[0]
		time.sleep(1)
		suggestion.click()
	except:
		print("XXXXXX Nie znaleziono zagadnienia.")
		file = openFile("aaaa-nie-znaleziono.txt", "a+")
		file.write(requestItems[item])
		file.close()
		continue

	try:
		elem = driver.find_element_by_id("Vorlage_Alternative")
		print("!!!!!! Zbyt wiele mozliwosci dla %s." % requestItems[item])
		file = openFile("aaaa-nie-znaleziono.txt", "a+")
		file.write(requestItems[item])
		file.close()
	except:

		content = driver.find_element_by_id("content")
		string = content.text
		#ustring = string.decode("utf-8")
		asciistring = string.encode("utf-8")
		#print(asciistring)
		newFile = requestItems[item]
		newFile = newFile.encode()
		newFile = newFile.decode("ascii","ignore")
		newFile = newFile.split("\r")
		if 0 <= item < 10:
			file = createFile("data\\00" + str(item) + "-" + newFile[0] + ".txt", 'wb')
		elif 10 <= item < 100:
			file = createFile("data\\0" + str(item) + "-" + newFile[0] + ".txt", 'wb')
		elif 100 <= item:
			file = createFile("data\\" + str(item) + "-" + newFile[0] + ".txt", 'wb')
		file.write(asciistring)
		file.close()
		try:
			imgPage = driver.find_elements_by_class_name("image")
			#print(imgPage[0])
			imgPage[0].click()
			time.sleep(1)
			print(".......Znaleziono obrazek")
			if 0 <= item < 10:
				driver.save_screenshot("data\\00" + str(item) + "-" + newFile[0] + ".png")
			elif 10 <= item < 100:
				driver.save_screenshot("data\\0" + str(item) + "-" + newFile[0] + ".png")
			elif 100 <= item:
				driver.save_screenshot("data\\" + str(item) + "-" + newFile[0] + ".png")
			print("++++++ Zapisano obrazek")
		except:
			print("------ Nie znaleziono obrazka.")
			file.close()
			continue
#elem = driver.find_element_by_name("body")
assert "No results found." not in driver.page_source

driver.close()