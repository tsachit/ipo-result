import json
import requests
import sys
from bs4 import BeautifulSoup
import pandas as pd

def fetchContent():
    try:
        response = requests.get('https://iporesult.cdsc.com.np/result/companyShares/fileUploaded')
        parsed_response = json.loads(response.text)
        return parsed_response['body']
    except:
        return []

def checkResult(id, boid):
    try:
        url = "https://iporesult.cdsc.com.np/result/result/check"
        headers = {
            'Content-Type': 'application/json'
        }
        payload = json.dumps({
            "companyShareId": id,
            "boid": boid
        })

        response = requests.request("POST", url, headers=headers, data=payload)
        if(response.status_code == 200):
            parsed_response = json.loads(response.text)
            return parsed_response['message']
        return 'Invalid request, please try again later. Thanks'
    except:
        return 'Invalid request, please try again later. Thanks'


def getID():
    try:
        id = int(input("Enter the id you want to check the IPO: "))
        if id <= 0:
            print('Invalid number inserted. Retrying...')
            return getID()
        return id
    except ValueError:
        print('String inserted, insert number only. Retrying...')
        return getID()


def getBOID():
    try:
        if(len(sys.argv) > 1):
            return int(sys.argv[1])

        return int(input("Enter your BOID number: "))
    except ValueError:
        print('String inserted, insert number only. Retrying...')
        return getBOID()

print('You can also provide BOID directly after main.py to avoid extra step')
print('Example: python main.py 1234567890123456\n')

result = fetchContent()
if(len(result)):
    df = pd.DataFrame(result)

    print('===========================LIST OF AVAILABLE COMPANIES===========================\n')
    print(df.to_string(index=False))
    print('=================================================================================\n')

    id = getID()
    name = df[df.id == id].name.tolist()[0]
    boid = getBOID()

    print(f"\nChecking for Company: {name} and BOID: {boid}\n")

    print(checkResult(id, boid))
else:
    print('Server busy, please try again later. Thanks')