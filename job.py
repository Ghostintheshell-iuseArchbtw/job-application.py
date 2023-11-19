##change format from pdf to docx msf 365
import PyPDF2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

##ADDED CONFIG AND SUBIMT TO THE JOB APPLICATION TO TOP OF CODE FOR CALIRITY
# Configuration
resume_file = "/home/ghostintheshell/Documents/resume.docx"
##needs specification
job_application_url = ""
field_id = "experience"

# Submit the job application
submit_job_application(resume_file, job_application_url, field_id)
## change experince to starting filed 
def extract_text_from_pdf(pdf_path):
    text = "experince"
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
    return text

def submit_job_application(resume_file, job_application_url, field_id):
    try:
        # Initialize the web driver
        driver = webdriver.Chrome(executable_path="/path/to/chromedriver")

        # Open the job application page
        driver.get(job_application_url)

        # Upload your resume
        resume_input = driver.find_element_by_id("resume-upload")
        resume_input.send_keys(resume_file)

        # Wait for the resume to upload
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, field_id))
        )

        # Extract text from the uploaded resume
        resume_text = extract_text_from_pdf(resume_file)

        # Populate the form field
        experience_field = driver.find_element_by_id(field_id)
        experience_field.send_keys(resume_text)

        # Submit the application
        submit_button = driver.find_element_by_id("submit-button")
        submit_button.click()
        
        print("Application submitted successfully.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        # Close the browser when done
        driver.quit()

