################################################################# PROJECT DEVELOPMENT LOG ########################################################################################## 
################################################################# GENERAL ######################################################################### 

S:\Orders\Orders\1100102000\1100102005_LYONDELL_BASELL_MEXICO\Proc\HMI\Lyondell_Jess


MM/DD/YYYY -	NOTES
10/13/2021 - 	10/13/2021	LOST PREVIOUS NOTES :( ; redid.
10/202021 - 	None Grouped Extracted; scripted data extract
				To Do:		Import non grouped
							Extract Grouped
							Import Grouped
10/212021 - 	Major Issues with my computer, had to get it fixed yesterday took all day
		Ungrouped Tags:
		Exported data using 2 scripts (2 buttons), 
		Imported data using 1 scripts; 
		*created a tag folder and fake tags to run a test first, then imported REAL after
		Grouped Tags:
		Only need to change Alarm_Description Fields; for the grouped, format is:
		Group of Alarms: 	Alarm Description = 
					Description =
NOTES:

		Allie Project Help Instructions

add designer
manual

http://10.10.251.4:8088

issue: "Host Unreachable" val said sim problems; something about VM settings

click network adapter button - disconnect

refresh desktop 

worked this top

open NEW Lyondell: Lyondell_Basell (1)		
		

################################################################# PROJECT PURPOSE ####################################################################################################  
-> 	Currently, the Tag Historian Log doesn't display the correct descriptions within the "Fault_Description" and "Equip_Description" Values stored in those memory tags
-> 	The description needed for each of those memory values are currently located within the: Vision Property Editor.
->	Extract the alarmpath, alm_desc, and desc fields from the vision property editor.
->	Then, go to the alm folder, within that folder, go to the memory tag fault and equip folders, and put in the appropriate fields (details in instructions). 

->	ALL of the fields need to be changed for EACH line on EACH screen:

UNGROUPED:

GROUPED:
		Only need to change Alarm_Description Fields; for the grouped, format is:
		Group of Alarms: 	Alarm Description = Fault_Description
					Description = Equip_Description
		Group
			Alarm1	
				PATH = [default]SPG/Line 1/Fiberglass/L1AK_01/L1AK_01_ZS_0501/ALM
				Alarm Description = Fault_Description
					Alarm1Description -> Changes per alarm
				Description = Equip_Description
					GROUPDESCRIPTION -> NEVER CHANGES
			Alarm2
				PATH = [default]SPG/Line 1/Fiberglass/L1AK_01/L1AK_01_ZS_0502/ALM
				Alarm Description = Fault_Description
					Alarm2Description
				Description = Equip_Description
					GROUPDESCRIPTION
			Alarm3
				Alarm Description = Fault_Description
					Alarm2Description
				Description = Equip_Description
					GROUPDESCRIPTION


[default]SPG/Liquid and Dust Collection/Dust Collection/C9CP_05/C9CP_05_HBS_01/ALM

Emergency Stop = alarm = bottom

################################################################# INSTRUCTIONS ######################################################################################################
Lyondell_Basell (1)
spgadmin
2191
Open the copy_of_Lyondell_Basell

Vision Property Editor -> Template Properties -> 
						-> AlarmPaths		<Dataset>
						-> Alm_Description 	<field>
						-> Description		<field>
						-> Line_Description	<field>
	0) Record Screen, Line:
					Screen:
					Line:
	
	1)What I need to Extract:
					*	AlarmPaths		<Dataset> 	
		C/P the dataset link; I will need this later to get to the correct item memory tags (below)
					*	Alm_Description <field>	
					*	Description 	<field>	
	2)What I need to Input:
					*	AlarmPaths	<Dataset> -> Link:
		Follow the link of the Dataset. The last part of the link will be the ALM folder. 
		Within the alarm folder, locate the following folders:
			Equip_Description	(Memory Tag)
			Fault_Description 	(Memory Tag)
				** NOTE: The Memory Tag folders listed above are WITHIN the ALM folder, NOT the folders wit hthe same name within the MAIN Folder!!!!
		Add the appropriate descritions to the appropiate memory tag folders: 
					*	Alm_Description <field>	->	/Fault_Description (Memory Tag) *double click, scroll down to Value located in Value* <Value>
					*	Description 	<field> ->	/Equip_Description (Memory Tag) *double click, scroll down to Value located in Value* <Value>

EXAMPLE:
					Screen:
					Line:Central Vav Convey Line 5
	
					*	AlarmPaths	<[default]SPG/Liquid and Dust Collection/Central Vacuum/C9DC_02/C9DC_02_PDH_0808/ALM/> 
					*	Alm_Description <Differential Pressure High>	->	/Fault_Description (Memory Tag) <Differential Pressure High>
					*	Description 	<Filter Receiver> 				->	/Equip_Description (Memory Tag) <<Filter Receiver>
######################      Folder STRUCTURE #######################################################################################################################################  
######################      NOTES			 #######################################################################################################################################  

Lyondell_Basell (1)
spgadmin
2191
Open the copy_of_Lyondell_Basell

CURRENT: Current working file of ongoing project
ARCHIVE: ALL BACKCUPS
Allie Project Help Instructions
add designer
manual
http://10.10.251.4:8088
issue: "Host Unreachable" val said sim problems; something about VM settings
click network adapter button - disconnect
refresh desktop 
worked this top
open NEW Lyondell: Lyondell_Basell (1)
################################################################################## END NOTES FOR USER####################################################################################################################
BUTTON 1 EXTRACT:

for comp in event.source.parent.getComponents(): 
	compname = comp.name
	parsname = compname[0:20]
	component = event.source.parent.getComponent('Power Table')
	if parsname == 'Coded Alarm Triangle':
		print comp.name
		#print comp.AlarmPaths.getValueAt(0,0)
		#print comp.Alm_Description
		#print comp.Description
for comp in event.source.parent.getComponents(): 
	compname = comp.name
	parsname = compname[0:20]
	component = event.source.parent.getComponent('Power Table')
	if parsname == 'Coded Alarm Triangle':
		#print comp.name
		print comp.AlarmPaths.getValueAt(0,0)
		#print comp.Alm_Description
		#print comp.Description
for comp in event.source.parent.getComponents(): 
	compname = comp.name
	parsname = compname[0:20]
	component = event.source.parent.getComponent('Power Table')
	if parsname == 'Coded Alarm Triangle':
		#print comp.name
		#print comp.AlarmPaths.getValueAt(0,0)
		print comp.Alm_Description
		#print comp.Description
		
BUTTON 2 EXTRACT:

for comp in event.source.parent.getComponents(): 
	compname = comp.name
	parsname = compname[0:20]
	component = event.source.parent.getComponent('Power Table')
	if parsname == 'Coded Alarm Triangle':
		#print comp.name
		#print comp.AlarmPaths.getValueAt(0,0)
		#print comp.Alm_Description
		print comp.Description

BUTTON 1 IMPORT:

BLAH BLAH BLAH
