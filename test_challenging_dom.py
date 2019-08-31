import pytest
from selenium import webdriver

# Settings function
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(scope="session")
def settings():
    return dict(chrome_path=r'C:\Doc\Admin\Misc\Python\Software\chromedriver_win32\CD_76\chromedriver.exe',
                web_url="http://the-internet.herokuapp.com/challenging_dom")


@pytest.fixture(scope="session")
def web_session(settings: dict) -> webdriver:
    """
    :rtype: webdriver
    :param settings:
    """
    driver: webdriver = webdriver.Chrome(settings["chrome_path"])
    yield driver
    driver.close()


def test_load_page(web_session: object, settings) -> object:
    """
    This test is the first test and is to test that the target web page can be opened.
    This then checks the title matches the expected page title "The Internet"
    :param settings:
    :param web_session:
    """
    print("Getting URL", settings["web_url"])
    web_session.get(settings["web_url"])
    assert "The Internet" in web_session.title


def test_check_page_header(web_session, settings):
    """
    This test checks that the page header matches the expected name "Challenging DOM"
    :rtype: object
    """
    print("Checking Page Header", settings["web_url"])  # TODO Fix this line after
    assert web_session.find_element_by_xpath('//div[@class="example"]/h3').text == "Challenging DOM"


def test_check_button(web_session):
    """
    # TODO Add test description
    :rtype: object
    """
    el = web_session.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button"]')
    button_id = el.get_attribute("id")
    el.click()
    el = web_session.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button"]')
    assert el.get_attribute("id") != button_id


def test_check_button_alert(web_session):
    """
    # TODO Add test description
    :rtype: object
    """
    el = web_session.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button alert"]')
    button_id = el.get_attribute("id")
    el.click()
    el = web_session.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button alert"]')
    assert el.get_attribute("id") != button_id


def test_check_button_success(web_session):
    """
    # TODO Add test description
    :rtype: object
    """
    el = web_session.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button success"]')
    button_id = el.get_attribute("id")
    el.click()
    el = web_session.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button success"]')
    assert el.get_attribute("id") != button_id


def test_check_table_header_one(web_session):
    """
    # TODO Add test description
    :rtype: object
    """
    el = web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[1]')
    th_text = el.text
    assert th_text == "Lorem"
    button = web_session.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button"]')
    button.click()
    print(th_text)
    assert web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[1]').text == th_text


def test_check_table_header_two(web_session):
    """
    # TODO Add test description
    :rtype: object
    """
    el = web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[2]')
    th_text = el.text
    assert th_text == "Ipsum"
    button = web_session.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button"]')
    button.click()
    print(th_text)
    assert web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[2]').text == th_text


def test_check_table_header_three(web_session):
    """
    # TODO Add test description
    :rtype: object
    """
    el = web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[3]')
    th_text = el.text
    assert th_text == "Dolor"
    button = web_session.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button"]')
    button.click()
    print(th_text)
    assert web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[3]').text == th_text


def test_check_table_header_four(web_session):
    """
    # TODO Add test description
    :rtype: object
    """
    el = web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[4]')
    th_text = el.text
    assert th_text == "Sit"
    button = web_session.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button"]')
    button.click()
    print(th_text)
    assert web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[4]').text == th_text


def test_check_table_header_five(web_session):
    """
    # TODO Add test description
    :rtype: object
    """
    el = web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[5]')
    th_text = el.text
    assert th_text == "Amet"
    button = web_session.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button"]')
    button.click()
    print(th_text)
    assert web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[5]').text == th_text


def test_check_table_header_six(web_session):
    """
    # TODO Add test description
    :rtype: object
    """
    el = web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[6]')
    th_text = el.text
    assert th_text == "Diceret"
    button = web_session.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button"]')
    button.click()
    print(th_text)
    assert web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[6]').text == th_text


def test_check_table_header_seven(web_session):
    """
    # TODO Add test description
    :rtype: object
    """
    el = web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[7]')
    th_text = el.text
    assert th_text == "Action"
    button = web_session.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button"]')
    button.click()
    print(th_text)
    assert web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[7]').text == th_text
