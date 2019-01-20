import spreadsheet
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import datetime

table = spreadsheet.get_sheet("EksisozlukKullanicilar").get_all_records()
table_caylaksira = spreadsheet.get_sheet("EksisozlukCaylakSira")
print(table_caylaksira)

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')  # Optional argument, if not specified will search path.
for row in table:
	if row["NumberOfEntry"] >= 10:
		print(row["email"])
		print(row["EksiPass"])
		driver.get('https://eksisozluk.com/giris')
		time.sleep(5) # Let the user actually see something!
		username = driver.find_element_by_name('UserName')
		password = driver.find_element_by_name('Password')
		username.send_keys(row["email"])
		password.send_keys(row["EksiPass"])
		username.submit()
		time.sleep(35) # Let the user actually see something!
		profile_url = driver.find_element_by_xpath("//*[@id='top-navigation']/ul/li[5]/a")
		driver.get(profile_url.get_attribute("href"))
		element = driver.find_element_by_xpath("//*[@id='content-body']/p")
		text = element.text
		caylak_sira = text[text.index("onay listesinde ")+len("onay listesinde "):text.index(". sıradasınız")]
		print(caylak_sira)
		table_caylaksira.append_row([row["email"], caylak_sira, str(datetime.datetime.now())])
		time.sleep(35) # Let the user actually see something!
		driver.get("https://eksisozluk.com/terk")

driver.quit()
