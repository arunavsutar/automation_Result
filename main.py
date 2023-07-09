import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv

chrome_options = Options()
chrome_options.add_argument('--headless')  # Run in headless mode without opening a browser window


def get_results(roll):
    driver = webdriver.Chrome(options=chrome_options) ;
    driver.get('http://www.bputexam.in/studentsection/resultpublished/studentresult.aspx')

    session_dropdown = driver.find_element(By.XPATH, '//*[@id="ddlSession"]')
    session_dropdown_options = session_dropdown.find_elements(By.TAG_NAME, 'option')
    session_dropdown_options[-1].click()

    reg_no_input = driver.find_element(By.XPATH, '//*[@id="txtRegNo"]')
    reg_no_input.send_keys(roll)

    dob_input = driver.find_element(By.XPATH, '//*[@id="dpStudentdob_dateInput"]')
    dob_input.clear()  # Clear any existing value
    dob_input.send_keys('13/10/2001')

    # Click the "View" button
    view_button = driver.find_element(By.XPATH, '//*[@id="btnView"]')
    view_button.click()

    # Click the "View Result" button inside the table
    view_result_button = driver.find_element(By.XPATH, '//*[@id="gvResultSummary_ctl02_lnkViewResult"]')
    view_result_button.click()

    # Fetch the student details and marks
    reg_no_span = driver.find_element(By.XPATH, '//*[@id="lblRollNo"]')
    student_name_span = driver.find_element(By.XPATH, '//*[@id="lblName"]')
    #fetching the subject grade

    dS_credit = driver.find_element(By.XPATH,'//*[@id="gvViewResult_ctl02_lblSubCredit"]')
    dS_grade  = driver.find_element(By.XPATH,'//*[@id="gvViewResult_ctl02_lblSubGradePoint"]')

    CSA_credit = driver.find_element(By.XPATH,'//*[@id="gvViewResult_ctl03_lblSubCredit"]')
    CSA_grade  = driver.find_element(By.XPATH,'//*[@id="gvViewResult_ctl03_lblSubGradePoint"]')

    C_credit = driver.find_element(By.XPATH,'//*[@id="gvViewResult_ctl04_lblSubCredit"]')
    C_grade  = driver.find_element(By.XPATH,'//*[@id="gvViewResult_ctl04_lblSubGradePoint"]')

    OS_credit = driver.find_element(By.XPATH,'//*[@id="gvViewResult_ctl05_lblSubCredit"]')
    OS_grade  = driver.find_element(By.XPATH,'//*[@id="gvViewResult_ctl05_lblSubGradePoint"]')

    DB_credit = driver.find_element(By.XPATH,'//*[@id="gvViewResult_ctl06_lblSubCredit"]')
    DB_grade  = driver.find_element(By.XPATH,'//*[@id="gvViewResult_ctl06_lblSubGradePoint"]')
    
    C_Lab_credit = driver.find_element(By.XPATH,'//*[@id="gvViewResult_ctl07_lblSubCredit"]')
    C_Lab_grade  = driver.find_element(By.XPATH,'//*[@id="gvViewResult_ctl07_lblSubGradePoint"]')

    Os_Lab_credit = driver.find_element(By.XPATH,'//*[@id="gvViewResult_ctl08_lblSubCredit"]')
    Os_Lab_grade  = driver.find_element(By.XPATH,'//*[@id="gvViewResult_ctl08_lblSubGradePoint"]')

    Db_Lab_credit = driver.find_element(By.XPATH,'//*[@id="gvViewResult_ctl09_lblSubCredit"]')
    Db_Lab_grade  = driver.find_element(By.XPATH,'//*[@id="gvViewResult_ctl09_lblSubGradePoint"]')
 


    result_span = driver.find_element(By.XPATH, '//*[@id="gvViewResult_ctl10_lblSGPA"]')

    
    print("Registration Number:", reg_no_span.text)
    print("Student Name:", student_name_span.text)

    print("Subject: Data Structures")
    print("Credit:", dS_credit.text)
    print("Grade:", dS_grade.text)

    print("Subject: Computer System Architecture")
    print("Credit:", CSA_credit.text)
    print("Grade:", CSA_grade.text)

    print("Subject: C Programming")
    print("Credit:", C_credit.text)
    print("Grade:", C_grade.text)

    print("Subject: Operating Systems")
    print("Credit:", OS_credit.text)
    print("Grade:", OS_grade.text)

    print("Subject: Database Management")
    print("Credit:", DB_credit.text)
    print("Grade:", DB_grade.text)

    print("Subject: C Lab")
    print("Credit:", C_Lab_credit.text)
    print("Grade:", C_Lab_grade.text)

    print("Subject: OS Lab")
    print("Credit:", Os_Lab_credit.text)
    print("Grade:", Os_Lab_grade.text)

    print("Subject: DB Lab")
    print("Credit:", Db_Lab_credit.text)
    print("Grade:", Db_Lab_grade.text)

    print("Result:", result_span.text)


    
roll_number = 2205297085 ;
for i in range (0,2):
    get_results(roll_number + i)

