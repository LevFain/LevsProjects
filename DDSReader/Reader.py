import DDSDefs as Dds
import ConfigManager as config

dds_topics = ['AtlasFusedEntityReport','EntityPosture', 'AttackReport', 'AttackCommand', 'ScenarioStatus']
dds_connector = Dds.Publisher(dds_topics)

start = ['\nStarting Reader\n','Connecting to topics:\n',str(dds_topics)+'\n','Connected, waiting for Data\n']
for f in start:
	print(f,end='\n')
	config.loading(2)


while True:
	try:
		dds_connector.start()
	except Exception as error:
		print(str(error))
		continue


