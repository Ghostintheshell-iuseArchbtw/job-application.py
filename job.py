import docx2txt
import PyPDF2

def extract_text_from_docx(docx_path):
    text = ""
    try:
        text = docx2txt.process(docx_path)
    except Exception as e:
        print(f"An error occurred while extracting text from DOCX: {str(e)}")
    return text

def submit_job_application(resume_file, job_application_url, field_id):
    try:
        # Initialize the web driver
        with webdriver.Chrome(executable_path="/path/to/chromedriver") as driver:
            # Open the job application page
            if not job_application_url:
                raise ValueError("Job application URL is not provided.")
            driver.get(job_application_url)

            # Check if the resume file exists
            if not os.path.isfile(resume_file):
                print("Resume file does not exist.")
                return

            # Upload your resume
            resume_input = driver.find_element_by_id("resume-upload")
            resume_input.send_keys(resume_file)

            # Wait for the resume to upload
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, field_id))
            )

            # Extract text from the uploaded resume
            if resume_file.endswith(".docx"):
                resume_text = extract_text_from_docx(resume_file)
            elif resume_file.endswith(".pdf"):
                resume_text = extract_text_from_pdf(resume_file)
            else:
                print("Unsupported resume format.")
                return

            # Populate the form field
            experience_field = driver.find_element_by_id(field_id)
            experience_field.send_keys(resume_text)

            # Submit the application
            submit_button = driver.find_element_by_id("submit-button")
            submit_button.click()

            print("Application submitted successfully.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Configuration
resume_file = "/home/ghostintheshell/Documents/resume.docx"
job_application_url = ""  # Specify the URL of the job application page
field_id = "experience"

# Submit the job application
submit_job_application(resume_file, job_application_url, field_id)
    try:
        text = docx2txt.process(docx_path)
    except Exception as e:
        print(f"An error occurred while extracting text from DOCX: {str(e)}")
    return text

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                text += page.extractText()
    except Exception as e:
        print(f"An error occurred while extracting text from PDF: {str(e)}")
    return text

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                text += page.extractText()
    except Exception as e:
        print(f"An error occurred while extracting text from PDF: {str(e)}")
    return text

def submit_job_application(resume_file, job_application_url, field_id):
    try:
        # Initialize the web driver
        driver = webdriver.Chrome(executable_path="/path/to/chromedriver")

        # Open the job application page
        driver.get(job_application_url)

        # Check if the resume file exists
        if not os.path.isfile(resume_file):
            print("Resume file does not exist.")
            return

        # Upload your resume
        resume_input = driver.find_element_by_id("resume-upload")
        resume_input.send_keys(resume_file)

        # Wait for the resume to upload
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, field_id))
        )

        # Extract text from the uploaded resume
        if resume_file.endswith(".docx"):
            resume_text = extract_text_from_docx(resume_file)
        elif resume_file.endswith(".pdf"):
            resume_text = extract_text_from_pdf(resume_file)
        else:
            print("Unsupported resume format.")
            return

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

# Configuration
resume_file = "/home/ghostintheshell/Documents/resume.docx"
job_application_url = ""  # Specify the URL of the job application page
field_id = "experience"

# Submit the job application
submit_job_application(resume_file, job_application_url, field_id)

