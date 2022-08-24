import logging
import DDSDefs as Dds


logger = logging.getLogger('main')
dds_topics = ['AtlasFusedEntityReport','EntityPosture', 'AttackReport', 'AttackCommand', 'ScenarioStatus']
dds_connector = Dds.Publisher(dds_topics)


print('Version 1.0.2 - 15/08/22')
print('Starting Application')
print('Connecting to ' + str(dds_topics))
print('Connected, waiting for Scenario Play')


while True:
	try:
		dds_connector.start()
	except Exception as error:
		print(str(error))
		continue


