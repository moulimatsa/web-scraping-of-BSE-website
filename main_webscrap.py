from selenium import webdriver
import time
import os
import csv



url = 'https://www.bseindia.com/corporates/Comp_Results.aspx?Code=500010'

options = webdriver.ChromeOptions()

download_dir = r'C:\Users\matsa\Downloads\new12.pdf'
os.mkdir(download_dir)
profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
               "download.default_directory": download_dir , "download.extensions_to_open": "applications/pdf"}
options.add_experimental_option('prefs', profile)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get(url)
time.sleep(1)
window_before = driver.window_handles[0]




def standalone():
    time.sleep(1)
    try:
        driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_lnkStandalone"]').click()
    except:
        pass
    time.sleep(1)
    x = driver.find_elements_by_xpath('//*[@id="ContentPlaceHolder1_lnkDownload"]')
    for xs in x:
        xs.click()

def detailed():
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_lnkDetailed"]').click()
    time.sleep(1)
    y = driver.find_elements_by_xpath('//*[@id="ContentPlaceHolder1_lnkDownload"]')
    for ys in y:
        ys.click()


def segment():
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_lnlSegment"]').click()
    time.sleep(1)
    z = driver.find_elements_by_xpath('//*[@id="ContentPlaceHolder1_lnkDownload"]')
    for zs in z:
        zs.click()


def consolidated():
    driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_lnkConsolidated"]').click()
    time.sleep(2)
    table = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_tbl_typeID"]')
    body = table.find_element_by_xpath('//*[@id="ContentPlaceHolder1_tbl_typeID"]/tbody')

    file_data = []

    body_rows = body.find_elements_by_tag_name('tr')

    for row in body_rows:
        data = row.find_elements_by_tag_name('td')
        file_row = []
        for datum in data:
            datum_text = datum.text
            file_row.append(datum_text)
        file_data.append(",".join(file_row))

    f = open("src3.csv", 'a+')
    f.write("\n".join(file_data))
    f.close()


