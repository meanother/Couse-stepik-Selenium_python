from selenium import webdriver
import math


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)


pic = browser.find_element_by_css_selector("#treasure")
x = pic.get_attribute("valuex")
print(x)
form = str(math.log(abs(12*math.sin(int(x)))))
answer = browser.find_element_by_css_selector("#answer").send_keys(form)

for i in ['#robotCheckbox', '#robotsRule' ]:
    browser.find_element_by_css_selector(i).click()


browser.find_element_by_css_selector(".btn").click()


#(math.log(abs(12*math.sin(int(x)))))




#human_radio = browser.find_element_by_id("humanRule")
#human_checked = human_radio.get_attribute("checked")
#найдем атрибус у данного радиобаттона
#print("value of human radio: ", human_checked)
#assert human_checked is not None, "Human radio is not selected by default"
#assert human_checked == "true", "Human radio is not selected by default"

#robots_radio = browser.find_element_by_id("robotsRule")
#robots_checked = robots_radio.get_attribute("checked")
#assert robots_checked is None
