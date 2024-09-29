from telethon import TelegramClient
import asyncio
import json

CREDS_FILE = 'Creds.json'

reader = open(CREDS_FILE, 'r')
creds = json.load(reader)

print(creds)

api_id = creds['api_id']
api_hash = creds['api_hash']

print(api_id, api_hash)

client = TelegramClient('testing', api_id, api_hash)

# class 

def filter(message):
    if message.media:
        return False
    
    if 'intern' in message.message.lower():
        return False

    return True

def get_salary(salary_string):
    salary = ""
    for i in range(len(salary_string)):
        if salary_string[i].isdigit() or salary_string[i] == '-':
            salary += salary_string[i]
        if i > 0 and i < len(salary_string)-1 and salary_string[i] == '.' and salary_string[i-1].isdigit() and salary_string[i+1].isdigit():
            salary += salary_string[i]
    return salary

def get_location(location):
    return location.upper().replace('JOB LOCATION:', '').strip()

def get_details(message):
    details = {}
    details['id'] = message.id
    details['time'] = message.date
    details['message'] = message.message
    
    content = message.message.split('\n')
    for item in content:
        if 'iring' in item:
            details['company'] = item.split('Hiring')[0].strip()
        if 'alary' in item:
            details['salary'] = get_salary(item)
        if 'ocation' in item:
            details['location'] = get_location(item)
        if 'http' in item:
            details['apply_link'] = item
    
    return details

async def test():
    await client.start()

    dialogs = await client.get_dialogs()
    
    print(dialogs[13].entity, end="\n\n\n\n\n")

    messages = await client.get_messages(dialogs[13].entity, 10)

    for message in messages:
        print(message, end="\n\n\n")

    # jobs = []

    # for message in messages:
    #     if filter(message):
    #         jobs.append(get_details(message))
    
    # for job in jobs:
    #     print(job)
            
    
asyncio.run(test())
