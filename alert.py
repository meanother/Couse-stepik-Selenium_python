# js script alert('Hello!');

#Для этого нужно сначала переключиться на окно с alert, а затем принять его с помощью команды accept():
alert = browser.switch_to.alert
alert.accept()

#Чтобы получить текст из alert, используйте свойство text объекта alert:
alert = browser.switch_to.alert
alert_text = alert.text

#Для переключения на окно confirm используется та же команда, что и в случае с alert:
confirm = browser.switch_to.alert
confirm.accept()

#Для confirm-окон можно использовать следующий метод для отказа:
confirm.dismiss()

#Третий вариант модального окна — prompt — имеет дополнительное поле для ввода текста. Чтобы ввести текст, используйте метод send_keys():
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()

#Переход на новую вкладку браузера
browser.switch_to.window(window_name)
#Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок. Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:
new_window = browser.window_handles[1]

#Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:
first_window = browser.window_handles[0]
#Текущую вкладку можно узнать так:
current_window = browser.current_window_handle


# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)
