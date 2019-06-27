from django.shortcuts import render, HttpResponse, redirect
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import os, json, getpass, time

chrome_options = Options()
chrome_options.add_argument('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
chrome_options.add_argument("--kiosk")


def index(req):
    return render(req, 'index.html')

def amazon(req):
    user = req.POST['user']
    password = req.POST['pword']

    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.implicitly_wait(100)
    browser.get('https://www.amazon.com')

    browser.find_element_by_link_text('Sign in').click()
    time.sleep(1)

    elem = browser.find_element_by_id('ap_email')
    elem.send_keys(user)
    elem = browser.find_element_by_id('ap_password')
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)
    time.sleep(10)

    browser.quit()
    return redirect('/')

def mernInstance(req):
    user = req.POST['user']
    password = req.POST['pword']
    instance = req.POST['instanceName']

    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.implicitly_wait(100)
    time.sleep(2)
    browser.get('https://aws.amazon.com/')
    time.sleep(1)

    browser.find_element_by_link_text('Create an AWS Account').click()
    time.sleep(1)
    browser.find_element_by_link_text('Sign in to an existing AWS account').click()

    elem = browser.find_element_by_id('resolving_input')
    elem.send_keys(user)
    elem.send_keys(Keys.RETURN)
    elem = browser.find_element_by_id('password')
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)
    time.sleep(1)

    browser.find_element_by_link_text('Services').click()
    browser.find_element_by_link_text('EC2').click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="gwt-debug-createInstanceView"]/div/div[2]/div[2]/div/table/tbody/tr/td[1]/div/button').click()
    elem = browser.find_element_by_id('gwt-debug-searchTextBox')
    elem.send_keys('ubuntu')
    time.sleep(1)
    elem.send_keys(Keys.RETURN)
    browser.find_element_by_xpath('//*[@id="gwt-uid-2712:selectButton"]').click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="gwt-debug-gotoNextPage-button"]').click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="gwt-debug-gotoNextPage-button"]').click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="gwt-debug-gotoNextPage-button"]').click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="gwt-debug-gotoNextPage-button"]').click()
    time.sleep(2) 
    elem = browser.find_element_by_link_text('Add Rule')
    time.sleep(1)
    elem.click()
    # browser.find_element_by_link_text('HTTP').click()
    # time.sleep(1)






    time.sleep(10)
    # browser.quit()
    return redirect('/')