def annual_results():
    time.sleep(1)
    try:
        jun18q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[2]/td[2]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        sep18q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[2]/td[3]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        dec18q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[2]/td[4]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar19q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[2]/td[5]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar19y = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[2]/td[7]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        jun17q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[3]/td[2]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        sep17q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[3]/td[3]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        dec17q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[3]/td[4]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar18q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[3]/td[5]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar18y = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[3]/td[7]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        jun16q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[4]/td[2]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        sep16q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[4]/td[3]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        dec16q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[4]/td[4]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar17q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[4]/td[5]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar17y = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[4]/td[7]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        jun15q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[5]/td[2]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        sep15q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[5]/td[3]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        dec15q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[5]/td[4]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar16q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[5]/td[5]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar16y = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[5]/td[7]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        jun14q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[6]/td[2]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        sep14q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[6]/td[3]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        dec14q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[6]/td[4]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar15q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[6]/td[5]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar15y = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[6]/td[7]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        jun13q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[7]/td[2]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        sep13q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[7]/td[3]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        dec13q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[7]/td[4]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar14q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[7]/td[5]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar14y = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[7]/td[7]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        jun12q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[8]/td[2]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        sep12q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[8]/td[3]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        dec12q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[8]/td[4]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar13q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[8]/td[5]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar13y = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[8]/td[7]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        jun11q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[9]/td[2]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        sep11q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[9]/td[3]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        dec11q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[9]/td[4]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar12q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[9]/td[5]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar12y = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[9]/td[7]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        jun10q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[10]/td[2]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        sep10q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[10]/td[3]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        dec10q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[10]/td[4]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar11q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[10]/td[5]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar11y = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[10]/td[7]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        jun9q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[11]/td[2]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        sep9q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[11]/td[3]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        dec9q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[11]/td[4]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar10q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[11]/td[5]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar10y = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[11]/td[7]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        jun8q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[12]/td[2]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        sep8q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[12]/td[3]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        dec8q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[12]/td[4]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar9q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[12]/td[5]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar9y = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[12]/td[7]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        jun7q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[13]/td[2]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        sep7q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[13]/td[3]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        dec7q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[13]/td[4]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar8q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[13]/td[5]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar8y = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[13]/td[7]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        jun6q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[14]/td[2]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        sep6q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[14]/td[3]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        dec6q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[14]/td[4]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar7q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[14]/td[5]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar7y = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[14]/td[7]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        jun5q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[15]/td[2]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        sep5q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[15]/td[3]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        dec5q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[15]/td[4]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar6q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[15]/td[5]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar6y = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[15]/td[7]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        jun4q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[16]/td[2]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        sep4q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[16]/td[3]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        dec4q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[16]/td[4]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar5q = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[16]/td[5]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)
    try:
        mar5y = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[16]/td[7]/a').click()
        try:
            standalone()
        except:
            pass
        try:
            consolidated()
        except:
            pass
        try:
            detailed()
        except:
            pass
        try:
            segment()
        except:
            pass
        driver.get(url)
    except:
        pass

    time.sleep(1)

    try:
        annual_report18 = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[2]/td[8]/a')
        for ar18 in annual_report18:
            time.sleep(1)
            ar18.click()
    except:
        pass

    try:
        annual_report17 = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[3]/td[8]/a')
        for ar17 in annual_report17:
            time.sleep(1)
            ar17.click()
    except:
        pass
    try:
        annual_report16 = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[4]/td[8]/a')
        for ar16 in annual_report16:
            time.sleep(1)
            ar16.click()
    except:
        pass
    try:
        annual_report15 = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[5]/td[8]/a')
        for ar15 in annual_report15:
            time.sleep(1)
            ar15.click()
    except:
        pass
    try:
        annual_report14 = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[6]/td[8]/a')
        for ar14 in annual_report14:
            time.sleep(1)
            ar14.click()
    except:
        pass
    try:
        annual_report13 = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[7]/td[8]/a')
        for ar13 in annual_report13:
            time.sleep(1)
            ar13.click()
    except:
        pass
    try:
        annual_report12 = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[8]/td[8]/a')
        for ar12 in annual_report12:
            time.sleep(1)
            ar12.click()
    except:
        pass
    try:
        annual_report11 = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[9]/td[8]/a')
        for ar11 in annual_report11:
            time.sleep(1)
            ar11.click()
    except:
        pass
    try:
        annual_report10 = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[10]/td[8]/a')
        for ar10 in annual_report10:
            time.sleep(1)
            ar10.click()
    except:
        pass
    try:
        annual_report9 = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[11]/td[8]/a')
        for ar9 in annual_report9:
            time.sleep(1)
            ar9.click()
    except:
        pass
    try:
        annual_report8 = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[12]/td[8]/a')
        for ar8 in annual_report8:
            time.sleep(1)
            ar8.click()
    except:
        pass
    try:
        annual_report7 = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[13]/td[8]/a')
        for ar7 in annual_report7:
            time.sleep(1)
            ar7.click()
    except:
        pass
    try:
        annual_report6 = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[14]/td[8]/a')
        for ar6 in annual_report6:
            time.sleep(1)
            ar6.click()
    except:
        pass
    try:
        annual_report5 = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[15]/td[8]/a')
        for ar5 in annual_report5:
            time.sleep(1)
            ar5.click()
    except:
        pass
    try:
        annual_report4 = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_tdData"]/table/tbody/tr/td/table/tbody/tr[16]/td[8]/a')
        for ar4 in annual_report4:
            time.sleep(1)
            ar4.click()
    except:
        pass


