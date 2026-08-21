addition = int(input('What is 2 + 2 equal? '))

binary_addition = bin(addition)

if addition == 4:
    print(f'Shows answer in binary: {binary_addition}')
else:
    print("Restart and Try again.")


color_of_sky = True

user_input = input("Is the color of the sky blue, True or False? ")

if user_input == str(color_of_sky):
    print("Correct")
else:
    print("Restart and try again.")

print()

print("This purely experimental, your computer will move slower than usually because of deliberate pauses in the code")
print()
import time
import json

time.sleep(2.4)

agents = [
        {"name": "Intuit", "role": "Payroll Specialist", "status": True },
        {"name": "Quic", "role": "Benefit Specialist", "status": True},
        {"name": "Booksy", "role": "Bookkeeping Specialist", "status": False}
        ]


name = "Light Yagami"
username = "l_yagami"
password = "*********"

print(f'Hello, {name}, You are a AI Technician with a non-profit organization in New York.\nIt is your first day and the VP of Payroll & Accounting is having issues with her agent.\nCan you stop by her office when you arrive she made it seem urgent.Her name is Misa Amane\nThanks in advance\n-AI Tech Lead-Ryuk\n')
print()
time.sleep(2.5)
print("Arrives at her office and knocks on the door")
print()
time.sleep(1)
print("Knock")
time.sleep(1)
print("Knock")
time.sleep(1)
print("knoc...")
print("Misa: Come in and hello,...")

time.sleep(2)

print(f'My name is {name}')
print()
time.sleep(1.5)

print(f'Misa: Yes, {name} great to have you on the team. I am Misa Amane, VP of Payroll & Accounting.\nThe issue is that we had AI update our staff members bonuses this year and housekeeping is making more \nthan the CEO because of long nights and weekends. Can you update the AI program?')

print()
print("Light: Sure, Misa. Happy to help. (Misa leaves) \nLets take a look at this program")
print()

print("...")
time.sleep(1)
print("Light: Trash but what can you expect from an organization that prides itself on not making a profit.")
print()
time.sleep(1.2)

print(f'Quickbooks 2024 Non-profit \nUsername\n{username}\nPassword\n{password}')
print()
time.sleep(1.2)
print(f'Welcome to Quickbooks, {name}. I am Intuit, your fully customizable AI assistant. How can I help you today?')
print()
time.sleep(1)
print("...close, you are the reason I am here in the first place.")
print()
time.sleep(1.2)
print("clicking...")
time.sleep(1.2)
print("Program...")
time.sleep(1)
print("AI...")
time.sleep(1)
print("Agents...")
time.sleep(1.5)
print(json.dumps(agents, indent= 2))
print()
time.sleep(1.5)
print("Light: I need to change the status of Intuit to false before I can update the properties")
print("for agent in agents:\n if agent['name'] == Intuit:\n     agent['status'] = 'False'")
time.sleep(1.5)
for agent in agents:
    if agent['name'] == "Intuit":
        agent['status'] = False

time.sleep(.5)
print(json.dumps(agents[0], indent= 2))
print()
print("right click, view Properties")
print()
time.sleep(2)

def print_border(message, char="*"):
    border_line = char * (len(message) + 6)
    
    print(border_line)
    print(f"{char}  {message}  {char}")
    print(border_line)

print_border("Intuit: Properties")
print(f'username = [{{"fname": "Light", "permission": "Technician"}}, {{"fname": "Ryuk", "permission": "Admin"}},]')
print("def welcome(username):\n     for user in username:  \n       if user.fname == 'Light' \n        print(f'Welcome to Quickbooks, {{fname}}. I am Intuit, your fully customizable AI assistant. How can I help you today?')\n       elif user.fname == 'Ryuk' \n        print(f'Welcome to Quickbooks, {{name}}. I am Intuit, your fully customizable AI assistant. How can I help you today?')\n else:\n \'Please complete your user profile\'.")
print()
print('user_permissions = [{{"read": "4", "write": "2", "execute": 1}}]')
print()
time.sleep(1.2)
print("Light: There is the problem. I just have to adjust the permissions. Also, why is there source code in the properties section. I don\'t have time for this")
time.sleep(1.2)
print("Program...")
time.sleep(1)
print("AI...")
time.sleep(1)
print("Agents...")
time.sleep(1)
print("Intuit...")
time.sleep(1)
print("Permissions...")
time.sleep(1)
print("Payroll...")
print(bin(4+2+1))
print("Lets remove the write permission")
print(bin(4+0+1))
print("Update")
time.sleep(1.5)
print("Updating...")
time.sleep(2)
print("Changes have applied, successfully.")
print("Light: Cannot\'t forget to turn Intuit\'s status back on ")
print('for agent in agents: \n     if agent["name"] == "Intuit": \n          agent["status"] = True')
for agent in agents:
    if agent['name'] == "Intuit":
        agent['status'] = True

time.sleep(.5)
print(json.dumps(agents[0], indent= 2))
