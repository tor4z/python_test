from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.chrome.options import Options as CHOptions

#assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
ff_options = FFOptions()
ff_options.set_headless(True)

ch_options = CHOptions()
ch_options.set_headless(True)
#chrome = webdriver.Chrome(chrome_options = ch_options)
firefox = webdriver.Firefox(firefox_options=ff_options)
#phantom = webdriver.PhantomJS()
for i in range(100):
	#firefox.get("http://www.acfun.cn/")
	#print(firefox.title)
	#chrome.get("https://cn.bing.com/")
	firefox.get("https://www.baidu.com/")
	print(firefox.title, i)
#chrome.close()
firefox.close()
#phantom.close()