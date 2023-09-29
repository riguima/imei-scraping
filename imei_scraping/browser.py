from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


class Browser:
    def __init__(self, headless: bool = True) -> None:
        options = Options()
        if headless:
            options.add_argument('--headless')
        self.driver = Firefox(
            service=Service(GeckoDriverManager().install()),
            options=options,
        )

    def get_imei(self, code: str) -> str:
        self.driver.get('https://mifirm.net/imei')
        code_input = self.driver.find_element(By.CSS_SELECTOR, '#imeiInput')
        code_input.send_keys(code)
        code_input.submit()
        alert = self.driver.find_element(By.CSS_SELECTOR, '.alert')
        breakpoint()
        return ''
