import requests

SERVERURL = "http://luna.hackclub.com"

def sendnumber(num):
    response = requests.post(SERVERURL, json={"number": num})
    
    if response.status_code == 200:
        print("Number submitted!")
    else:
        print(f"Failed to send numbers: {response.json().get('error')}")

def getnumber():
    response = requests.get(SERVERURL)
    
    if response.status_code == 200:
        numbers = response.json().get('numbers', [])
        print(f"Numbers: {numbers}")
    else:
        print(f"Failed to fetch numbers: {response.json().get('error')}")
