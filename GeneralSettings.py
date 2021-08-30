class GeneralSettings:
    CHROME_DRIVER_PATH: str = "C:\\Users\\sdboer\\Desktop\\Projecten\\chromedriver.exe"
    TEAMLEADER_URL: str = "https://app.teamleader.eu/?gotologin"
    TEAMLEADER_LOGIN: str = "dmetz@sharpminds.nl"
    TEAMLEADER_PASSWORD: str = "Goud2vis!"
    COLUMNS_TO_READ: list[str] = ['SharpMinds', 'HelloFlex', 'CAOWijzer', 'MatchQ']
    PATH_FILE_EXCEL: str = 'Klantenbestand2.xlsx'

    XPATH_TAG_SHARPMINDS = '//*[@id="multicat_picker_tags"]/option[26]'
    XPATH_TAG_PEOPLE = '//*[@id="multicat_picker_tags"]/option[12]'  # HelloFlex People
    XPATH_TAG_HELLOFLEX = '//*[@id="multicat_picker_tags"]/option[28]'  # Software Klant
    XPATH_TAG_CAOWIJZER = '//*[@id="multicat_picker_tags"]/option[4]'
    XPATH_TAG_MATCHQ = '//*[@id="multicat_picker_tags"]/option[14]'
    XPATH_TAG_KLANT = '//*[@id="multicat_picker_tags"]/option[13]'

    XPATH_STATUS_KLANT = '//*[@id="multicat_picker_custom_field_229518"]/option[5]'

    XPATH_DEBTOR_NUMBER = '//*[@id="custom_field_409722"]'

    XPATH_PRODCUT_SHARPMINDS = '//*[@id="multicat_picker_custom_field_229497"]/option[9]'
    XPATH_PRODCUT_PEOPLE = '//*[@id="multicat_picker_custom_field_229497"]/option[2]'
    XPATH_PRODCUT_HELLOFLEX = '//*[@id="multicat_picker_custom_field_229497"]/option[3]'
    XPATH_PRODCUT_CAOWIJZER = '//*[@id="multicat_picker_custom_field_229497"]/option[4]'
    XPATH_PRODCUT_MATCHQ = '//*[@id="multicat_picker_custom_field_229497"]/option[10]'
