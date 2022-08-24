import os
import rticonnextdds_connector as rti
import json
import socket
from time import sleep
from os import path as os_path
import ConfigManager

# this setting is needed for more than 15 connectors in application
rti.Connector.set_max_objects_per_thread(4096)


dds_topics =  { 'AtlasFusedEntityReport': {'channel': 'Subscriber::EntityReport_DR', 'dir': 'input'}, 
                'ScenarioStatus': {'channel': 'Subscriber::ScenarioStatus_DR', 'dir': 'input'}, 
                'EntityPosture': {'channel': 'Subscriber::EntityPosture_DR', 'dir': 'input'}, 
                'FusionReport': {'channel': 'Subscriber::FusionReport_DR', 'dir': 'input'}, 
                'AttackReport': {'channel': 'Subscriber::AttackReport_DR', 'dir': 'input'}, 
                'AttackCommand_DR': {'channel': 'Subscriber::AttackCommand_DR', 'dir': 'input'}, 
                }

file_path = os_path.dirname(os_path.realpath(__file__))

def get_connector_with_name(participant_name: str):
    return rti.Connector(
    config_name="Reader_Participant_Library::"+participant_name,
    url=file_path + "./Configs/DDS_Participant_Config.xml",
)




class Publisher(object):
    def __init__(self, logger=None, override_dds_topics=None, entity_connector=None, attack_connector=None):
        if not attack_connector:
            self.attack_connector = get_connector_with_name("Attack_Participant")
        else:
            self.attack_connector = attack_connector

        if not entity_connector:
            self.entity_connector = get_connector_with_name("Entity_Participant")
        else:
            self.entity_connector = entity_connector
        self.logger = logger
        self.channels = dict({})
        self.seq_num = dict({})
        if override_dds_topics:
            self.dds_topics = override_dds_topics
        else:
            self.dds_topics = dds_topics

    def GetScenarioStatus(self):
        try:
            dr = self.entity_connector.get_input("Subscriber::ScenarioStatus_DR")
        except:
            print("reader ScenarioStatus_DR dont exist")
        
        dr.take()
        curr_status = None
        for sample in dr.samples:
            curr_status = sample.get_dictionary()
        if not curr_status:
            return {}
        getKeys = curr_status['engine_status']
        for thevalue in str(getKeys):
            # print(thevalue)
            while thevalue == "1":
                # print('Scenario Running')
                self.start()
            while thevalue == "2":
                # print('Scenario Paused')
                self.GetScenarioStatus()
            while thevalue == "3":
                # print('Scenario Rewinding')
                self.GetScenarioStatus()
            while thevalue == None:
                # print('No Scenario')
                self.GetScenarioStatus()

    def GetAttackCommand(self):
        try:
            dr = self.attack_connector.get_input("Subscriber::AttackCommand_DR")
        except:
            print("reader AttackCommand_DR dont exist")
        
        dr.take()
        curr_message = []
        for sample in dr.samples:
            curr_message.append(sample.get_dictionary())
        if not curr_message:
            return {}
        command = {
                    'AttackCommand':
                        {
                            'EntityName':curr_message[0]['attacking_entity_name'],
                            'WeaponName':curr_message[0]['weapon_name'],
                            'AttackLocation':curr_message[0]['attack_location']
                    }
                }
        jcommand = json.dumps(command, indent=2)
        print(jcommand)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        sock.sendto(bytes(jcommand, "utf-8"), (ConfigManager.server1['IP'], int(ConfigManager.server1['PORT'])))


    def GetEntityPosture(self):
        try:
            dr = self.entity_connector.get_input("Subscriber::EntityPosture_DR")
        except:
            print("reader EntityPosture_DR dont exist")
        
        dr.take()
        curr_message = []
        for sample in dr.samples:
            curr_message.append(sample.get_dictionary())
        if not curr_message:
            return {}
        command = {
                    'EntityPosture':
                        { 
                        'EntityName':curr_message[0]['entity_name'],
                        'Posture':curr_message[0]['posture']['PostureEnum']
                }
            }
        jcommand = json.dumps(command, indent=2)
        print(jcommand)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        sock.sendto(bytes(jcommand, "utf-8"), (ConfigManager.server2['IP'], int(ConfigManager.server2['PORT'])))

    def GetAtlasReport(self):
        try:
            dr = self.entity_connector.get_input("Subscriber::EntityReport_DR")
        except:
            print("reader EntityReport_DR dont exist")
        
        dr.take()
        curr_message = []
        for sample in dr.samples:
            curr_message.append(sample.get_dictionary())
        if not curr_message:
            return {}
        report = {
                    'AtlasFusedEntityReport':
                        { 
                        'EntityName':curr_message[0]['unitName'],
                        'Enumaration':curr_message[0]['unitEnumaration'],
                        'WeaponStatus':curr_message[0]['weaponStatus'],
                        'Hostility':curr_message[0]['hostility'],
                        'Attitude':curr_message[0]['attitude'],
                        'DamageState':curr_message[0]['entityDamageState'],
                        'TimeStamp':curr_message[0]['timestamp'],
                        'Classification':curr_message[0]['classification'],
                        'Velocity':curr_message[0]['velocity']['ENUVelocityVector'],
                        'Posture':curr_message[0]['posture'],
                        'Location':curr_message[0]['worldLocation']
                    }
                }
        jreport = json.dumps(report, indent=2)
        print(jreport)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        sock.sendto(bytes(jreport, "utf-8"), (ConfigManager.server3['IP'], int(ConfigManager.server3['PORT'])))

    def GetAttackReport(self):
        try:
            dr = self.attack_connector.get_input("Subscriber::AttackReport_DR")
        except:
            print("reader AttackReport_DR dont exist")
        
        dr.take()
        curr_message = []
        for sample in dr.samples:
            curr_message.append(sample.get_dictionary())
        if not curr_message:
            return {}
        report = {
                    'AttackReport':
                        {
                            'AttackerName':curr_message[0]['attacking_entity_name'],
                            'WhosUnderAttack':curr_message[0]['entity_under_attack_name'],
                            'WeaponName':curr_message[0]['weaponType'],
                            'AttackLocation':curr_message[0]['attack_location']
                        }
                    }
        jreport = json.dumps(report, indent=2)
        print(jreport)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        sock.sendto(bytes(jreport, "utf-8"), (ConfigManager.server4['IP'], int(ConfigManager.server4['PORT'])))

    def start(self):
        # self.GetScenarioStatus()
        self.GetAttackReport()
        self.GetAtlasReport()
        self.GetAttackCommand()
        self.GetEntityPosture()

