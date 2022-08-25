import os
import sys
import json
from time import sleep

def loading(num):
    for i in range(num):
        if i <= i:
            # arrows = ['←', '↖', '↑', '↗', '→', '↘', '↓', '↙']
            arrows = ['[----]','[=---]','[-=--]','[--=-]','[---=]','[----]','      ']
            for arrow in arrows:
                print("                            "+arrow,end='\r')
                sleep(0.05)

if not 'tabulate' or not 'rticonnextdds_connector' in sys.modules.keys():
    os.system('pip install tabulate -q -q -q')
    os.system('pip install rticonnextdds_connector -q -q -q')# installs modules that are not present 

from tabulate import tabulate



print('\n                   Version 1.0.9 - 25/08/22                   '+'\n')
print('                       Starting Config                        '+'\n')
loading(2)

# this checks if the necessary modules are installed, if not, installs the

with open('./Configs/Config.json', 'r') as configFile:
    config_data = json.load(configFile)

Server1 = config_data['Server1']
Server2 = config_data['Server2']
Server3 = config_data['Server3']
Server4 = config_data['Server4']
Server5 = config_data['Server5']
Server6 = config_data['Server6']


print('                   Current list of servers                        '+'\n')
loading(2)
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
