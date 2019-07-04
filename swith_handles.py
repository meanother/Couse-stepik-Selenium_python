from selenium import webdriver
import math

link = "http://suninjuly.github.io/redirect_accept.html"
try:
    b = webdriver.Chrome()
    b.get(link)

    b.find_element_by_css_selector(".trollface").click()
    new_window = b.window_handles[1]
    b.switch_to.window(new_window)
    
    x = b.find_element_by_css_selector("#input_value").text
    ex = str(math.log(abs(12*math.sin(int(x)))))
    b.find_element_by_css_selector(".form-control").send_keys(ex)
    b.find_element_by_css_selector(".btn").click()
except Exception as e:
    print(e)

