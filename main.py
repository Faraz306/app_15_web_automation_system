from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC

class WebAutomation:
    def __init__(self):
        chrome_options = Options()

        chrome_options.add_argument("--disable-search-engine-choice-screen")

        chrome_options.add_experimental_option("detach", True)

        service = Service("chromedriver-win64/chromedriver.exe")

        self.driver = webdriver.Chrome(service=service, options=chrome_options)

        self.driver.get("https://demoqa.com/login")
        self.driver.execute_script("window.location.replace('https://demoqa.com/login');")


    def login(self, name, password):
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "userName")))
        username_field.click()

        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
        password_field.click()

        login_button = self.driver.find_element(By.ID, "login")
        login_button.click()

        username_field.send_keys(name)
        password_field.send_keys(password)
        self.driver.execute_script("arguments[0].click();", login_button)


    def text_box(self, username, email, currentaddress, permanentaddress):
        self.driver.get("https://demoqa.com/text-box")

        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="root"]/div[1]/div/div/div[1]/div/div/div[1]/span/div')))
        elements.click()
        text_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "item-0")))
        text_box.click()
        user_name = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "userName")))
        user_name.click()
        user_email = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "userEmail")))
        user_email.click()
        current_address = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "currentAddress")))
        current_address.click()
        permanent_address = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "permanentAddress")))
        permanent_address.click()
        user_name.send_keys(username)
        user_email.send_keys(email)
        current_address.send_keys(currentaddress)
        permanent_address.send_keys(permanentaddress)

    def download_file(self):

        self.driver.get("https://demoqa.com/upload-download")

        download_element_button = self.driver.find_element(By.ID, "item-7")
        download_element_button.click()

        download_file = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "uploadFile")))
        download_file.click()
        download_file.send_keys(r"C:\Users\Faraz\PycharmProjects\PythonProject3\pikachu.png")

        download_button = self.driver.find_element(By.ID, "downloadButton")
        download_button.click()
    def close(self):
        self.driver.quit()

if __name__ == "__main__":

    automate_web = WebAutomation()
    automate_web.login(name="Yamaan Faraz", password="20164854YHFa$")
    automate_web.text_box(username="Yamaan Faraz", email="farazyamaan@gmail.com"
                          , currentaddress="Rambagh Colony, near Nauchandi Thana, Gali no.1, Meerut"
                          , permanentaddress="Rambagh Colony, near Nauchandi Thana, Gali no.1, Meerut")
    automate_web.download_file()
    automate_web.close()
