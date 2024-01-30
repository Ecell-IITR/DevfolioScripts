import requests
import json
# import pandas as pd
def get_mail(num):
    if num>500:
        return "Limit Exceeded"
    response = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count="+str(num))
    mail = json.loads(response.text)
    return mail
def get_messages_arr(mail):
    arr = []
    mail = mail.split('@')
    while len(arr)==0:
        response = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={mail[0]}&domain={mail[1]}")
        messages = json.loads(response.text)
        arr = messages
    # response = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={mail[0]}&domain={mail[1]}")
    # messages = json.loads(response.text)
    return arr
def get_message(mail,id):
    mail = mail.split('@')
    response = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={mail[0]}&domain={mail[1]}&id={id}")
    message = json.loads(response.text)
    return message
print(get_messages_arr("3fy9gu3mmb@laafd.com"))
# print(get_message("rdrgsr9h@vjuum.com",928360623))
