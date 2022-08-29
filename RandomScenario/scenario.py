import os, random, shutil

def init():
        
        # scenarios folder location and bat name
        scen_dir = os.path.abspath("./scenarios")
        scen = "/scenario.bat"
        print(scen_dir)  
                
        # scnx files location
        for root, dirs, files in os.walk('./scenarios/scnx'):
            flen = len(files) -1
        
        if flen >= 1:    
            # random number from 0 (as indexs start from 0) till (including) the amount of files
            # in the files directory
            rndnum = str(random.randint(0,flen))
            
            # random scenario chosing
            rndScn = files[int(rndnum)]

            # making sure the selected scenario
            # is existent in the main scenarios folder
            # of VRF            
            src = './scenarios/scnx/'+str(rndScn)
            dst = str(os.getenv('mak_vrfdir'))+'/userData/scenarios/'
            shutil.copy2(src, dst)
            
            # read our VRF SIM BAT
            with open('./scenarios/scenario.bat', 'r') as file:
                # read a list of lines into data
                data = file.readlines()

            # print our current file that is goign to be used and the new one
            print("\nYour current ScenarioFile: "+ data[39])
            print('New Scenario will be: '+ rndScn + "\n")
            
            # change the SCENARIO_FILE to the randomly chosen one
            data[39] = 'set SCENARIO_FILE=../userData/scenarios/'+rndScn+'\n'

            # and write everything back
            with open('./scenarios/scenario.bat', 'w') as file:
                file.writelines(data)

            # now start the new BAT
            print('Running Scenario '+rndScn+'\n')
            os.system('start '+scen_dir+scen)
        else:
            
            rndScn = files[0]
            
            # making sure the selected scenario
            # is existent in the main scenarios folder
            # of VRF 
            src = './scenarios/scnx/'+str(rndScn)
            dst = str(os.getenv('mak_vrfdir'))+'/userData/scenarios/'
            shutil.copy2(src, dst)
            
            # read our VRF SIM BAT
            with open('./scenarios/scenario.bat', 'r') as file:
                # read a list of lines into data
                data = file.readlines()

            # print our current file that is goign to be used and the new one
            print("\nYour current ScenarioFile: "+ data[39])
            print('New Scenario will be: '+ rndScn + "\n")
            
            # change the SCENARIO_FILE to the randomly chosen one
            data[39] = 'set SCENARIO_FILE=../userData/scenarios/'+rndScn+'\n'

            # and write everything back
            with open('./scenarios/scenario.bat', 'w') as file:
                file.writelines(data)

            # now start the new BAT
            print('Running Scenario '+rndScn+'\n')
            os.system('start '+scen_dir+scen)
