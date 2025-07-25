from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

def check_slots(license_number, booking_ref):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Set correct path to ChromeDriver using Service
    service = Service("C:/Users/ScorpioX/Desktop/order 2/chromedriver-win32/chromedriver.exe")

    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get('https://driver-services.dvsa.gov.uk/change-driving-test/what-is-your-reference-number')
        time.sleep(3)

        # Step 1: Fill in form
        driver.find_element("id", "driving-licence-number").send_keys(license_number)
        driver.find_element("id", "application-reference-number").send_keys(booking_ref)
        driver.find_element("css selector", "button[type=submit]").click()
        time.sleep(5)

        # Step 2: Check if slots are visible (You must update this based on live site changes)
        page_source = driver.page_source
        return "no earlier date" not in page_source.lower()

    except Exception as e:
        print(f"Error: {e}")
        return False

    finally:
        driver.quit()
