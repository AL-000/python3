from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys


def main():
    #запуск браузера и открытие страницы
    driver = webdriver.Chrome()
    url = "https://r7-office.ru/request_personal"
    driver.get(url)
    time.sleep(1)

    #Ввод Имени
    elements_name = driver.find_elements_by_xpath("//input[@class='t-input js-tilda-rule ']")
    second_name = elements_name[0]
    second_name.click()
    second_name.clear()
    second_name.send_keys('Тест')
    time.sleep(1)

    #Ввод Фамилии
    elements_lastname = driver.find_elements_by_xpath("//input[@class='t-input js-tilda-rule ']")
    second_lastname = elements_lastname[1]
    second_lastname.click()
    second_lastname.clear()
    second_lastname.send_keys('Тестов')
    time.sleep(2)

    # Скрол вниз#
    driver.execute_script("window.scrollTo(0, 500)")

    #Ввод почты
    elements_email = driver.find_elements_by_xpath("//input[@class='t-input js-tilda-rule ']")
    second_email = elements_email[2]
    second_email.click()
    second_email.clear()
    second_email.send_keys('test@mail.ru')
    time.sleep(2)

    #Ввод телефона
    elements_phone = driver.find_elements_by_xpath("//input[@class='t-input t-input-phonemask']")
    second_phone = elements_phone[0]
    second_phone.click()
    second_phone.clear()
    second_phone.send_keys('951-442-43-47')
    time.sleep(2)

    # (JavaScriptExecutor) Нажатие чекбокса
    che_box = driver.find_elements_by_xpath("//input[@class='t-checkbox js-tilda-rule']")
    che_box1 = che_box[0]
    driver.execute_script("arguments[0].click();", che_box1)
    time.sleep(2)

    # (JavaScriptExecutor) Нажатие чекбокса 2
    che_box02 = driver.find_elements_by_xpath("//input[@class='t-checkbox js-tilda-rule']")
    che_box2 = che_box02[1]
    driver.execute_script("arguments[0].click();", che_box2)
    time.sleep(2)

    # Нажатие кнопки отправить
    elem_comm = driver.find_elements_by_xpath("//button[contains(text(), 'Отправить')]")
    send_feed = elem_comm[0]
    send_feed.click()
    time.sleep(2)

    # открытие страницы "Загрузки"
    url = "https://r7-office.ru/downloads#1_2"
    driver.get(url)
    time.sleep(3)

    # Считывание поддерживаемых систем
    text1 = driver.find_element_by_xpath("// a[contains(text(), 'Альт Линукс')]").text
    text2 = driver.find_element_by_xpath("// a[contains(text(), 'РОСА Линукс')]").text
    text3 = driver.find_element_by_xpath("// a[contains(text(), 'Astra Linux')]").text
    text4 = driver.find_element_by_xpath("// a[contains(text(), 'РЕД ОС')]").text

    # Запись поддерживаемых систем в лист
    listOS = [text1, text2, text3, text4]

    print('python3 -m test.py\n', listOS)

    time.sleep(6)

main()
