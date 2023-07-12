import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv
import pandas as pd

chrome_options = Options()
# Run in headless mode without opening a browser window
chrome_options.add_argument('--headless')


def get_data(rollnooo, rng):
    regd_no_ = []
    student_name_ = []
    ds_grade_ = []
    csa_grade_ = []
    c_grade_ = []
    os_grade_ = []
    db_grade_ = []
    c_lab_grade_ = []
    os_lab_grade_ = []
    db_lab_grade_ = []
    result_ = []
    ###########################
    for i in range(rng+1):
        roll = rollnooo+i

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(
            'http://www.bputexam.in/studentsection/resultpublished/studentresult.aspx')

        session_dropdown = driver.find_element(
            By.XPATH, '//*[@id="ddlSession"]')
        session_dropdown_options = session_dropdown.find_elements(
            By.TAG_NAME, 'option')
        session_dropdown_options[-1].click()

        reg_no_input = driver.find_element(By.XPATH, '//*[@id="txtRegNo"]')
        reg_no_input.send_keys(roll)

        dob_input = driver.find_element(
            By.XPATH, '//*[@id="dpStudentdob_dateInput"]')
        dob_input.clear()  # Clear any existing value
        dob_input.send_keys('13/10/2001')

        # Click the "View" button
        view_button = driver.find_element(By.XPATH, '//*[@id="btnView"]')
        view_button.click()

        # Click the "View Result" button inside the table
        view_result_button = driver.find_element(
            By.XPATH, '//*[@id="gvResultSummary_ctl02_lnkViewResult"]')
        view_result_button.click()

        # Fetch the student details and marks
        reg_no_span = driver.find_element(By.XPATH, '//*[@id="lblRollNo"]')
        student_name_span = driver.find_element(By.XPATH, '//*[@id="lblName"]')
        # fetching the subject grade

        dS_grade = driver.find_element(
            By.XPATH, '//*[@id="gvViewResult_ctl02_lblSubGradePoint"]')

        CSA_grade = driver.find_element(
            By.XPATH, '//*[@id="gvViewResult_ctl03_lblSubGradePoint"]')

        C_grade = driver.find_element(
            By.XPATH, '//*[@id="gvViewResult_ctl04_lblSubGradePoint"]')

        OS_grade = driver.find_element(
            By.XPATH, '//*[@id="gvViewResult_ctl05_lblSubGradePoint"]')

        DB_grade = driver.find_element(
            By.XPATH, '//*[@id="gvViewResult_ctl06_lblSubGradePoint"]')

        C_Lab_grade = driver.find_element(
            By.XPATH, '//*[@id="gvViewResult_ctl07_lblSubGradePoint"]')

        Os_Lab_grade = driver.find_element(
            By.XPATH, '//*[@id="gvViewResult_ctl08_lblSubGradePoint"]')

        Db_Lab_grade = driver.find_element(
            By.XPATH, '//*[@id="gvViewResult_ctl09_lblSubGradePoint"]')

        result_span = driver.find_element(
            By.XPATH, '//*[@id="gvViewResult_ctl10_lblSGPA"]')

        reg_no = reg_no_span.text
        student_name = student_name_span.text

        ds_grade = dS_grade.text

        csa_grade = CSA_grade.text

        c_grade = C_grade.text

        os_grade = OS_grade.text

        db_grade = DB_grade.text

        c_lab_grade = C_Lab_grade.text

        os_lab_grade = Os_Lab_grade.text

        db_lab_grade = Db_Lab_grade.text

        result = result_span.text

        regd_no_.append(reg_no)
        student_name_.append(student_name)
        ds_grade_.append(ds_grade)
        csa_grade_.append(csa_grade)
        c_grade_.append(c_grade)
        os_grade_.append(os_grade)
        db_grade_.append(db_grade)
        c_lab_grade_.append(c_lab_grade)
        os_lab_grade_.append(os_lab_grade)
        db_lab_grade_.append(db_lab_grade)
        result_.append(result)
    df = pd.DataFrame({
        "Registration no.": regd_no_,
        "Name": student_name_,
        "DS": ds_grade_,
        "CSA": csa_grade_,
        "C": c_grade_,
        "OS": os_grade_,
        "DB": db_grade_,
        "C_Lab": c_lab_grade_,
        "OS_Lab": os_lab_grade_,
        "DB_Lab": db_lab_grade_,
        "RESULT": result_
    })
    return df
    # with open('D:\python\\final_result.csv', 'a', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow([reg_no, student_name,ds_grade,csa_grade,c_grade,
    #                      os_grade,db_grade,c_lab_grade,
    #                     os_lab_grade,db_lab_grade,result])

# roll_number = 2205297152 ;
# for i in range (0,20):
#     get_results(roll_number + i)
