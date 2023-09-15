import json

from bs4 import BeautifulSoup

import settings
from pages.base_page import BasePage
from utils.dictionary_endpoints import endpoints_info
from pages.locators import BaseLocator


class MainPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = settings.base_settings.base_url
        driver.get(url)
        self.endpoints = driver.find_elements(*BaseLocator.ENDPOINTS)
        self.links = driver.find_elements(*BaseLocator.LINKS)
        self.resp_code = driver.find_element(*BaseLocator.RESPONSE_CODE)
        self.output_response = driver.find_element(*BaseLocator.OUTPUT_RESPONSE)

    def href_by_name(self, endpoint_name):
        number_of_element = endpoints_info(endpoint_name=endpoint_name)
        return self.links[number_of_element].get_attribute('href')

    def endpoint_click(self, endpoint_name):
        number_of_element = endpoints_info(endpoint_name=endpoint_name)
        self.endpoints[number_of_element].click()

    def response_code(self):
        return self.resp_code.text

    def out_response(self):
        return self.output_response.text

    def json_data_for_request_body(self, test_name):
        self.endpoint_click(test_name)
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        html_element = soup.find('pre', {'data-key': 'output-request'}).text
        json_data = json.loads(html_element)
        return json_data
