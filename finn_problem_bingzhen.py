"""
pip install selenium and beautifulsoup4 if not installed on your environment.
Download the chrome driver, extract it and then copy the file in the folder of the program.
Run python finn_problem_bingzhen.py with arguments (closed with double quotes) to add additional searchs.
For example, run python finn_problem_bingzhen.py "Finn AI | The Leading" "AI chatbot" "bank chatbot"
The test result is in the file test_result.log
"""

from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import sys

def autoGoogleSearch(srh_terms):
    # Open the Chrome. Note that the driver is the folder of this py file
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(executable_path=".\chromedriver.exe", chrome_options=options)
    for term in srh_terms:
        # Open the website google.ca
        browser.implicitly_wait(0.5)
        browser.get(r"https://www.google.ca/")
        # lcoate search box and search terms
        srh_box = browser.find_element_by_name("q")
        srh_box.send_keys(term)
        srh_box.submit()
        sleep(0.5)
        # Find the first result
        b_soup = BeautifulSoup(browser.page_source, 'html.parser')
        src_results = b_soup.find_all('div', class_="yuRUbf")
        res_url = ""
        if len(src_results):
            res_url = src_results[0].a.get('href')
            print(res_url)
        # Record test result into a log file
        test_result = "Passed" if ".finn.ai" in res_url else "Failed"
        log_line = "Search term {} is {}".format(term, test_result)
        with open("test_results.log", "a+") as file:
            # append the log into the file line by line
            file.seek(0)
            content = file.read(100)
            if len(content) > 0:
                file.write("\n")
            file.write(log_line)

if __name__ == "__main__":
    terms = [
        "Finn AI",
        "Personal banking chatbot",
        "Natural language banking chatbot",
        "AI powered banking chatbot",
        "AI platform for banking"
    ]
    # add additional search to terms
    if len(sys.argv) > 1:
        add_term = sys.argv[1:]
        terms.extend(add_term)
        print(add_term)
    autoGoogleSearch(terms)