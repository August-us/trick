from selenium import webdriver
import time
def huateng():
    optios=webdriver.chrome.options.Options().add_argument('--allow-outdated-plugins')
    browser = webdriver.Chrome(options=optios)
    browser.maximize_window()
    allow_flash(browser,"https://rc.qzone.qq.com/348?via=QZ.APPMANAGE.APPASSISTANT")
    browser.get('https://rc.qzone.qq.com/348?via=QZ.APPMANAGE.APPASSISTANT')
    browser.find_element_by_id("gotoapp-link").click()
    time.sleep(3)
    browser.switch_to.frame(0)
    #通过使用选择器选择到表单元素进行模拟输入和点击按钮提交
    # browser.find_element_by_id('switcher_plogin').click()
    # browser.find_element_by_id('u').clear()
    # browser.find_element_by_id('u').send_keys(myqq)
    # browser.find_element_by_id('p').clear()
    # browser.find_element_by_id('p').send_keys(mypas)
    # browser.find_element_by_id('login_button').click()
    # 使用TIM关联登录
    time.sleep(3)
    browser.find_element_by_id('nick_1289269253').click()
    input()
    browser.quit()

from urllib.parse import quote_plus as url_quoteplus
from urllib.parse import urlsplit
from selenium.webdriver.common.by import By as WebBy
from selenium.webdriver.support.ui import Select as WebSelect

def allow_flash(driver, url):
    def _base_url(url):
        if url.find("://") == -1:
            url = "http://{}".format(url)
        urls = urlsplit(url)
        return "{}://{}".format(urls.scheme, urls.netloc)

    def _shadow_root(driver, element):
        return driver.execute_script("return arguments[0].shadowRoot", element)

    base_url = _base_url(url)
    driver.get("chrome://settings/content/siteDetails?site={}".format(url_quoteplus(base_url)))

    root1 = driver.find_element(WebBy.TAG_NAME, "settings-ui")
    shadow_root1 = _shadow_root(driver, root1)
    root2 = shadow_root1.find_element(WebBy.ID, "container")
    root3 = root2.find_element(WebBy.ID, "main")
    shadow_root3 = _shadow_root(driver, root3)
    root4 = shadow_root3.find_element(WebBy.CLASS_NAME, "showing-subpage")
    shadow_root4 = _shadow_root(driver, root4)
    root5 = shadow_root4.find_element(WebBy.ID, "advancedPage")
    root6 = root5.find_element(WebBy.TAG_NAME, "settings-privacy-page")
    shadow_root6 = _shadow_root(driver, root6)
    root7 = shadow_root6.find_element(WebBy.ID, "pages")
    root8 = root7.find_element(WebBy.TAG_NAME, "settings-subpage")
    root9 = root8.find_element(WebBy.TAG_NAME, "site-details")
    shadow_root9 = _shadow_root(driver, root9)
    root10 = shadow_root9.find_element(WebBy.ID, "plugins")  # Flash
    shadow_root10 = _shadow_root(driver, root10)
    root11 = shadow_root10.find_element(WebBy.ID, "permission")
    WebSelect(root11).select_by_value("allow")

def  visit():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('https://user.qzone.qq.com/1289269253/main')
    browser.switch_to.frame('login_frame')
    input()
    # 通过使用选择器选择到表单元素进行模拟输入和点击按钮提交
    # browser.find_element_by_id('switcher_plogin').click()
    # browser.find_element_by_id('u').clear()
    # browser.find_element_by_id('u').send_keys(myqq)
    # browser.find_element_by_id('p').clear()
    # browser.find_element_by_id('p').send_keys(mypas)
    # browser.find_element_by_id('login_button').click()
    # 使用TIM关联登录
    browser.switch_to_frame()
    time.sleep(3)
    browser.find_element_by_id('nick_1289269253').click()
if __name__ == '__main__':
    huateng()
    # visit()