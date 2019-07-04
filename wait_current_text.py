from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import pyperclip


link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    b = webdriver.Chrome()
    b.get(link)
    #b.implicitly_wait(12)
    #b.find_element_by_css_selector(".btn").click()
    price = WebDriverWait(b, 12).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"),"10000 RUR"))
    b.find_element_by_css_selector(".btn").click() 

    x = b.find_element_by_css_selector("#input_value").text
    ex = str(math.log(abs(12*math.sin(int(x)))))
    b.find_element_by_css_selector(".form-control").send_keys(ex)
    b.find_element_by_css_selector("#solve").click()

except Exception as e:
    print(e)
pyperclip.copy(b.switch_to.alert.text.split(': ')[-1])

