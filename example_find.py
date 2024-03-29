from selenium import webdriver
import time

#link = "http://suninjuly.github.io/registration1.html"
link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

#name = browser.find_element_by_css_selector(".first_block .first")
name = browser.find_element_by_xpath("//input[@class='form-control first']")
name.send_keys("name")

#for example css_selector
#("div.first_block input.form-control.first")
#("div.first_block input.form-control.second")
#("div.first_block input.form-control.third")
#family = browser.find_element_by_css_selector(".first_block .second")
family = browser.find_element_by_xpath("//input[@placeholder='Введите фамилию']")
family.send_keys("family")


#mail = browser.find_element_by_css_selector(".first_block .third")
mail = browser.find_element_by_xpath("//input[@placeholder='Введите Email']")
mail.send_keys("mail")




# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
