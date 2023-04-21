from selenium import webdriver

url = "https://www.google.com/search?q=fiverr&rlz=1C1GCEA_enCA1052CA1052&oq=fiverr&aqs=chrome.0.0i355i433i512j46i199i433i465i512j69i59j0i512l7.1036j1j15&sourceid=chrome&ie=UTF-8"
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)

driver.get(url)
print(driver.title)
