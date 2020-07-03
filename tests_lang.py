import pytest
import yaml
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with open('data.yaml', 'rt', encoding='utf8', )  as yml:
    translate_data = yaml.load(yml, Loader=yaml.Loader)


default_currency = [("ru", "RUB"), ("en", "USD"), ("de", "EUR"), ("fil", "PHP"), ("fr", "EUR"), ("it", "EUR"),
                    ("ja", "JPY"), ("ko", "KRW"), ("pt-br", "BRL"), ("tr", "TRY"), ("vi", "USD"), ("zh", "CNY"), ("zh-tw", "CNY")]


class TestLocalization:
    @pytest.mark.parametrize("language, expect_result, css_selector", translate_data)
    def test_guest_should_see_correct_translation(self, browser, language, expect_result, css_selector):
        link = f"https://coinmarketcap.com/{language}/"
        browser.get(link)
        actual_result = browser.find_element_by_css_selector(css_selector).text
        assert actual_result == expect_result

    @pytest.mark.parametrize("language, expect_result", default_currency)
    def test_guest_should_see_correct_default_currency(self, browser, language, expect_result):
        link = f"https://coinmarketcap.com/{language}/"
        button = 'div[class = "cmc-popover__trigger"]>button.wn9odt-0'
        browser.get(link)
        WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, button),expect_result))
        actual_currency =  browser.find_element_by_css_selector(button).text
        assert actual_currency == expect_result



@pytest.mark.parametrize("language", ["ru", "en", "de", "es", "fil", "fr", "hi", "it", "ja", "ko", "pt-br", "tr", "vi", "zh", "zh-tw"])
class TestFunctional:
    def test_guest_can_change_language_with_button(self, browser, language):
        browser.implicitly_wait(5)
        link = "https://coinmarketcap.com/"
        button = '//div[@class="cmc-popover"]/div[@class="cmc-popover__trigger"]/button[@title]'
        browser.get(link)
        browser.find_element_by_xpath(button).click()
        drop_elem = browser.find_element_by_xpath('//div[@class = "frscwy-3 frscwy-4 iUHqnq"]/a[@href="/'+language+'/"]')
        drop_elem.click()
        actual_result = browser.find_element_by_xpath(button).text
        assert actual_result == language.upper()

    @pytest.mark.parametrize("css_selector, expect_header", [(".jopABT", "Log In"), (".gXirId.cmc-link", "Create an Account")])
    def test_guest_can_move_to_pages(self, browser, language, css_selector, expect_header):
        browser.implicitly_wait(5)
        link = f"https://coinmarketcap.com/{language}/"
        browser.get(link)
        new_window_url = browser.find_element_by_css_selector(css_selector).get_attribute("href")
        browser.get(new_window_url)
        assert browser.find_element_by_css_selector("h1").text == expect_header

    def test_guest_can_subscribe(self, browser, language):
        browser.implicitly_wait(5)
        link = f"https://coinmarketcap.com/{language}/"
        email = str(time.time()) + "@fakemail.com"
        browser.get(link)
        subscribe_field = browser.find_element_by_css_selector('.kczUvt .cmc-newsletter-signup__widget input[name="email"]')
        subscribe_field.send_keys(email)
        button = browser.find_element_by_css_selector('button[id ="_form_3_submit"]')
        button.click()
        assert browser.find_element_by_css_selector(".eggaDS").text == "You're on the list!"


