import requests
from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd
import urllib

# get session
ses = requests.Session()

login_url = "http://www.msftconnecttest.com/redirect"
username = "liu_zihao_1@students.edu.sg"
pwd = "Lzh_54894426"

username = username.upper()

print(f"{datetime.now()}: Trying to login...")
response = requests.get(login_url)
soup = BeautifulSoup(response.text, 'html.parser')
script_tag = soup.find('script')

if script_tag is not None:
    redirect_url = script_tag.string.strip().split('"')[1]
    print(f"{datetime.now()}: Redirected to {redirect_url}")
    response = requests.get(redirect_url)   
    print(response.text)

    payload = {
        'username': username,
        'password': pwd,
        'submit': "Continue"
    }

    requests.post(redirect_url, data = payload)



# form = html.find_element_by_xpath(modules.xpath.attribute_value("id", "login-form"))
# print(form)
# data = form.extract_form_datas()
# # print(data)
# data["AdminLoginForm[username]"] = username
# data["AdminLoginForm[password]"] = pwd
# response = ses.post(login_url, data=data)
# print(f"Returned status code: {response.status_code}")
# print(f"{datetime.now()}: Login success.")

# if 'Welcome' in response.content.decode():
#     print("1")
# else:
#     print("0")