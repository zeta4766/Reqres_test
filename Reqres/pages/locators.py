from selenium.webdriver.common.by import By


class BaseLocator:
    ENDPOINTS = (By.CSS_SELECTOR, "div.endpoints > ul > li")
    LINKS = (By.XPATH, "//*[@data-key='try-link']")
    RESPONSE_CODE = (By.CLASS_NAME, "response-code")
    OUTPUT_RESPONSE = (By.XPATH, "//*[@data-key='output-response']")
