import json

with open('./Configs/Config.json', 'r') as configFile:
    config_data = json.load(configFile)

server1 = config_data['server1']
server2 = config_data['server2']
server3 = config_data['server3']
server4 = config_data['server4']
server5 = config_data['server5']
server6 = config_data['server6']
# port_list = config_data['PORTS']
# print(ip_list[0]['Server1'])
# print(port_list)

print('Current List of servers to send info via UDP')
print(" Server ID |  Server IP  |  Server Port  | Linked Command"
    '\n', "Server 1 ","| ",server1['IP']," |    ", int(server1['PORT']),"     | ", server1['Command'],
    '\n', "Server 2 ","| ",server2['IP']," |    ", int(server2['PORT']),"     | ", server2['Command'],
    '\n', "Server 3 ","| ",server3['IP']," |    ", int(server3['PORT']),"     | ", server3['Command'],
    '\n', "Server 4 ","| ",server4['IP']," |    ", int(server4['PORT']),"     | ", server4['Command'],
    '\n', "Server 5 ","| ",server5['IP']," |    ", int(server5['PORT']),"     | ", server5['Command'],
    '\n', "Server 6 ","| ",server6['IP']," |    ", int(server6['PORT']),"     | ", server6['Command']
    )

