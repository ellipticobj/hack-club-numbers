import requests

SERVERURL = "http://luna.hackclub.com:8000"

def sendnumber(num):
    print("sending numbers to server...")
    response = requests.post(SERVERURL, json={"number": num})
    
    if response.status_code == 200:
        print("number submitted!")
    else:
        print(f"failed to send numbers: {response.json().get('error')}")

def getnumbers():
    print("fetching numbers from server...")
    response = requests.get(SERVERURL)
    
    if response.status_code == 200:
        numbers = response.json().get('numbers', [])
        return numbers
    else:
        print(f"failed to fetch numbers: {response.json().get('error')}")
        return 0

while True:
    choice = input("1. enter a number\n2. view numbers\n3. exit\n> ")
    
    if choice == "1":
        try:
            number = int(input("input an integer: "))
        except ValueError:
            print("please input an integer")
        
        sendnumber(number)
    
    elif choice == "2":
        getnumbers()
    
    elif choice == "3":
        break
    
    else:
        print("please input 1 2 or 3")