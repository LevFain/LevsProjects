import json
from os import path as os_path


def start():
    val = input("What would you like to change? (Command/IP/Port)\n")
    if val == "IP" or val == "ip":
        ipChange()
    if val == "Port" or val == "port":
        portChange()
    if val == "Command" or val == "command":
        commandChange()

def ipChange():
    Server = input("For which Server would you like to change? (1-6)\n")
    if Server == "1":
        with open('./Configs/Config.json', 'r+') as f:
            data = json.load(f)
            print("Current IP: " + data['Server1']['IP'])
            data['Server1']['IP'] = input("New IP: ")
            f.seek(0)
            json.dump(data, f, indent=5)
            f.close()
            print('IP Changed')
            more = input('Anything else to change? (Y/N)\n')
            if more == "Y" or more == "y":
                start()
            else:
                exit
    if Server == "2":
        with open('./Configs/Config.json', 'r+') as f:
            data = json.load(f)
            print("Current IP: " + data['Server2']['IP'])
            data['Server2']['IP'] = input("New IP: ")
            f.seek(0)
            json.dump(data, f, indent=5)
            f.close()
            print('IP Changed')
            more = input('Anything else to change? (Y/N)\n')
            if more == "Y" or more == "y":
                start()
            else:
                exit
    if Server == "3":
        with open('./Configs/Config.json', 'r+') as f:
            data = json.load(f)
            print("Current IP: " + data['Server3']['IP'])
            data['Server3']['IP'] = input("New IP: ")
            f.seek(0)
            json.dump(data, f, indent=5)
            f.close()
            print('IP Changed')
            more = input('Anything else to change? (Y/N)\n')
            if more == "Y" or more == "y":
                start()
            else:
                exit
    if Server == "4":
        with open('./Configs/Config.json', 'r+') as f:
            data = json.load(f)
            print("Current IP: " + data['Server4']['IP'])
            data['Server4']['IP'] = input("New IP: ")
            f.seek(0)
            json.dump(data, f, indent=5)
            f.close()
            print('IP Changed')
            more = input('Anything else to change? (Y/N)\n')
            if more == "Y" or more == "y":
                start()
            else:
                exit
    if Server == "5":
        with open('./Configs/Config.json', 'r+') as f:
            data = json.load(f)
            print("Current IP: " + data['Server5']['IP'])
            data['Server5']['IP'] = input("New IP: ")
            f.seek(0)
            json.dump(data, f, indent=5)
            f.close()
            print('IP Changed')
            more = input('Anything else to change? (Y/N)\n')
            if more == "Y" or more == "y":
                start()
            else:
                exit
    if Server == "6":
        with open('./Configs/Config.json', 'r+') as f:
            data = json.load(f)
            print("Current IP: " + data['Server6']['IP'])
            data['Server6']['IP'] = input("New IP: ")
            f.seek(0)
            json.dump(data, f, indent=5)
            f.close()
            print('IP Changed')
            more = input('Anything else to change? (Y/N)\n')
            if more == "Y" or more == "y":
                start()
            else:
                exit
            
