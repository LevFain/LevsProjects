import json
import os
import sys
from time import sleep
from tabulate import tabulate


print('\n')
print('                   Version 1.0.8 - 24/08/22                   '+'\n')
print('                       Starting Config                        '+'\n')

# this checks if the necessary modules are installed, if not, installs them
modules=['tabulate','rticonnextdds_connector'] # modules to check
for module in modules:
    if module in sys.modules:
        continue
    else:
        os.system("pip install "+module) # installs modules that are not present 

with open('./Configs/Config.json', 'r') as configFile:
    config_data = json.load(configFile)

Server1 = config_data['Server1']
Server2 = config_data['Server2']
Server3 = config_data['Server3']
Server4 = config_data['Server4']
Server5 = config_data['Server5']
Server6 = config_data['Server6']


def loading():
    # ← ↖ ↑ ↗ → ↘ ↓ ↙
    print("↑", end="\r")
    sleep(0.05)
    print("↗", end="\r")
    sleep(0.05)
    print("→", end="\r")
    sleep(0.05)
    print("↘", end="\r")
    sleep(0.05)
    print("↓", end="\r")
    sleep(0.05)
    print("↙", end="\r")
    sleep(0.05)
    print("←", end="\r")
    sleep(0.05)
    print("↖", end="\r")
    sleep(0.05)
    print("↑", end="\r")


loading()
loading()
print('                   Current list of servers                        '+'\n')
print(tabulate([['Server 1', Server1['IP'],Server1['PORT'],Server1['Command']],
                ['Server 2', Server2['IP'],Server2['PORT'],Server2['Command']],
                ['Server 3', Server3['IP'],Server3['PORT'],Server3['Command']],
                ['Server 4', Server4['IP'],Server4['PORT'],Server4['Command']],
                ['Server 5', Server5['IP'],Server5['PORT'],Server5['Command']],
                ['Server 6', Server6['IP'],Server6['PORT'],Server6['Command']]],
                headers = ['Server ID','Server IP','Server Port','Linked Command'],
                tablefmt="pretty",
                stralign="center",
                numalign="center"))
