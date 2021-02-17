from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import design  # Это наш конвертированный файл дизайна
import re


def do_things(login, passwd):
    dr = webdriver.Chrome()
    have_cookie = False 
    maximized = False
    count = 0 
    hrefs = []
    refreshed = False 
    Moscow = False
    dr.get("https://hh.ru/account/login?backurl=%2F")
    time.sleep(1)
    login_form = dr.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/form/div[1]/input")
    password_form = dr.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/form/div[2]/span/input")
    # time.sleep(100)
    for key in re.findall(r'.', login):
        time.sleep(0.3)
        login_form.send_keys(key)
    for key in re.findall(r'.', passwd):
        time.sleep(0.3)
        password_form.send_keys(key)
    time.sleep(3)
    dr.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/form/div[4]/button").click()
    time.sleep(3)
    while True:
    #https://hh.ru/search/vacancy?L_is_autosearch=false&clusters=true&enable_snippets=true&resume=3b5da9c4ff07fc756d0039ed1f526e3769367a&page= // Для того чтобы искать доступные вакансии
    # https://hh.ru/search/vacancy?L_is_autosearch=false&clusters=true&enable_snippets=true&text=python&page=
        dr.get("https://hh.ru/search/vacancy?L_is_autosearch=false&clusters=true&enable_snippets=true&text=python&page=%d" % count)
        count += 1 
        if not maximized:
            dr.maximize_window() 
            maximized = True
        bs = BeautifulSoup(dr.page_source,"lxml")
        if not refreshed:
            dr.refresh()
        time.sleep(3)
        appended = 0
        for elem in  dr.find_elements_by_link_text('Откликнуться'):
            appended +=1 
            hrefs.append(elem.get_attribute("href"))
        if appended == 0:
            break
    
    badhrefs = []
    for orderhref in hrefs:
        try:
            dr.get(orderhref)
            dr.execute_script('document.getElementsByClassName("bloko-button                            bloko-button_primary                            HH-VacancyResponsePopup-Submit                            HH-SubmitDisabler-Submit                            HH-SimpleValidation-Submit")[0].click()')
        except:
            badhrefs.append(orderhref)
            pass
    
class ExampleApp(QtWidgets.QMainWindow, design.Ui_HH_project_Maxim):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.initialize_text)
       
    def initialize_text(self):
        login_ = self.textEdit.toPlainText()
        passwd_ = self.textEdit_2.toPlainText()
        self.close()
        do_things(login_, passwd_)
        
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()