# This is a sample Python script.

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class UnitetsExample(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_find(self):
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title)

        element = driver.find_element_by_name('q')
        element.send_keys("selenium")
        element.send_keys(Keys.RETURN)
        time.sleep(5)
        assert "No se encontró el elemento:" not in driver.page_source

    def tearDown(self):
        self.driver.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main()
