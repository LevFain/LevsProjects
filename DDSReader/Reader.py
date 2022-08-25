import DDSDefs as Dds
import ConfigManager as config

dds_topics = ['AtlasFusedEntityReport','EntityPosture', 'AttackReport', 'AttackCommand', 'ScenarioStatus']
dds_connector = Dds.Publisher(dds_topics)

print('\nStarting Reader\n')
config.loading()
config.loading()
print('Connecting to topics:\n')
print(str(dds_topics)+'\n')
config.loading()
config.loading()
print('Connected, waiting for Data Reports')

while True:
	config.loading()
	try:
		dds_connector.start()
	except Exception as error:
		print(str(error))
		continue


