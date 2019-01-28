
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time


driver = webdriver.Chrome()
driver.get("https://auth.csun.edu/cas/login?method=POST&service=https%3A%2F%2Fmynorthridge.csun.edu%2Fpsp%2FPANRPRD%2F%3Fcmd%3Dlogin%26languageCd%3DENG")
elem = driver.find_element_by_id("username")
elem.clear()
elem.send_keys("jt80851")
elem = driver.find_element_by_id("password")
elem.send_keys(*****)
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

myList = [109769177, 106716127,106716127 ]

for var in outstanding:
    
    driver.get("https://cmsweb.csun.edu/psc/CNRPRD/EMPLOYEE/EMPL/c/NR_SR_STUDENT_INQUIRY.NR_QA_QUERY.GBL?PORTALPARAM_PTCNAV=NR_QA_QUERY1&EOPP.SCNode=EMPL&EOPP.SCPortal=EMPLOYEE&EOPP.SCName=CSUN_SA&EOPP.SCLabel=Inquire&EOPP.SCFName=INQUIRE2&EOPP.SCSecondary=true&EOPP.SCPTfname=INQUIRE2&FolderPath=PORTAL_ROOT_OBJECT.CSUN_SA.NR_SR_STUDENT_INQUIRY.INQUIRE2.NR_QA_QUERY1&IsFolder=false&PortalActualURL=https%3a%2f%2fcmsweb.csun.edu%2fpsc%2fCNRPRD%2fEMPLOYEE%2fEMPL%2fc%2fNR_SR_STUDENT_INQUIRY.NR_QA_QUERY.GBL&PortalRegistryName=EMPLOYEE&PortalServletURI=https%3a%2f%2fcmsweb.csun.edu%2fpsp%2fCNRPRD%2f&PortalURI=https%3a%2f%2fcmsweb.csun.edu%2fpsc%2fCNRPRD%2f&PortalHostNode=SA&NoCrumbs=yes&PortalKeyStruct=yes")
    time.sleep(1)
  
    elem = driver.find_element_by_id("NR_QA_STDNT_S1_EMPLID")
    elem.send_keys(var)
    elem.send_keys(Keys.RETURN)

    time.sleep(1)
       

    try:
        #find grad date/degree plan
        tab = driver.find_element_by_id("ICTAB_1")

        #find student GPA
        #tab = driver.find_element_by_id("ICTAB_3")
        
        if tab.is_displayed():
         
            tab.click()
        
            time.sleep(1)
                
            name = driver.find_element_by_id("NR_QA_STDNT_SRC_NAME_PSFORMAT")

            print(str(name.text))
                
            #find student GPA

            #csungpa = driver.find_element_by_id("NR_QA_DERIVED_NR_QA_CSUN_GPA$0")
            #totalgpa = driver.find_element_by_id("NR_QA_DERIVED_NR_QA_TOT_GPA$0")

            #find number of units enrolled in
            #if str(driver.find_element_by_id("STDNT_CAR_TM_VW_STRM$0").text) != "2183":

            #    driver.find_element_by_id("$ICField5$hdown$0").click()
            #    time.sleep(2)
            #    numofunits = driver.find_element_by_id("NR_QA_DERIVED_NR_UNT_ENRL$0")
            #    print("Number of units - Spring 2017: " + str(numofunits.text))

            
            #else:
            #    numofunits = driver.find_element_by_id("NR_QA_DERIVED_NR_UNT_ENRL$0")
            #    print("Number of units - Spring 2017: " + str(numofunits.text))
                

            #find graduation date
            #grad = driver.find_element_by_id("win0divTERM_TBL_DESCR$36$$0")
           
            #find degreecode
            #this will find the last button to jump to last degree code for student
            #if it doesn't find the last button, it will simply look for the degree code

            try:
               driver.find_element_by_id("$ICField20$hend$0")
               driver.find_element_by_id("$ICField20$hend$0").click()
               major = driver.find_element_by_id("ACAD_PLAN_TBL_DESCR$0")
               #plan = driver.find_element_by_id("ACAD_PLAN_ACAD_PLAN$0")
               
               
           
            except NoSuchElementException: 
                print("")
            
            finally:
                 major = driver.find_element_by_id("ACAD_PLAN_TBL_DESCR$0") 
            #    plan = driver.find_element_by_id("ACAD_PLAN_ACAD_PLAN$0")

            #print("Name: " + str(name.text))

            #print("GPA: " + str(csungpa.text))
            #print("Total GPA: " + str(totalgpa.text) + '\n')

            #print("Graduation Date: " + str(grad.text) + '\n')
            #print("Academic plan: " + str(plan.text) + '\n')
            print("Major: " + str(major.text) + '\n')

        
    except NoSuchElementException:
        print('\n' + "Check " + str(var) + " manually"+ '\n' )

#driver.close()
#sys.exit(0)
       
        
        







