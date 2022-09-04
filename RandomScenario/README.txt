This program:
	-Selects a random scenario from the scnx sub folder in files.
	-Overwrites the scenario.bat with the new randomly selected scenario.
	-Makes sure that the selected scenario is present in the %MAK_VRFDIR%/userData/scenarios folder.
	-Starts the scenario.bat.
	-Allows you to change DomainID in the scenario BAT.
	-Allows you to create a NEW scenario.bat with the selected scenario
	
Important:
	-Make sure that your %MAK_VRFDIR%, is pathed to the currently used VRF and to the most updated one.
	-If you want to change a DomainID, do it before starting the main program.
		as the main program first takes the original scenario.bat and uses it,
		and the domain change occurs on it.
	-Creating a new .bat will simply copy the scenario.bat and paste it along with all the usual things it does,
		it also changes the name to the scenario name.


How to use:
	1) Place any scenario file you want in the scnx folder
	2) start "start.bat"
	3) type 'start' or 'change' or 'create'
		-start; starts the main program (randomaly selectes a scenario and start scenario.bat with it)
		-change; lets you change the DomainID of the BAT
		-create; lets you create a new .bat with the selected scenario (can be a random scenario or a single one)


Comes with a few random scenarios I chose for testings...
