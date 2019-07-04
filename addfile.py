from selenium import webdriver
import os

link = "http://suninjuly.github.io/file_input.html"
b = webdriver.Chrome()
b.get(link)

b.find_element_by_css_selector("[name='firstname']").send_keys("name")
b.find_element_by_css_selector("[name='lastname']").send_keys("family")
b.find_element_by_css_selector("[name='email']").send_keys("namefamily@yandex.ru")

dir1 = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(dir1, 'file.txt')
b.find_element_by_css_selector("#file").send_keys(file_path)
b.find_element_by_css_selector(".btn").click()

