# -*- coding: utf-8 -*-#
from django.conf import settings
from django.test import LiveServerTestCase
from selenium import webdriver


class HostTest(LiveServerTestCase):
    def test_homepage(self):
        driver = webdriver.Chrome(executable_path=settings.BASE_DIR / "chromedriver")

        driver.get("http://127.0.0.1:8000/")
