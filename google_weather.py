from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = Options()
options.headless = True

# Don't allow images to load
chrome_prefs = {}
options.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}

capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"

options.add_argument("--ignore-certificate-errors")
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
options.add_argument('start-maximized')
# options.add_argument('--log-level=3')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
# PATH = f"{os.path.normpath(os.getcwd() + os.sep + os.pardir)}/chromedriver.exe"
PATH = r'C:\Users\nishm\Desktop\Desktop\chromedriver_win32\chromedriver_v95.exe'
def precepitation_info(city):
    driver = webdriver.Chrome(options=options, executable_path=PATH, desired_capabilities=capa)
    wait1 = WebDriverWait(driver, 2000)
    driver.get(f'https://www.google.com/search?q={city}+weather')
    wait1.until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="wob_rain"]')))
    # driver.execute_script("window.stop();")
    # print(driver.find_element_by_xpath('//*[@id="wob_rain"]').text)
    # driver.find_element_by_xpath('//*[@id="wob_rain"]').click()
    # wait1.until(EC.visibility_of_element_located(
    #     (By.XPATH, '//*[@id="wob_pg"]/div[1]/div[1]')))
    # driver.execute_script("window.stop();")
    time_data = []
    precipitation_data = []
    # j=0
    try:
        for i in range(1, 20):
            tim_e = driver.find_element_by_xpath(f'//*[@id="wob_pg"]/div['+str(i)+']/div[1]').get_attribute('aria-label')
            time_data.append(str(tim_e).split(' ', 2)[2])
            precipitation_data.append(str(tim_e).split(' ', 2)[0])
            # print(time_data[i-1],"-->", precipitation_data[i-1])
            # print(i, time_data[j])
            # j+=1
        driver.close()
        return time_data, precipitation_data
    except Exception as e:
        print(e)
        driver.close()
        return -1
# time_data, precipitation = precepitation_info('bangalore')
# print(time_data)
# print(precipitation)
