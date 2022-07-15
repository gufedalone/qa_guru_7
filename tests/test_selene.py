from selene import by, be
from selene.support.shared import browser


def test_github():

    browser.open('https://github.com')
    browser.config.driver.set_window_size(width=1920, height=1080)

    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys('eroshenkoam/allure-example')
    browser.element('.header-search-input').submit()

    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element('#issues-tab').click()
    
    browser.element(by.partial_text('#76')).should(be.visible)
