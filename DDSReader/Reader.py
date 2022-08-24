import DDSDefs as Dds
import ConfigManager as config

dds_topics = ['AtlasFusedEntityReport','EntityPosture', 'AttackReport', 'AttackCommand', 'ScenarioStatus']
dds_connector = Dds.Publisher(dds_topics)

print('Connecting to topics:\n')
print(str(dds_topics)+'\n')
config.loading()
print('Connected, waiting for Scenario Play')

while True:
	try:
		dds_connector.start()
	except Exception as error:
		print(str(error))
		continue