def trade_values():
    pre_close = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(1) > div > table > tbody > tr:nth-child(1) > td.textsr")
    pre_cl_rel = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(1) > div > table > tbody > tr:nth-child(1) > td.textvalue.ng-binding")

    for pre in pre_close:
        for pre1 in pre_cl_rel:
            x1 = pre.text.strip()
            y1 = pre1.text.strip()

    open_val = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(1) > div > table > tbody > tr:nth-child(3) > td.textsr")
    open_rel = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(1) > div > table > tbody > tr:nth-child(3) > td.textvalue.ng-binding")

    for open_v in open_val:
        for open_r in open_rel:
            x2 = open_v.text.strip()
            y2 = open_r.text.strip()

    high_val = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(1) > div > table > tbody > tr:nth-child(5) > td.textsr")
    high_rel = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(1) > div > table > tbody > tr:nth-child(5) > td.textvalue.ng-binding")

    for high_v in high_val:
        for high_r in high_rel:
            x3 = high_v.text.strip()
            y3 = high_r.text.strip()

    low_val = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(1) > div > table > tbody > tr:nth-child(7) > td.textsr")
    low_rel = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(1) > div > table > tbody > tr:nth-child(7) > td.textvalue.ng-binding")

    for low_v in low_val:
        for low_r in low_rel:
            x4 = low_v.text.strip()
            y4 = low_r.text.strip()

    vwap_val = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(1) > div > table > tbody > tr:nth-child(9) > td.textsr")
    vwap_rel = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(1) > div > table > tbody > tr:nth-child(9) > td.textvalue.ng-binding")

    for vwap_v in vwap_val:
        for vwap_r in vwap_rel:
            x5 = vwap_v.text.strip()
            y5 = vwap_r.text.strip()

    fiftywkh_val = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(2) > div > table > tbody > tr:nth-child(1) > td.textsr > a")
    fiftywkh_rel = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(2) > div > table > tbody > tr:nth-child(1) > td.textvalue.ng-binding")

    for fiftywkh_v in fiftywkh_val:
        for fiftywkh_r in fiftywkh_rel:
            x6 = fiftywkh_v.text.strip()
            y6 = fiftywkh_r.text.strip()

    fiftywkl_val = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(2) > div > table > tbody > tr:nth-child(3) > td.textsr > a")
    fiftywkl_rel = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(2) > div > table > tbody > tr:nth-child(3) > td.textvalue.ng-binding")

    for fiftywkl_v in fiftywkl_val:
        for fiftywkl_r in fiftywkl_rel:
            x7 = fiftywkl_v.text.strip()
            y7 = fiftywkl_r.text.strip()

    upb_val = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(2) > div > table > tbody > tr:nth-child(5) > td.textsr")
    upb_rel = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(2) > div > table > tbody > tr:nth-child(5) > td.textvalue.ng-binding")

    for upb_v in upb_val:
        for upb_r in upb_rel:
            x8 = upb_v.text.strip()
            y8 = upb_r.text.strip()

    lpb_val = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(2) > div > table > tbody > tr:nth-child(7) > td.textsr")
    lpb_rel = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(2) > div > table > tbody > tr:nth-child(7) > td.textvalue.ng-binding")

    for lpb_v in lpb_val:
        for lpb_r in lpb_rel:
            x9 = lpb_v.text.strip()
            y9 = lpb_r.text.strip()

    avgqty_val = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(2) > div > table > tbody > tr:nth-child(9) > td.textsr")
    avgqty_rel = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(2) > div > table > tbody > tr:nth-child(9) > td.textvalue.ng-binding")

    for avgqty_v in avgqty_val:
        for avgqty_r in avgqty_rel:
            x10 = avgqty_v.text.strip()
            y10 = avgqty_r.text.strip()

    ttq_val = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(3) > div > table > tbody > tr:nth-child(1) > td.textsr")
    ttq_rel = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(3) > div > table > tbody > tr:nth-child(1) > td.textvalue.ng-binding")

    for ttq_v in ttq_val:
        for ttq_r in ttq_rel:
            x11 = ttq_v.text.strip()
            y11 = ttq_r.text.strip()

    turn_over_val = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(3) > div > table > tbody > tr:nth-child(3) > td.textsr")
    turn_over_rel = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(3) > div > table > tbody > tr:nth-child(3) > td.textvalue.ng-binding")

    for turn_over_v in turn_over_val:
        for turn_over_r in turn_over_rel:
            x12 = turn_over_v.text.strip()
            y12 = turn_over_r.text.strip()

    mcap_full_val = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(3) > div > table > tbody > tr:nth-child(5) > td.textsr")
    mcap_full_rel = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(3) > div > table > tbody > tr:nth-child(5) > td.textvalue.ng-binding")

    for mcap_full_v in mcap_full_val:
        for mcap_full_r in mcap_full_rel:
            x13 = mcap_full_v.text.strip()
            y13 = mcap_full_r.text.strip()

    mcap_ff_val = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(3) > div > table > tbody > tr:nth-child(7) > td.textsr")
    mcap_ff_rel = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(3) > div > table > tbody > tr:nth-child(7) > td.textvalue.ng-binding")

    for mcap_ff_v in mcap_ff_val:
        for mcap_ff_r in mcap_ff_rel:
            x14 = mcap_ff_v.text.strip()
            y14 = mcap_ff_r.text.strip()

    faceval_val = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(3) > div > table > tbody > tr:nth-child(9) > td.textsr ")
    faceval_rel = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(3) > div > table > tbody > tr:nth-child(9) > td.textvalue.ng-binding")

    for faceval_v in faceval_val:
        for faceval_r in faceval_rel:
            x15 = faceval_v.text.strip()
            y15 = faceval_r.text.strip()

    eps_val = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td.textsr")
    eps_rel = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td.textvalue.ng-binding")

    for eps_v in eps_val:
        for eps_r in eps_rel:
            x16 = eps_v.text.strip()
            y16 = eps_r.text.strip()

    ceps_val = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(4) > div > table > tbody > tr:nth-child(3) > td.textsr")
    ceps_rel = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(4) > div > table > tbody > tr:nth-child(3) > td.textvalue.ng-binding")

    for ceps_v in ceps_val:
        for ceps_r in ceps_rel:
            x17 = ceps_v.text.strip()
            y17 = ceps_r.text.strip()

    pe_val = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(4) > div > table > tbody > tr:nth-child(5) > td.textsr")
    pe_rel = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(4) > div > table > tbody > tr:nth-child(5) > td.textvalue.ng-binding")

    for pe_v in pe_val:
        for pe_r in pe_rel:
            x18 = pe_v.text.strip()
            y18 = pe_r.text.strip()

    pb_val = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(4) > div > table > tbody > tr:nth-child(7) > td.textsr")
    pb_rel = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(4) > div > table > tbody > tr:nth-child(7) > td.textvalue.ng-binding")

    for pb_v in pb_val:
        for pb_r in pb_rel:
            x19 = pb_v.text.strip()
            y19 = pb_r.text.strip()

    roe_val = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(4) > div > table > tbody > tr:nth-child(9) > td.textsr")
    roe_rel = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(4) > div > table > tbody > tr:nth-child(9) > td.textvalue.ng-binding")

    for roe_v in roe_val:
        for roe_r in roe_rel:
            x20 = roe_v.text.strip()
            y20 = roe_r.text.strip()

    category_val = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(5) > div > table > tbody > tr:nth-child(1) > td.textsr")
    category_rel = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(5) > div > table > tbody > tr:nth-child(1) > td.textvalue.ng-binding")

    for category_v in category_val:
        for category_r in category_rel:
            x21 = category_v.text.strip()
            y21 = category_r.text.strip()

    group_val = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(5) > div > table > tbody > tr:nth-child(3) > td.textsr")
    group_rel = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(5) > div > table > tbody > tr:nth-child(3) > td.textvalue.ng-binding")

    for group_v in group_val:
        for group_r in group_rel:
            x22 = group_v.text.strip()
            y22 = group_r.text.strip()

    index_val = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(5) > div > table > tbody > tr:nth-child(5) > td.textsr")
    index_rel = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(5) > div > table > tbody > tr:nth-child(5) > td.textvalue.ng-binding")

    for index_v in index_val:
        for index_r in index_rel:
            x23 = index_v.text.strip()
            y23 = index_r.text.strip()

    industry_val = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(5) > div > table > tbody > tr:nth-child(7) > td.textsr")
    industry_rel = driver.find_elements_by_css_selector(
        "#eqcommanheader > div:nth-child(5) > div > div:nth-child(5) > div > table > tbody > tr:nth-child(7) > td.textvalue.ng-binding")

    for industry_v in industry_val:
        for industry_r in industry_rel:
            x24 = industry_v.text.strip()
            y24 = industry_r.text.strip()

    header = ['id', x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22,
              x23, x24]
    rows = [
        [1, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16, y17, y18, y19, y20, y21, y22, y23,
         y24]
    ]

    with open('try.csv', 'w+') as f:
        csv_writer = csv.writer(f, quotechar="'")

        csv_writer.writerow(header)

        csv_writer.writerows(rows)


