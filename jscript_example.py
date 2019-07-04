from selenium import webdriver
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)
#browser.execute_script("alert('Robots at work');")
#browser.execute_script("document.title='Script executing';")
#browser.execute_script('document.title="Script executing";')
#browser.execute_script("document.title='Script executing';alert('Robots at work');")
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()


# browser.execute_script("window.scrollBy(0, 100);")

