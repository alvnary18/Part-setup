import ssl
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from timeit import default_timer as timer
ssl._create_default_https_context = ssl._create_unverified_context
import selenium
from bs4 import BeautifulSoup
import pandas as pd
chromedriver = 'C:\Projects HP\Part setup\chromedriver.exe'
driver = selenium.webdriver.Chrome(chromedriver)
driver.maximize_window()
start = timer()
driver.get('https://vistabrokerpro.corp.hp.com/DWS/default.aspx')
driver.implicitly_wait(10)
input_path = "C:/Projects HP/Part setup/"
request_id = pd.read_csv(input_path + "2.csv")
request_id_status1 = request_id
# DFT navigation
for i in request_id['request_id'].values:
    search = Select(driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlSelectApplication'))
    search.select_by_visible_text('Procurement Tracking')
    sleep(2)
    search2 = Select(driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlUserType'))
    search2.select_by_visible_text('Approver')
    sleep(2)
    search3 = Select(driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlUser'))
    search3.select_by_visible_text('All')
    sleep(2)
    search4 = Select(driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlStatus'))
    search4.select_by_visible_text('All')
    sleep(2)
    driver.find_element_by_id('ctl00_ContentPlaceHolder1_fromDate').clear()
    driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_fromDate"]').send_keys('6/1/2019')
    search5 = Select(driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlSearch'))
    search5.select_by_visible_text('RequestID')
    sleep(2)
    driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtSearch"]').send_keys(str(i))
    driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_viewReq"]').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_gvRequest"]/tbody/tr[2]/td[12]').click()
    driver.switch_to.window(driver.window_handles[1])
    page_source = driver.page_source
    driver.implicitly_wait(10)
    soup = BeautifulSoup(page_source, 'lxml')
    # print(soup.findAll)
    # Scaping information from DFT tool
    RequestID = soup.find("span", id='ctl00_ContentPlaceHolder1_LBLHiddenRequestId')
    request_id_status1.loc[i, 'RequestID'] = str(RequestID.text)
    Tangible = soup.find(id='ctl00_ContentPlaceHolder1_gvOrderDetail_ctl02_txtIntangibles').get("value")
    request_id_status1.loc[i, 'Tangible'] = Tangible
    ContactName = soup.find(id='ctl00_ContentPlaceHolder1_txtContactName').get("value")
    request_id_status1.loc[i, 'ContactName'] = ContactName
    ManufacturerName = soup.find(id='ctl00_ContentPlaceHolder1_txtManufacturername').get("value")
    request_id_status1.loc[i, 'ManufacturerName'] = ManufacturerName
    PL = soup.find("select", {"id": "ctl00_ContentPlaceHolder1_ddlProductLine"})
    options = PL.find_all('option', selected=True)
    values1 = [o.get("value") for o in options]
    request_id_status1.loc[i, 'Product Line'] = values1
    Vendor = soup.find("select", {"id": "ctl00_ContentPlaceHolder1_ddlVendo"})
    options = Vendor.find_all('option', selected=True)
    values2 = [o.get("value") for o in options]
    request_id_status1.loc[i, 'Vendor'] = values2
    Weight = soup.find(id='ctl00_ContentPlaceHolder1_txtWeight').get("value")
    request_id_status1.loc[i, 'Weight'] = Weight
    Length = soup.find(id='ctl00_ContentPlaceHolder1_txtDimensions').get("value")
    request_id_status1.loc[i, 'Length'] = Length
    Width = soup.find(id='ctl00_ContentPlaceHolder1_txtWidth').get("value")
    request_id_status1.loc[i, 'Width'] = Width
    Height = soup.find(id='ctl00_ContentPlaceHolder1_txtHeight').get("value")
    request_id_status1.loc[i, 'Height'] = Height
    COO = soup.find(id='ctl00_ContentPlaceHolder1_txtCOO').get("value")
    request_id_status1.loc[i, 'COO'] = COO
    MFgPartNum = soup.find(id='ctl00_ContentPlaceHolder1_gvOrderDetail_ctl02_txtMfgPartNos').get("value")
    MFgPartNum1 = soup.find(id='ctl00_ContentPlaceHolder1_gvOrderDetail_ctl03_txtMfgPartNos').get("value")
    MFgPartNum2 = soup.find(id='ctl00_ContentPlaceHolder1_gvOrderDetail_ctl04_txtMfgPartNos').get("value")
    MFgPartNum3 = soup.find(id='ctl00_ContentPlaceHolder1_gvOrderDetail_ctl05_txtMfgPartNos').get("value")
    MFgPartNum4 = soup.find(id='ctl00_ContentPlaceHolder1_gvOrderDetail_ctl06_txtMfgPartNos').get("value")
    MFgPartNum5 = soup.find(id='ctl00_ContentPlaceHolder1_gvOrderDetail_ctl07_txtMfgPartNos').get("value")
    MFgPartNum6 = soup.find(id='ctl00_ContentPlaceHolder1_gvOrderDetail_ctl08_txtMfgPartNos').get("value")
    MFgPartNum7 = soup.find(id='ctl00_ContentPlaceHolder1_gvOrderDetail_ctl09_txtMfgPartNos').get("value")
    MFgPartNum8 = soup.find(id='ctl00_ContentPlaceHolder1_gvOrderDetail_ctl10_txtMfgPartNos').get("value")
    MFgPartNum9 = soup.find(id='ctl00_ContentPlaceHolder1_gvOrderDetail_ctl11_txtMfgPartNos').get("value")
    MFgPartNum10 = soup.find(id='ctl00_ContentPlaceHolder1_gvOrderDetail_ctl12_txtMfgPartNos').get("value")
    request_id_status1.loc[i, 'MFgPartNum'] = str(MFgPartNum)
    request_id_status1.loc[i, 'MFgPartNum1'] = str(MFgPartNum1)
    request_id_status1.loc[i, 'MFgPartNum2'] = str(MFgPartNum2)
    request_id_status1.loc[i, 'MFgPartNum3'] = str(MFgPartNum3)
    request_id_status1.loc[i, 'MFgPartNum4'] = str(MFgPartNum4)
    request_id_status1.loc[i, 'MFgPartNum5'] = str(MFgPartNum5)
    request_id_status1.loc[i, 'MFgPartNum6'] = str(MFgPartNum6)
    request_id_status1.loc[i, 'MFgPartNum7'] = str(MFgPartNum7)
    request_id_status1.loc[i, 'MFgPartNum8'] = str(MFgPartNum8)
    request_id_status1.loc[i, 'MFgPartNum9'] = str(MFgPartNum9)
    request_id_status1.loc[i, 'MFgPartNum10'] = str(MFgPartNum10)
    #closes the current tab
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
#exporting the data to excel

request_id_status1.to_csv("DFT results.csv", index=False)
driver.close()
end = timer()
print("Time Taken:", end-start)





