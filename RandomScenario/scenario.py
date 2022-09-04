import os, random, shutil

def init():
        # checks if you want to start the program or change domain
        print('Start or Change Domain\n')
        val = str.lower(input())
        if val == 'start' or val == 's':
            start()
        if val == 'create':
            create()
        if val == 'change' or val == 'domain' or val == 'c' or val == 'd':
            change()
        if val == 'help' or val == 'h':
            # help
            print('\nTo use the application, these are the applicable commands:')
            print('\nstart or s to start the main program', 'change or c to change DomainID\n', sep='\n')
            init()
            
        if val != 'start' or val != 's' or val != 'change' or val != 'c' or val != 'help' or val != 'h':
            # invalid inputs
            print('\nInvalid input.\n')
            print('Type help or h for help\n')
            init()

def start():
    random.seed()
    # clear CMD screen
    os.system('cls')
    
    # scenarios folder location and bat name
    scen_dir = os.path.abspath("./scenarios")
    scen = "/scenario.bat"
    # print(scen_dir) #remove # to check if path is correct  
            
    # scnx files location
    for root, dirs, files in os.walk('./scenarios/scnx'):
        flen = len(files) -1

    # this check is to prevent error if only one scenario file exists
    if flen >= 1:
        
        # random number from 0 (as indexs start from 0) till (including) the amount of files
        # in the files directory
        random.shuffle(files)
        rndnum = str(random.randint(0,flen))
        
        # random scenario chosing
        rndScn = files[int(rndnum)]

        # making sure the selected scenario
        # is existent in the main scenarios folder
        # of VRF            
        src = f'./scenarios/scnx/{rndScn}'
        makDir = os.getenv('mak_vrfdir')
        dst = f'{makDir}/userData/scenarios/'
        shutil.copy2(src, dst)
        
        # read our VRF SIM BAT
        with open('./scenarios/scenario.bat', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
        
        #change title to new scenario
        titleData = rndScn.split('.')
        data[2] = f'title {titleData[0]}\n'
        
        # print our current file that is going to be used and the new one
        splitData = data[39].split('/')
        print(f'\nYour current ScenarioFile: {splitData[3]}')
        print(f'New Scenario will be: {titleData[0]}\n')
        
        # change the SCENARIO_FILE to the randomly chosen one
        data[39] = f'set SCENARIO_FILE=../userData/scenarios/{rndScn}\n'
        
        # write everything back
        with open('./scenarios/scenario.bat', 'w') as file:
            file.writelines(data)

        # now start the new BAT
        print(f'Starting VRFSIM with new scenario\n')
        os.system(f'start {scen_dir}{scen}')
        init()
        
    # if only one scenario file exists in the scnx folder it will be the only one chosen to start with
    else:
        
        # assigning the scenario to a var
        scn = files[0]
        
        # making sure the selected scenario
        # is existent in the main scenarios folder
        # of VRF 
        src = f'./scenarios/scnx/{scn}'
        makDir = os.getenv('mak_vrfdir')
        dst = f'{makDir}/userData/scenarios/'
        shutil.copy2(src, dst)
        
        # read our VRF SIM BAT
        with open('./scenarios/scenario.bat', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
            
        #change title to new scenario
        titleData = scn.split('.')
        data[2] = f'title {titleData[0]}\n'
        
        # print our current file that is going to be used and the new one
        splitData = data[39].split('/')
        print(f'\nYour current ScenarioFile: {splitData[3]}')
        print(f'New Scenario will be: {titleData[0]}\n')
        
        # change the SCENARIO_FILE to the new one
        data[39] = f'set SCENARIO_FILE=../userData/scenarios/{scn}\n'
        
        # write back to bat
        with open(f'./scenarios/scenario.bat', 'w') as file:
            file.writelines(data)

        # start the new BAT
        print(f'Starting VRFSIM with new scenario\n')
        os.system(f'start {scen_dir}{scen}')
        init()        
            
def create():
    random.seed()
    # clear CMD screen
    os.system('cls')
    
    # scenarios folder location and bat name
    scen_dir = os.path.abspath("./scenarios")
    scen = "/scenario.bat"
    # print(scen_dir) #remove # to check if path is correct  
            
    # scnx files location
    for root, dirs, files in os.walk('./scenarios/scnx'):
        flen = len(files) -1

    # this check is to prevent error if only one scenario file exists
    if flen >= 1:
        
        # random number from 0 (as indexs start from 0) till (including) the amount of files
        # in the files directory
        random.shuffle(files)
        rndnum = str(random.randint(0,flen))
        
        # random scenario chosing
        rndScn = files[int(rndnum)]

        # making sure the selected scenario
        # is existent in the main scenarios folder
        # of VRF            
        src = f'./scenarios/scnx/{rndScn}'
        makDir = os.getenv('mak_vrfdir')
        dst = f'{makDir}/userData/scenarios/'
        shutil.copy2(src, dst)
        
        # read our VRF SIM BAT
        with open('./scenarios/scenario.bat', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
        
        #change title to new scenario
        titleData = rndScn.split('.')
        data[2] = f'title {titleData[0]}\n'
        
        # print our current file that is going to be used and the new one
        splitData = data[39].split()
        print(f'\nYour current ScenarioFile: {splitData[1][36:]}\n')
        print(f'New Scenario will be: {titleData[0]}\n')
        
        # change the SCENARIO_FILE to the randomly chosen one
        data[39] = f'set SCENARIO_FILE=../userData/scenarios/{rndScn}\n'
        
        # write everything back
        with open(f'./scenarios/{titleData[0]}.bat', 'w') as file:
            file.writelines(data)

        # now start the new BAT
        print(f'Starting VRFSIM with new scenario\n')
        os.system(f'start {scen_dir}/{titleData[0]}.bat')
        init()
        
    # if only one scenario file exists in the scnx folder it will be the only one chosen to start with
    else:
        
        # assigning the scenario to a var
        scn = files[0]
        
        # making sure the selected scenario
        # is existent in the main scenarios folder
        # of VRF 
        src = f'./scenarios/scnx/{scn}'
        makDir = os.getenv('mak_vrfdir')
        dst = f'{makDir}/userData/scenarios/'
        shutil.copy2(src, dst)
        
        # read our VRF SIM BAT
        with open('./scenarios/scenario.bat', 'r') as file:
            # read a list of lines into data
            data = file.readlines()

        # print our current file that is going to be used and the new one
        splitData = data[39].split()
        print(f'\nYour current ScenarioFile: {splitData[1][36:]}\n')
        print(f'New Scenario will be: {scn}\n')
        
        # change the SCENARIO_FILE to the new one
        data[39] = f'set SCENARIO_FILE=../userData/scenarios/{scn}\n'

        #change title to new scenario
        titleData = scn.split('.')
        data[2] = f'title {titleData[0]}\n'
        
        # write back to bat
        with open(f'./scenarios/{scn}.bat', 'w') as file:
            file.writelines(data)

        # start the new BAT
        print(f'Starting VRFSIM with {scn}\n')
        os.system(f'start {scen_dir}/{scn}.bat')
        init()
            
def change():
    os.system('cls')
    # read our VRF SIM BAT
    with open('./scenarios/scenario.bat', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    
    
    # current domain
    print(f'\nYour Current DomainID: {data[43][3:5]}')
    print(f'\nYour Current AppNumber: {data[42][3:7]}')
    print(f'\nYour Current SiteID: {data[44][9:11]}')
    print(f'\nYour Current sessionId: {data[45][12:14]}')
    
    # new domain assigning 
    print('\nNew Domain?\n')
    newDom = input()
    
    if newDom.isdigit() is True:
        os.system('cls')
        userDir = os.getenv('userprofile')
        parent_dir = f'{userDir}/Desktop/BE_LOGS'
        directory = f'Domain{newDom}'
        path = os.path.join(parent_dir, directory)
        os.makedirs(path, exist_ok=True)
        
        if len(newDom) == 1:
            # if new domain is single digit

            data[37] = f'set DOMAIN={newDom}\n'
            data[42] = f'-a 310{newDom} ^\n'
            data[43] = f'-x {newDom} ^\n'
            data[44] = f'--siteId {newDom} ^\n'
            data[45] = f'--sessionId {newDom} ^\n' 
            
            # new domain
            print(f'\nYour New DomainID: {data[43][3]}')
            print(f'\nYour New AppNumber: {data[42][3:7]}')
            print(f'\nYour New SiteID: {data[44][9]}')
            print(f'\nYour New sessionId: {data[45][12]}\n')
            
        else:
            if len(newDom) == 2:
                os.system('cls')
                # if new domain is two digits
                
                data[37] = f'set DOMAIN={newDom}\n'
                data[42] = f'-a 31{newDom} ^\n'
                data[43] = f'-x {newDom} ^\n'
                data[44] = f'--siteId {newDom} ^\n'
                data[45] = f'--sessionId {newDom} ^\n' 
                
                # new domain
                print(f'\nYour New DomainID: {data[43][3]}')
                print(f'\nYour New AppNumber: {data[42][3:7]}')
                print(f'\nYour New SiteID: {data[44][9]}')
                print(f'\nYour New sessionId: {data[45][12]}\n')
            else:
                os.system('cls')
                # if new domain in more than two digit
                data[37] = f'set DOMAIN={newDom}\n'
                data[42] = f'-a 3{newDom} ^\n'
                data[43] = f'-x {newDom} ^\n'
                data[44] = f'--siteId {newDom} ^\n'
                data[45] = f'--sessionId {newDom} ^\n'
                
                # new domain
                print(f'\nYour New DomainID: {data[43][3:6]}')
                print(f'\nYour New AppNumber: {data[42][3:7]}')
                print(f'\nYour New SiteID: {data[44][9:12]}')
                print(f'\nYour New sessionId: {data[45][12:15]}\n')
    else:
        os.system('cls')
        print('\nNew Domain must be a number!')
        change()

    
    # write back to bat
    with open('./scenarios/scenario.bat', 'w') as file:
        file.writelines(data)
    
    init()
    
init()