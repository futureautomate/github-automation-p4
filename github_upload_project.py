# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 17:36:06 2020

@author: Tejas
"""

from selenium import webdriver
import time
from logindata import USERNAME,PASSWORD
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome('F:\Channel\webdriver\chromedriver.exe', chrome_options=options)
time.sleep(1)


driver.get('http://www.github.com')
time.sleep(3)

continue_link = driver.find_element_by_link_text('Sign in')
continue_link.click()
time.sleep(3)
if driver.find_element_by_name('login'):
    pass
else:
    time.sleep(2)
    
login = driver.find_element_by_name('login')
password = driver.find_element_by_name("password")
time.sleep(0.5)
    
login.send_keys(USERNAME)
time.sleep(1)
    
password.send_keys(PASSWORD)
time.sleep(1)
    
button = driver.find_element_by_name('commit')
button.click()
time.sleep(2)

'''-------------------------------X-------------------------------'''

new_repository = driver.find_element_by_link_text('New')
new_repository.click()
time.sleep(2)

repository_name = driver.find_element_by_id('repository_name')
repository_name.send_keys('github-automation-p3')
time.sleep(2)

repository_description = driver.find_element_by_id('repository_description')
repository_description.send_keys('GitHub Automation Using Selenium Part 3')
time.sleep(2)

repository_auto_init = driver.find_element_by_id('repository_auto_init')
repository_auto_init.click()
time.sleep(2)   

create_repo_button = driver.find_element_by_css_selector('button.first-in-line')
create_repo_button.click()
time.sleep(2)   

"""-------------------------------------------------X-------------------------------------------------"""

repo_link = driver.find_element_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/ul/li[1]/div/a/span[2]')
repo_link.click()
time.sleep(1)

upload_button = driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div/div[3]/div[2]/a[1]')
upload_button.click()
time.sleep(1)

upload_file = driver.find_element_by_xpath('//*[@id="upload-manifest-files-input"]')
upload_file.send_keys(r'F:\Channel\Code\web automation using selenium and python\github_automation\github_upload_project.py')
time.sleep(5)

commit_upload = driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div/form/button')
commit_upload.click()

"""-------------------------------------------------X-------------------------------------------------"""
count = 1
time.sleep(1)
search_bar_repo_search = driver.find_element_by_xpath('/html/body/div[1]/header/div[3]/div/div/form/label/input[1]')
search_bar_repo_search.send_keys(input("Enter Your Search .... \n"))
search_bar_repo_search.send_keys(Keys.ENTER)

repo_list = driver.find_element_by_xpath('//*[@id="js-pjax-container"]/div/div[3]/div/ul')
item_list = repo_list.find_elements_by_css_selector('a.v-align-middle')
print("List of Repo")
for item in item_list:
    text = item.text
    print("Press {} for {}".format(count, text))
    count = count + 1
opt = int(input("Enter Your Option\n"))
   
item_list[opt-1].send_keys(Keys.ENTER)
count = 0

fork = driver.find_element_by_css_selector('form.btn-with-count')
fork.click()
