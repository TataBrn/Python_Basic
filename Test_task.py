"""
Итоговое задание
1. Открыть страницу http://google.com/ncr
2. Выполнить поиск слова “selenide”
3. Проверить, что первый результат – ссылка на сайт selenide.org.
4. Перейти в раздел поиска изображений
5. Проверить, что первое изображение неким образом связано с сайтом selenide.org.
6. Вернуться в раздел поиска Все
7. Проверить, что первый результат такой же, как и на шаге 3.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.chrome.service import Service


class Search(unittest.TestCase):
    """
    Содержит тесты
    """

    def setUp(self):
        """
        Выполняет набор действий до запуска каждого теста
        """
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-notifications')
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("prefs", {'intl.accept_languages': 'en'})
        service = Service('chromedriver.exe')
        self.drv = webdriver.Chrome(service=service, options=options)

    def test_search(self):
        """
        Сам тест
        """

        # 1.Открываем страницу http://google.com/ncr
        self.drv.get('http://google.com/ncr')

        assert 'Google' in self.drv.title

        # 2. Пишем запрос со словом “selenide”
        elm = self.drv.find_element(By.NAME, 'q')
        elm.send_keys('selenide')
        elm.send_keys(Keys.ENTER)

        # 3. Проверяем, что первый  результат – ссылка на сайт selenide.org.
        urls = self.drv.find_elements(By.TAG_NAME, 'cite')
        result_url = urls[0].text
        assert 'selenide.org' in result_url, 'Первая ссылка не selenide.org'

        # 4. Переходим в раздел поиска изображений
        image_search = self.drv.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
        image_search.click()

        # 5. Проверяем, что первое изображение неким образом связано с сайтом selenide.org.
        img_urls = self.drv.find_elements(By.CLASS_NAME, 'dmeZbb')
        assert 'selenide.org' in img_urls[0].text, 'Первая картинка не связана с selenide.org'

        # 6. Возвращаемся в раздел поиска Все
        all_search = self.drv.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]')
        all_search.click()

        # 7. Проверяем, что первый результат такой же, как и на шаге 3.
        urls_new = self.drv.find_elements(By.TAG_NAME, 'cite')
        new_result_url = urls_new[0].text
        assert result_url == new_result_url, 'Первая ссылка не такая же, как на шаге 3'

    def tearDown(self):
        """
        Набор команд по завершению каждого теста
        """
        self.drv.close()
        self.drv.quit()


if __name__ == '__main__':
    unittest.main()
