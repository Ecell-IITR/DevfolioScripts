from selenium import webdriver
import time as t
from email_trial import get_mail,get_messages_arr,get_message
from b4_t import get_code
from name import generate_indian_name,generate_username



file  = open("emails.txt","a+")
itrator = 0
while itrator<1:
    driver2 = webdriver.Chrome()
    try:
        name = generate_indian_name(1)[0]
        user_name = generate_username(1)

        print("started")
        mail = get_mail(1)[0]
        print(mail)
        
        driver2.get('https://devfolio.co/signup?from=https%3A%2F%2Fproductathon-ai.devfolio.co%2F')

        t.sleep(10)
        inputs = driver2.find_element("tag name",'input')
        inputs.send_keys(mail)
        buttons = driver2.find_elements("tag name",'button')

        for button in buttons:
            if button.text == "Continue":
                button.click()
                t.sleep(4)
                break
        messages = get_messages_arr(mail)
        id = None
        code =None
        for message in messages:
            print(message)
            if message['subject'] == "Verify your email":
                id = message['id']    
                response = get_message(mail,id)
                code = get_code(response['body'])
                
                buttons = driver2.find_elements("tag name",'button')

                print("code is ",code)
                print(buttons)
                for button in buttons:
                    print(button.text)
                    try:
                        if button.text == "Enter code manually":
                            print("tried to click")
                            button.click()      
                            break
                    except:
                        continue
                t.sleep(10)
                break
        print("sucess")
        inputs = driver2.find_elements("tag name",'input')
        it = 0 
        print(inputs)
        for input in inputs:
            aria = str(input.get_attribute("aria-label"))
            print(aria,it)
            if aria.find("Please enter OTP character") !=-1 :
                input.send_keys(code[it])
                it+=1
        t.sleep(5)
        buttons = driver2.find_elements("tag name",'button')

        for button in buttons:
            if button.text == "Continue":
                button.click()
                
                break
        t.sleep(4)

        whl=driver2.window_handles
        driver2.switch_to.window(whl[1])
        t.sleep(4)
        inputs = driver2.find_elements("tag name",'input')

        for input in inputs:
            try:
                atr = str(input.get_attribute("id"))
                print(atr)
                if atr == "first_name":
                    input.send_keys(name[0])
                if atr == "last_name":
                    input.send_keys(name[1])
                if atr == "username":
                    input.send_keys(user_name[0])
                if atr == "password":
                    input.send_keys("sds@124CHECK")
            except:
                continue
        print("inputs done")
        t.sleep(4)
        buttons = driver2.find_elements("tag name",'button')
        for button in buttons:
            if button.text == "Continue":
                button.click()

                
        t.sleep(2)
        
        whl=driver2.window_handles    
        driver2.switch_to.window(whl[0])  
        t.sleep(16)
        print('Apply now')

        buttons = driver2.find_elements("tag name",'button')
        for button in buttons:
            if button.text == "Apply now":
                button.click()
                
                
                break

        # driver2.switch_to.window(whl[0])   
        t.sleep(8)

        buttons = driver2.find_elements("tag name",'button')
        for button in buttons:
            if button.text == "Continue to the application":
                button.click()
                
                
                break
        t.sleep(8)

        text = driver2.find_element("tag name",'textarea')


        text.send_keys("I am very excited to participate in this hackathon")
        buttons = driver2.find_elements("tag name",'button')
        for button in buttons:
            stri = str(button.text)
            if "Next" in stri:
                button.click()
                
                break
        t.sleep(4)
        inputs = driver2.find_elements("tag name",'input')
        for input in inputs:
            try:
                atr = str(input.get_attribute("name"))
                if atr == "hasNoFormalEducation":
                    input.click()
                    t.sleep(4)
                    break
            except:
                continue
        buttons = driver2.find_elements("tag name",'button')
        for button in buttons:
            stri = str(button.text)
            if "Next" in stri:
                button.click()
                
                break
        inputs = driver2.find_elements("tag name",'input')
        for input in inputs:
            try:
                atr = str(input.get_attribute("value"))
                if atr == "Frontend Developer":
                    input.click()
                    t.sleep(4)
                    break
            except:
                continue
        buttons = driver2.find_elements("tag name",'button')
        for button in buttons:
            stri = str(button.get_attribute("class"))
            if "suggestion-list" in stri:
                button.click()
                
                break
        buttons = driver2.find_elements("tag name",'button')
        for button in buttons:
            stri = str(button.text)
            if "Next" in stri:
                button.click()
                
                break
        for button in buttons:
            stri = str(button.text)
            if "Submit" in stri:
                button.click()
                
                break
        itrator+=1
        file.write(mail+"\n")
    except Exception as e:
        print(e)
        
        pass
    


