from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
import util

# mount webdriver
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.maximize_window()

# navigate to website
driver.get("https://www.educative.io/login")

# login
username = "danielszwimer@gmail.com"
password = "hk9scxbhhad4N@H"
time.sleep(4)
driver.find_element(By.ID, "email-field").send_keys(username)
time.sleep(5)
driver.find_element(By.ID, "password-field").send_keys(password)
time.sleep(1)
driver.find_element(By.XPATH, """//button[@class="contained-primary w-full mt-6 leading-6 p-2"]""").click()

time.sleep(25)

# make array of courses we want here

# course = "https://www.educative.io/courses/hands-on-php-mysql-crud-application"

courses = {"https://www.educative.io/courses/learn-the-a-to-z-of-amazon-web-services-aws/NEYAGllZr48": "Learn AWS",
           "https://www.educative.io/courses/cloud-architecture-a-guide-to-design-and-architect-your-cloud/qVl160R3xjk":"Cloud Architecture",
           "https://www.educative.io/courses/software-design-patterns-best-practices/xVovQB3Rknq":"Design Patterns",
           "https://www.educative.io/courses/learn-rust-from-scratch/g7MooO7APQ6":"Rust",
           "https://www.educative.io/courses/hands-on-blockchain-hyperledger-fabric/xV91vr9pZoP":"Blockchain",
           "https://www.educative.io/courses/software-architecture-in-java-design-development/R8vEvzW8060":"Software Architecture Java",
           "https://www.educative.io/courses/developing-microservices-with-spring-boot/B8l7VWGXl5k":"Microservices with Spring boot",
           "https://www.educative.io/courses/oauth2-with-spring-security/7Aq1E6vZqVA":"oAuth2 with Spring",
           "https://www.educative.io/courses/guide-to-java-programming/JE8QOyMponP":"Java",
           "https://www.educative.io/courses/advanced-docker-techniques/m2qYw8Mvl30":"Advanced Docker",
           "https://www.educative.io/courses/grokking-the-coding-interview/xl0ElGxR6Bq":"Grokking coding",
           "https://www.educative.io/courses/practical-guide-to-kubernetes/R8rn5n66WVK":"Practical K8",
           "https://www.educative.io/courses/the-kubernetes-course/x1PMBwNB7zz":"Learn K8",
           "https://www.educative.io/courses/grokking-the-system-design-interview/B8nMkqBWONo":"Grokking systems",
           "https://www.educative.io/courses/grokking-the-machine-learning-interview/JEOBmok417l":"Groking ML",
           "https://www.educative.io/courses/the-way-to-go/N8ZJrXGGEzD":"GO",
           "https://www.educative.io/courses/lean-product-management/m7W7VxXR2p3":"Product Management",
           "https://www.educative.io/courses/grokking-the-coding-interview/RMyv02ylw2q":"Grokking Coding Interview",
           "https://www.educative.io/courses/flask-develop-web-applications-in-python/N72l20MX7vv":"Flask",}

for course in courses:

    driver.get(course)
    time.sleep(5)

    # element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, """//button[@class="contained-primary w-full"]""")))
    # driver.execute_script("arguments[0].click();", element)
    # time.sleep(10)

    count = 0

    os.makedirs(f'./{courses[course]}', exist_ok=True)

    while True:
        try:
            if driver.find_element(By.XPATH, """//button[@class="outlined-primary m-0"]""").is_displayed():
                #take the screenshot
                S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
                driver.set_window_size(S('Width'), S('Height'))  # May need manual adjustment
                driver.find_element(By.TAG_NAME, 'body').screenshot(f"./{courses[course]}/{courses[course]}{str(count)}.png")
                #go to the next page
                driver.find_element(By.XPATH, """//button[@class="outlined-primary m-0"]""").click()
                time.sleep(10)
                count = count + 1
                print("next page clicked")
        except:
            #screenshot last page
            S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
            driver.set_window_size(S('Width'), S('Height'))  # May need manual adjustment
            driver.find_element(By.TAG_NAME, 'body').screenshot(f"./{courses[course]}/{courses[course]}{str(count)}.png")
            print("finishing up")
            break