def portChange():
    Server = input("For which Server would you like to change? (1-6)\n")
    if Server == "1":
        with open('./Configs/Config.json', 'r+') as f:
            data = json.load(f)
            print("Current PORT: " + data['Server1']['PORT'])
            data['Server1']['PORT'] = input("New PORT: ")
            f.seek(0)
            json.dump(data, f, indent=5)
            f.close()
            print('PORT Changed')
            more = input('Anything else to change? (Y/N)\n')
            if more == "Y" or more == "y":
                start()
            else:
                exit
    if Server == "2":
        with open('./Configs/Config.json', 'r+') as f:
            data = json.load(f)
            print("Current PORT: " + data['Server2']['PORT'])
            data['Server2']['PORT'] = input("New PORT: ")
            f.seek(0)
            json.dump(data, f, indent=5)
            f.close()
            print('PORT Changed')
            more = input('Anything else to change? (Y/N)\n')
            if more == "Y" or more == "y":
                start()
            else:
                exit
    if Server == "3":
        with open('./Configs/Config.json', 'r+') as f:
            data = json.load(f)
            print("Current PORT: " + data['Server3']['PORT'])
            data['Server3']['PORT'] = input("New PORT: ")
            f.seek(0)
            json.dump(data, f, indent=5)
            f.close()
            print('PORT Changed')
            more = input('Anything else to change? (Y/N)\n')
            if more == "Y" or more == "y":
                start()
            else:
                exit
    if Server == "4":
        with open('./Configs/Config.json', 'r+') as f:
            data = json.load(f)
            print("Current PORT: " + data['Server4']['PORT'])
            data['Server4']['PORT'] = input("New PORT: ")
            f.seek(0)
            json.dump(data, f, indent=5)
            f.close()
            print('PORT Changed')
            more = input('Anything else to change? (Y/N)\n')
            if more == "Y" or more == "y":
                start()
            else:
                exit
    if Server == "5":
        with open('./Configs/Config.json', 'r+') as f:
            data = json.load(f)
            print("Current PORT: " + data['Server5']['PORT'])
            data['Server5']['PORT'] = input("New PORT: ")
            f.seek(0)
            json.dump(data, f, indent=5)
            f.close()
            print('PORT Changed')
            more = input('Anything else to change? (Y/N)\n')
            if more == "Y" or more == "y":
                start()
            else:
                exit
    if Server == "6":
        with open('./Configs/Config.json', 'r+') as f:
            data = json.load(f)
            print("Current PORT: " + data['Server6']['PORT'])
            data['Server6']['PORT'] = input("New PORT: ")
            f.seek(0)
            json.dump(data, f, indent=5)
            f.close()
            print('PORT Changed')
            more = input('Anything else to change? (Y/N)\n')
            if more == "Y" or more == "y":
                start()
            else:
                exit

def commandChange():
    Server = input("For which Server would you like to change? (1-6)\n")
    if Server == "1":
        with open('./Configs/Config.json', 'r+') as f:
            data = json.load(f)
            print("Current Command: " + data['Server1']['Command'])
            data['Server1']['Command'] = input("New Linked Command: ")
            f.seek(0)
            json.dump(data, f, indent=5)
            f.close()
            print('Linked Command Changed')
            more = input('Anything else to change? (Y/N)\n')
            if more == "Y" or more == "y":
                start()
            else:
                exit
    if Server == "2":
        with open('./Configs/Config.json', 'r+') as f:
            data = json.load(f)
            print("Current Command: " + data['Server2']['Command'])
            data['Server2']['Command'] = input("New Linked Command: ")
            f.seek(0)
            json.dump(data, f, indent=5)
            print('Linked Command Changed')
            f.close()
            more = input('Anything else to change? (Y/N)\n')
            if more == "Y" or more == "y":
                start()
            else:
                exit
    if Server == "3":
        with open('./Configs/Config.json', 'r+') as f:
            data = json.load(f)
            print("Current Command: " + data['Server3']['Command'])
            data['Server3']['Command'] = input("New Linked Command: ")
            f.seek(0)
            json.dump(data, f, indent=5)
            print('Linked Command Changed')
            f.close()
            more = input('Anything else to change? (Y/N)\n')
            if more == "Y" or more == "y":
                start()
            else:
                exit
    if Server == "4":
        with open('./Configs/Config.json', 'r+') as f:
            data = json.load(f)
            print("Current Command: " + data['Server4']['Command'])
            data['Server4']['Command'] = input("New Linked Command: ")
            f.seek(0)
            json.dump(data, f, indent=5)
            print('Linked Command Changed')
            f.close()
            more = input('Anything else to change? (Y/N)\n')
            if more == "Y" or more == "y":
                start()
            else:
                exit
    if Server == "5":
        with open('./Configs/Config.json', 'r+') as f:
            data = json.load(f)
            print("Current Command: " + data['Server5']['Command'])
            data['Server5']['Command'] = input("New Linked Command: ")
            f.seek(0)
            json.dump(data, f, indent=5)
            f.close()
            print('Linked Command Changed')
            more = input('Anything else to change? (Y/N)\n')
            if more == "Y" or more == "y":
                start()
            else:
                exit
    if Server == "6":
        with open('./Configs/Config.json', 'r+') as f:
            data = json.load(f)
            print("Current Command: " + data['Server6']['Command'])
            data['Server6']['Command'] = input("New Linked Command: ")
            f.seek(0)
            json.dump(data, f, indent=2)
            print('Linked Command Changed')
            f.close()
            more = input('Anything else to change? (Y/N)\n')
            if more == "Y" or more == "y":
                start()
            else:
                exit
                
start()