def buy_sell_price():
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)
    item = driver.find_element_by_xpath(
        '//*[@id="deribody"]/div[2]/div[2]/div[2]/div/div[1]/div/table/tbody/tr/td/table')
    driver.execute_script("arguments[0].click();", item)
    time.sleep(2)
    data1 = []
    for table in driver.find_elements_by_xpath(
            '//*[@id="deribody"]/div[2]/div[2]/div[2]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr'):
        data = [item.text.strip() for item in table.find_elements_by_xpath(".//*[self::td or self::th]")]
        data1.append(data)

    with open('a2.csv', 'w', newline='') as write_file:
        write = csv.writer(write_file)
        write.writerows([r] for r in data1)

def corp_announcements():
    options = webdriver.ChromeOptions()

    download_dir = r'C:\Users\matsa\Downloads\new11.pdf'
    os.mkdir(download_dir)
    profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
               "download.default_directory": download_dir, "download.extensions_to_open": "applications/pdf"}
    options.add_experimental_option('prefs', profile)
    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(10)
    driver.get(url)
    time.sleep(1)
    x = driver.find_elements_by_xpath('//*[@id="lblann"]/table/tbody/tr[4]/td/table/tbody/tr/td/a/i')

    for xs in x:
        time.sleep(3)
        xs.click()


