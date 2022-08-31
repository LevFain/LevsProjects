
@ECHO OFF
title Peekabo
color 8F
cd /d %MAK_VRFDIR%/bin64

:WMIC
:: Check WMIC is available
WMIC.EXE Alias /? >NUL 2>&1 || GOTO s_error

:: Use WMIC to retrieve date and time
FOR /F "skip=1 tokens=1-6" %%G IN ('WMIC Path Win32_LocalTime Get Day^,Hour^,Minute^,Month^,Second^,Year /Format:table') DO (
   IF "%%~L"=="" goto s_done
      Set _yyyy=%%L
      Set _mm=00%%J
      Set _dd=00%%G
      Set _hour=00%%H
      SET _minute=00%%I
      SET _second=00%%K
)

:s_done
:: Pad digits with leading zeros
      Set _mm=%_mm:~-2%
      Set _dd=%_dd:~-2%
      Set _hour=%_hour:~-2%
      Set _minute=%_minute:~-2%
      Set _second=%_second:~-2%

Set logtimestamp=%_hour%_%_minute%_%_second%-%_yyyy%_%_mm%_%_dd%
goto make_dump

:s_error
echo WMIC is not available, using default log filename
Set logtimestamp=_

:make_dump
set SIM_DESKTOP=C:\Users\VR-FORCES\Desktop\BE_LOGS
set FILENAME=BE_6_%logtimestamp%.log
set SCENARIO_FILE=../userData/scenarios/sensortest.scnx

start /B vrfSimHLA1516e.exe ^
-a 3102 ^
-x 2 ^
--siteId 2 ^
--sessionId 2 ^
-F RPR_FOM_v2.0_1516-2010.xml --rprFomVersion 2.0 --rprFomRevision 2 --fomModules MAK-VRFExt-4_evolved.xml --fomModules MAK-DIGuy-4_evolved.xml --fomModules MAK-LgrControl-2_evolved.xml --fomModules MAK-VRFAggregate-3_evolved.xml --fomModules MAK-DynamicTerrain-2_evolved.xml --loadPlugin MAK_DDS_Plugin.dll -n 1 --outputLogFile %SIM_DESKTOP%\Domain6\%FILENAME% --scenarioFileName "%SCENARIO_FILE%"
rem C:\MAK\vrforces4.7\bin64\vrfSimHLA1516e.exe -a 3021 -x 21 -F RPR_FOM_v2.0_1516-2010.xml --rprFomVersion 2.0 --rprFomRevision 2 --fomModules MAK-VRFExt-4_evolved.xml --fomModules MAK-DIGuy-4_evolved.xml --fomModules MAK-LgrControl-2_evolved.xml --fomModules MAK-VRFAggregate-3_evolved.xml --fomModules MAK-DynamicTerrain-2_evolved.xml --siteId 21 --loadPlugin MAK_DDS_Plugin.dll -n 1 --outputLogFile "%SIM_DESKTOP%\BE_Logs\Domain21\%FILENAME%" --scenarioFileName "%SCENARIO_FILE%"

pause

