from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

StudentID = "" #7 Digit Student Code
Password = "" #Password
options = webdriver.ChromeOptions()
PATH = "" #location of the chrome webdriver for selenium

driver = webdriver.Chrome(PATH, chrome_options=options)
Website= "" #Website for your omnivox
driver.get(Website)


driver.find_element_by_id("Identifiant").send_keys(StudentID)
driver.find_element_by_id("Password").send_keys(Password)
driver.find_element_by_class_name("btn.green.darken-3.right.recaptcha-trigger.no-margin-right").click()
ScheduleMakingTime=1622787780
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_partOffreServices_offreV2_INSC")))
driver.find_element_by_xpath('//*[@id="ctl00_partOffreServices_offreV2_INSC"]/span').click()

Time= 1623250798

while Time - int(time.time())>0:
    continue
else:
    
    Thing='1'
    while Thing=='1':
        
        try:
            driver.find_element_by_xpath('//*[@id="tblContenuSSO"]/table/tbody/tr/td/table/tbody/tr/td/center/form/button').click()
            Thing='ergrt'
        except:
            driver.refresh()
    
    CourseCodes=['PRO-LBM', '420-LCU-05', '345-LPH-MS', '603-103-MQ']
    
    for names in CourseCodes: #Add them to the course offerings
        Thing='None'
        while Thing=='None':
            try:
                try:
                    driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td/table/tbody/tr/td/center/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td[1]/center/div[2]/form/font/input[1]').clear()
                except:
                    continue
                driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td/table/tbody/tr/td/center/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td[1]/center/div[2]/form/font/input[1]').send_keys(names)
                driver.find_element_by_xpath('//*[@id="btnAjouter"]').click()
                Thing='549829'
            except:
                continue
    
    
    Teacher_Name={'PRO-LBM':'02', '345-LPH-MS':'04', '420-LCU-05':'01', '603-103-MQ':'20'}    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tblContenuSSO")))
    
    for names in CourseCodes: #Add to the dropdowns
        Group='Groupe'+str(names.replace('-',''))
        section= Teacher_Name.get(names)
        try:
            driver.find_element_by_xpath('//*[@name="'+Group+'"]/option[contains(.,"'+section+'")]').click()
        except:
            driver.find_element_by_xpath('//*[@name="'+Group+'"]/option[text()="Try all"]').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "divSoumettre")))
    driver.find_element_by_xpath('//*[@id="divSoumettre"]/input').click()
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tblContenuSSO")))
        driver.find_element_by_xpath('//*[@id="tblContenuSSO"]/table/tbody/tr/td/table/tbody/tr/td/form[1]/font/b/a').click()
    except:
        pass
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "divConfirm")))
    driver.find_element_by_xpath('//*[@id="divConfirm"]/input[1]').send_keys(Password)


    driver.find_element_by_xpath('//*[@id="divConfirm"]/input[2]').click()