def notices():
    url = 'https://www.bseindia.com/markets/MarketInfo/NoticesCirculars.aspx?txtscripcd=500010'
    options = webdriver.ChromeOptions()

    download_dir = r'C:\Users\matsa\Downloads\new34.pdf'
    os.mkdir(download_dir)
    profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
               "download.default_directory": download_dir, "download.extensions_to_open": "applications/pdf"}
    options.add_experimental_option('prefs', profile)
    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(10)
    driver.get(url)
    time.sleep(1)
    x = driver.find_elements_by_xpath('//*[@id="ContentPlaceHolder1_GridView2"]/tbody/tr/td[6]')

    for xs in x:
        time.sleep(3)
        xs.click()


def meetings():
    url = 'https://www.bseindia.com/stock-share-price/meetings/board-meetings/500010/'

    download_dir = r'C:\Users\matsa\Downloads\new31.pdf'
    os.mkdir(download_dir)
    profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
               "download.default_directory": download_dir, "download.extensions_to_open": "applications/pdf"}
    options.add_experimental_option('prefs', profile)
    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(10)
    driver.get(url)
    time.sleep(1)
    x = driver.find_element_by_xpath(
        '//*[@id="deribody"]/div[2]/div/div/table/tbody/tr/td/table/tbody/tr[11]/td/a/i').click()
    time.sleep(2)
    y = driver.find_elements_by_xpath('//*[@id="ContentPlaceHolder1_lnkDownload"]/i')

    for ys in y:
        time.sleep(1)
        ys.click()

def disclosures():
    options = webdriver.ChromeOptions()

    download_dir = r'C:\Users\matsa\Downloads\new31.pdf'
    os.mkdir(download_dir)
    profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
               "download.default_directory": download_dir, "download.extensions_to_open": "applications/pdf"}
    options.add_experimental_option('prefs', profile)
    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(10)
    driver.get(url)
    time.sleep(1)
    x = driver.find_element_by_xpath('//*[@id="l121"]').click()
    time.sleep(2)
    y = driver.find_elements_by_xpath('//*[@id="downloadlnk"]')

    for ys in y:
        time.sleep(1)
        ys.click()

    k = driver.find_element_by_xpath('//*[@id="l122"]').click()
    time.sleep(1)

    l = driver.find_element_by_xpath('//*[@id="downloadlnk"]')

    for ls in l:
        time.sleep(1)
        ls.click()

    g = driver.find_element_by_xpath('//*[@id="l123"]').click()
    time.sleep(1)

    h = driver.find_element_by_xpath('//*[@id="downloadlnk"]')
    for hs in h:
        time.sleep(1)
        hs.click()
