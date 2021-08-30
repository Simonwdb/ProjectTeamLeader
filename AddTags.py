import time
import pandas as pd
from selenium.common.exceptions import TimeoutException
from TeamleaderWeb import TeamLeaderWeb
from ReadData import ReadData
from GeneralSettings import GeneralSettings as Settings

names = [' B.V.', ' BV', ' N.V.', ' NV', ' bv']


def strip_name(string: str) -> str:
    for n in names:
        if n in string:
            string = string[:string.index(n)]
            # print('func: strip_name: String is now: ', string)
            return string


def get_completed_companies() -> list[str]:
    try:
        with open('Voltooid.txt', 'r+') as file:
            data = file.read().splitlines()
            return data
    except FileNotFoundError:
        print('func: get_completed_companies: Voltooid.txt bestaat nog niet')


def write_completed_log(raw_company_name: str) -> None:
    with open('Voltooid.txt', 'a+') as file:
        file.writelines(raw_company_name+'\n')


def write_error_log(label: str, raw_company_name: str, debtor_number: str) -> None:
    with open('Handmatige tags.txt', 'a+') as file:
        file.writelines(f'label: {label} - company: {raw_company_name} - debtor: {debtor_number}\n')


class AddTags:
    driver: TeamLeaderWeb
    df: pd.DataFrame
    readData: ReadData
    wait_time: float

    def __init__(self) -> None:
        self.wait_time = 1.2
        self.driver = TeamLeaderWeb()
        self.readData = ReadData()
        self.df = self.readData.df

    def sleep(self) -> None:
        time.sleep(self.wait_time)

    def find_company(self, label: str, company: str, debtor_number: str, raw_company_name: str) -> None:
        self.driver.click_on_company_tab()
        self.sleep()
        self.driver.clear_search_bar()
        self.sleep()
        self.driver.search_company(message=company)
        self.sleep()
        self.edit_tags(label=label, debtor_number=debtor_number, raw_company_name=raw_company_name)

    def edit_tags(self, label: str, debtor_number: str, raw_company_name: str) -> None:
        if self.driver.is_total_amount_one():
            # there is a match with the search company
            # now perform adding tags to the company
            self.go_to_edit_company()
            self.sleep()
            # clicking on the tag to add label and product to add label
            self.add_single_tag(label=label)
            self.sleep()
            # clicking on the status to add 'Klant'
            self.driver.click_single_tag(xpath=Settings.XPATH_STATUS_KLANT)
            self.sleep()
            # add debtor number
            self.driver.send_keys_by_xpath(xpath=Settings.XPATH_DEBTOR_NUMBER, message=debtor_number)
            self.sleep()
            self.driver.save_edit_company()
            self.sleep()
            write_completed_log(raw_company_name=raw_company_name)
        else:
            print('func: edit_tags: More than 1 company found')
            write_error_log(label=label, raw_company_name=raw_company_name, debtor_number=debtor_number)
            self.driver.clear_search_bar()

    def go_to_edit_company(self) -> None:
        self.driver.click_on_company()
        self.sleep()
        self.driver.edit_company()
        self.sleep()

    def add_single_tag(self, label: str) -> None:
        tag = None
        product = None
        if label == Settings.COLUMNS_TO_READ[0]:
            tag = Settings.XPATH_TAG_SHARPMINDS
            product = Settings.XPATH_PRODCUT_SHARPMINDS
        elif label == Settings.COLUMNS_TO_READ[1]:
            tag = Settings.XPATH_TAG_HELLOFLEX
            product = Settings.XPATH_PRODCUT_HELLOFLEX
        elif label == Settings.COLUMNS_TO_READ[2]:
            tag = Settings.XPATH_TAG_CAOWIJZER
            product = Settings.XPATH_PRODCUT_CAOWIJZER
        elif label == Settings.COLUMNS_TO_READ[3]:
            tag = Settings.XPATH_TAG_MATCHQ
            product = Settings.XPATH_PRODCUT_MATCHQ
        self.driver.click_single_tag(xpath=tag)
        self.sleep()
        self.driver.click_single_tag(xpath=product)
        self.sleep()

    def get_company_list(self, label: str) -> list[str]:
        return self.df[label].dropna().to_list()

    def add_tags(self, df: pd.DataFrame):
        completed_list = get_completed_companies()
        label = df.columns.to_list()[1]
        for index, row in df.iterrows():
            if row[1] not in completed_list:
                try:
                    company = strip_name(row[1])
                    if company is None:
                        # print('func: add_tags: company is None -> company = ', row[1])
                        company = row[1]
                    print('-- func: add_tags: company: ', company, ' -- label: ', label, '--')
                    self.find_company(label=label, company=company, debtor_number=row[0], raw_company_name=row[1])
                except TimeoutException:
                    print("func: add_tags: TimeOutException appeared")
                    write_error_log(label=label, raw_company_name=row[1], debtor_number=row[0])

    def run_program(self):
        self.driver.login_in()
        df_list = self.readData.get_df_list()
        for df in df_list:
            self.add_tags(df)


if __name__ == '__main__':
    app = AddTags()
    app.run_program()
