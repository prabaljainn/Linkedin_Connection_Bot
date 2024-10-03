# importing the required modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from Scripts import constants
import csv
import time

# setup


def configurations():
    global driver
    global options

    # options = Options()
    # # opens the window in full screen
    # options.add_argument("--start-maximized")
    # options.binary_location = "./ChromeDriver/chromedriver.exe"


    # setting the Chrome Driver path
    driver = webdriver.Chrome()
    driver.get("https://www.linkedin.com/login")

    # assert "No results found." not in driver.page_source
    # driver.close()
    # assert "Python" in driver.title

    # driver = webdriver.Chrome(options=options, executable_path="ChromeDriver/chromedriver.exe")  # For mac use -> /usr/local/bin/chromedriver


# this class deals with the CSV file operations like opening the file, setting up the writer, inserting new row, etc.
class Csv_io:
    def __init__(self, filename, mode, newline):
        self.filename = filename
        self.mode = mode
        self.newline = newline

        self.openfile()
        self.writer_setup()

    # opens file
    def openfile(self):
        self.file_to_write = open(
            self.filename, mode=self.mode, newline=self.newline)

    # initialises the writer object
    def writer_setup(self):
        self.csv_writer = csv.writer(self.file_to_write)

    # inserts a new row into the CSV file
    def insert_row(self, info):
        self.csv_writer.writerow(info)

    def __str__(self):
        return 'this class deals with the CSV file operations'

# this class deals with the DOM operations like grabbing the elements using selectors, clicking on elements, sending text to elements, etc.


class Webpage:
    # opens the given url
    def visit(self, url):
        driver.get(url)

    def click_with_xpath_selector(self, xpath_selector):
        driver.find_element_by_xpath(xpath_selector).click()
    # clicks the element selected using CSS Selector

    def click_with_css_selector(self, css_selector):
        driver.find_element(css_selector).click()

    # gets the element selected using CSS Selector
    def grab_element_with_css_selector(self, css_selector):
        return driver.find_element(css_selector)

    # gets the elements* selected using CSS Selector
    def grab_elements_with_css_selector(self, css_selector):
        return driver.find_elements_by_css_selector(css_selector)

    # sends the entered text to the element selected using CSS Selector
    def type_value_with_css_selector(self, css_selector, keys):
        driver.find_element(css_selector).send_keys(keys)

    # gets the text from the element selected using CSS Selector
    def grab_text_with_css_selector(self, css_selector):
        return driver.find_element(css_selector).text

    # returns the url of the current page
    def get_url(self):
        return driver.current_url

# this class deals with the browser operations like ending the session, going back to previous page, wait, etc.


class Browser:
    # end the current session
    def end_session(self):
        driver.quit()

    # go back to previous page
    def go_back(self):
        driver.back()

    # wait/sleep for given time
    def wait(self, duration):
        driver.implicitly_wait(duration)

# this is the user class


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# logs text onto python console


def log(text):
    print(text)

# main function
def main():
    configurations()

    user = User(constants.username, constants.password)

    csv_io = Csv_io('OutputFolder/dataset.csv', 'a', '')

    webpage = Webpage()

    browser = Browser()

    browser.wait(2)

    # webpage.visit("https://www.linkedin.com/login")
    userName = driver.find_element(By.ID, "username")
    userName.clear()
    userName.send_keys(user.username)
    userName.send_keys(Keys.RETURN)
    
    password = driver.find_element(By.ID, "password")
    password.clear()
    password.send_keys(user.password)
    password.send_keys(Keys.RETURN)

    # elem.send_keys('andrepeixoto@gmail.com')
    
    # webpage.type_value_with_css_selector("input[id='username']", user.username)
    # webpage.type_value_with_css_selector("input[id='password']", user.password)
    # webpage.click_with_css_selector("button[type='submit']")

    for keyword in list(constants.commaseparated.split(';')):
        for page in range(1, int(constants.upto_page) + 1):
            time.sleep(5)

            link = "https://www.linkedin.com/search/results/people/?keywords=" + \
                keyword + "&origin=CLUSTER_EXPANSION&network=%5B%22S%22%2C%22O%22%5D&page=" + str(page)
            
            driver.get(link)

            list_of_cards = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'reusable-search__result-container'))
        )

            log(f"a total of {len(list_of_cards)} Connections found on page {page} for {keyword}")

            for i in range(1, len(list_of_cards) + 1):
                time.sleep(2)

                try:
                    button_on_card = webpage.grab_element_with_css_selector(
                        f"li[class= 'reusable-search__result-container ']:nth-child({i}) button").is_enabled()

                    button_text = webpage.grab_text_with_css_selector(
                        f"li[class= 'reusable-search__result-container ']:nth-child({i}) button span")

                    if button_on_card == True and button_text == 'Connect':
                        time.sleep(1)
                        webpage.click_with_css_selector(
                            f"li[class= 'reusable-search__result-container ']:nth-child({i}) span a span span")

                        time.sleep(2)

                        name_grab = webpage.grab_text_with_css_selector("h1")
                        browser.wait(10)
                        # webpage.click_with_css_selector("button[data-control-name='connect']")
                        # webpage.click_with_css_selector("button[class= 'artdeco-button artdeco-button--2 artdeco-button--primary ember-view pvs-profile-actions__action']")
                        connect_xpath = "/html[1]/body[1]/div[6]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/section[1]/div[2]/div[3]/div[1]/button[1]"
                        webpage.click_with_xpath_selector(connect_xpath)
                        time.sleep(0)

                        webpage.click_with_css_selector(
                            "button[aria-label='Send now']")

                        description1 = webpage.grab_text_with_css_selector(
                            "div[class= 'text-body-medium break-words']")

                        description2 = webpage.grab_text_with_css_selector(
                            "span[class = 'text-body-small inline t-black--light break-words']")

                        link_to_profile = webpage.get_url()

                        time.sleep(1)

                        log(f"{constants.Bcolors.WARNING}{name_grab} who is {description1} at {description2} for profile {link_to_profile}{constants.Bcolors.ENDC}")

                        info = [name_grab, description1,
                                description2, link_to_profile]

                        csv_io.insert_row(info)

                        time.sleep(1)

                    webpage.visit(link)

                    browser.wait(10)

                except NoSuchElementException:
                    pass
                except Exception as e:
                    log(e)

        log(f"{constants.Bcolors.UNDERLINE} All New Connection's data appended to dataset.csv {constants.Bcolors.ENDC}")

        browser.end_session()

        csv_io.insert_row(["---------", "----------",
                          "----------", "-------------"])
