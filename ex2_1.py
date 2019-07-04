from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)
print(x)
print(y)
input1 = browser.find_element_by_css_selector("#answer").send_keys(y)


checkbox = browser.find_element_by_css_selector(".form-check-label[for='robotCheckbox']").click()
radio = browser.find_element_by_css_selector(".form-check-label[for='robotsRule']").click()
button = browser.find_element_by_css_selector("button.btn").click()

