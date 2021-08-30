from GeneralSettings import GeneralSettings
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TeamLeaderWeb:
    driver: webdriver.Chrome

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(GeneralSettings.CHROME_DRIVER_PATH)

    def get_web_element_by_xpath(self, xpath: str) -> webdriver:
        return WebDriverWait(self.driver, 2.5).until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def send_keys_by_xpath(self, xpath: str, message: str) -> None:
        self.get_web_element_by_xpath(xpath).send_keys(message)

    def click_object_by_xpath(self, xpath: str) -> None:
        self.get_web_element_by_xpath(xpath).click()

    def login_in(self) -> None:
        self.driver.get(GeneralSettings.TEAMLEADER_URL)
        login_xpath = '//*[@id="username"]'
        self.send_keys_by_xpath(login_xpath, GeneralSettings.TEAMLEADER_LOGIN)
        password_xpath = '//*[@id="password"]'
        self.send_keys_by_xpath(password_xpath, GeneralSettings.TEAMLEADER_PASSWORD)
        login_button_xpath = '//*[@id="loginButton"]'
        self.click_object_by_xpath(login_button_xpath)

    def click_on_company_tab(self) -> None:
        company_tab_xpath = '//*[@id="app-primary-navigation"]/div/div/a[2]'
        self.click_object_by_xpath(company_tab_xpath)

    def search_company(self, message: str):
        search_xpath = '//*[@id="rightcontent"]/div/div[3]/div[2]/div/div[1]/div/div/div/input'
        self.send_keys_by_xpath(search_xpath, message + Keys.ENTER)

    def clear_search_bar(self) -> None:
        clear_xpath = '//*[@id="rightcontent"]/div/div[3]/div[2]/div[1]/div[1]/div/div/div/div[2]'
        # only click on the clear_search_button when it's visible, if not pass the function
        try:
            self.click_object_by_xpath(clear_xpath)
        except TimeoutException:
            # print('func: clear_search_bar: cross is not visible')
            pass

    def is_total_amount_one(self) -> bool:
        amount_xpath = '//*[@id="rightcontent"]/div/div[3]/div[4]/div[1]/div/span'
        amount = self.get_web_element_by_xpath(amount_xpath)
        return int(amount.text[-1]) == 1

    def click_on_company(self) -> None:
        company_xpath = '//*[@id="crm_companies"]/div/a'
        self.click_object_by_xpath(company_xpath)

    def edit_company(self) -> None:
        edit_xpath = '//*[@id="company-info"]/div[1]/div/button'
        self.click_object_by_xpath(edit_xpath)

    def click_single_tag(self, xpath: str) -> None:
        self.click_object_by_xpath(xpath)

    def save_edit_company(self) -> None:
        save_xpath = '//*[@id="thebutton"]'
        self.click_object_by_xpath(save_xpath)







