from selenium import webdriver
import time
driver = webdriver.Chrome(r"E:\Web\papa\day10\chromedriver(1).exe")
driver.get("http://sbj.cnipa.gov.cn/")
# time.sleep(1)

driver.find_element_by_xpath("//a[text()='商标公告']").click()
time.sleep(5)
for handle in driver.window_handles:
    print(handle)
    driver.switch_to_window(handle)
driver.find_element_by_id('annNum').send_keys(1)

driver.find_element_by_id('annNumSubmit').click()


# time.sleep(5)
# print(11)
# driver.find_element_by_xpath("//a[text()='商标综合查询']")
