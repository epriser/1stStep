from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

chrome_options = webdriver.ChromeOptions()
#chrome_options.binary_location = ''
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


driver.get(url='https://datalab.naver.com/shoppingInsight/sCategory.naver')

driver.find_element(By.XPATH, '//*[@id="18_device_0"]').click()
driver.find_element(By.XPATH, '//*[@id="19_gender_0"]').click()
driver.find_element(By.XPATH, '//*[@id="20_age_0"]').click()

time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[1]/div/a').click()

# from openpyxl import Workbook
# wb = Workbook()
# ws = wb.create_sheet('오토코더')
# wb.remove_sheet(wb['Sheet'])
# ws.append((['순위', '인기검색어']))


resultList = []

for i in range(0, 1):
    for j in range(1, 21):
        path = f'//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[1]/ul/li[{j}]/a'
        result = driver.find_element(By.XPATH, path).text
        # key, value = result.split('\n')
        # print(f'key:{key}, value:{value}')
        time.sleep(0.1)
        # ws.append(result.split('\n'))
        # resultList.(key, value)
        # resultDic[key] = value
        resultList.append(result.split("\n"))

    # print(resultDic)
    print(resultList)
    driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/a[2]').click()
    time.sleep(1)

input()
# wb.save('C:/11.xlsx')



