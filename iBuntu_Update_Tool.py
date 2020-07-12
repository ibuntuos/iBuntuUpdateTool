#!/usr/bin/env python
#	(c) 2020 by iBuntu OS
# 	07/10/2020
#	Tool for Helping with Update or Upgrade iBuntu to new version


import PySimpleGUI as sg
import webbrowser as browser
import os
import packagelist
import subprocess

sg.theme('LightGrey')
WorkPath=os.path.dirname(os.path.realpath(__file__))
#WorkPath=os.path.dirname(WorkPath)


#Define Layouts for Frames
frame_layout = [
                  [sg.T('')],
                  [sg.T('1.'), sg.Radio('Backup your system', "RADIO1", enable_events=True, key='Backup')],
                  [sg.T('')],
                  [sg.T('2.'),sg.Radio('Save your Packages', "RADIO1", enable_events=True, key='Save')],
                  [sg.T('')],
                  [sg.T('3.'),sg.Radio('Download iBuntu', "RADIO1", enable_events=True, key='Download')],
                  [sg.T('')],
                  [sg.T('4.'),sg.Radio('Create Bootstick', "RADIO1", enable_events=True, key='Bootstick')],
                  [sg.T('')],
                  [sg.T('5.'),sg.Radio('Update your System', "RADIO1", enable_events=True, key='Update')],
                  [sg.T('')],
                  [sg.T('6.'),sg.Radio('Restore your Packages', "RADIO1", enable_events=True, key='Restore')],
                  [sg.T('')],
                  [sg.T('                '),sg.Button('OK')],
               ]

frame_layout_Text = [
                  [sg.T('				', key='Textlabel_1')],
                  [sg.T('				', key='Textlabel_2')],
                  [sg.T('				', key='Textlabel_3')],
                  [sg.T('				', key='Textlabel_4')],
                  [sg.T('				', key='Textlabel_5')],
                  [sg.T('				', key='Textlabel_6')],
                  [sg.T('				', key='Textlabel_7')],
                  [sg.T('				', key='Textlabel_8')],
                  [sg.T('				', key='Textlabel_9')],
                  [sg.T('				', key='Textlabel_10')],
                  [sg.T('				', key='Textlabel_11')],
                  [sg.T('				', key='Textlabel_12')],
                  [sg.T('				', key='Textlabel_13')],
                  [sg.T('				', key='Textlabel_14')],
               ]


#Define Colums of Labels
colHeader = [[sg.Image(r''+WorkPath+'/UpdateLogo.png'), sg.Text('iBuntu Update Tool', font=("SF Compact Display", 18), text_color='black'), sg.Image(r''+WorkPath+'/update-icon-18.png')]]
colClose = [[sg.Text('© 2020  iBuntu OS', font=("Helvetica", 9)),sg.Text('   iBuntuos.com', font=("Helvetica", 9)),sg.Button('Close')]]



#Define Main Window-Layout
layout = [
          [sg.Column(colHeader)],
          [sg.Frame('Options', frame_layout, font='Any 9', title_color='blue'), sg.Frame('Guide', frame_layout_Text, font='Any 9', title_color='blue')],
          [sg.Column(colClose)],
         ]


#Define Output-Window-Layout
layout2 = [
		[sg.Multiline(size=(60, 20), background_color='#A2D2FF', text_color='white', key='textbox')],
		[sg.Button('Close Window')]
          ]



#Initialize the whole thing

window = sg.Window('iBuntu Update Tool', layout, font=("Helvetica", 12), size=(600, 600), finalize=True)
window.Element('Textlabel_4').update('This tool is for helping you')
window.Element('Textlabel_5').update('migrate Your System safely from one')
window.Element('Textlabel_6').update('Version to another.')
window.Element('Textlabel_8').update('Just follow the instructions on the')
window.Element('Textlabel_9').update('left from Top to Bottom and this tool')
window.Element('Textlabel_10').update('will guide you through the process')
window.Element('Textlabel_11').update('with as less effort for you as possible.')
run=1



while True:
	event, values = window.read()

	if event == sg.WIN_CLOSED or 'Close' in event:
		break


#Changing the Information-Tab according to choosen Radiobutton

	if event == 'Backup':
		window.Element('Textlabel_1').update('')
		window.Element('Textlabel_2').update('')
		window.Element('Textlabel_3').update('')
		window.Element('Textlabel_4').update('')
		window.Element('Textlabel_5').update('First you always should make a Backup')
		window.Element('Textlabel_6').update('of your system to ensure that you can')
		window.Element('Textlabel_7').update('role back if ever something went wrong.')
		window.Element('Textlabel_10').update('Press \'OK \' to start Timeshift,')
		window.Element('Textlabel_11').update('the Backup Tool of iBuntu OS.')
		window.Element('Textlabel_8').update('')
		window.Element('Textlabel_9').update('')
		window.Element('Textlabel_12').update('')
		window.Element('Textlabel_13').update('')
		window.Element('Textlabel_14').update('')


	if event == 'Save':
		window.Element('Textlabel_1').update('')
		window.Element('Textlabel_2').update('')
		window.Element('Textlabel_3').update('Because you will lose the software you')
		window.Element('Textlabel_4').update('installed manually since you are using')
		window.Element('Textlabel_5').update('iBuntu you need to create a list')
		window.Element('Textlabel_6').update('of all packages you added yourself')
		window.Element('Textlabel_7').update('since you installed iBuntu before.')
		window.Element('Textlabel_8').update('')
		window.Element('Textlabel_9').update('Press \'OK\' to save your package-List ')
		window.Element('Textlabel_10').update('for Restoring it after the Uprade/Update.')
		window.Element('Textlabel_11').update(')
		window.Element('Textlabel_12').update('')
		window.Element('Textlabel_13').update('')



	if event == 'Download':
		window.Element('Textlabel_1').update('')
		window.Element('Textlabel_2').update('')
		window.Element('Textlabel_3').update('')
		window.Element('Textlabel_4').update('')
		window.Element('Textlabel_5').update('Now you need to download the newest')
		window.Element('Textlabel_6').update('Version of iBuntu to go on.')
		window.Element('Textlabel_7').update('')
		window.Element('Textlabel_10').update('')
		window.Element('Textlabel_11').update('')
		window.Element('Textlabel_8').update('Press \'OK \' to go to "ibuntuos.com"')
		window.Element('Textlabel_9').update('Where you can download it.')
		window.Element('Textlabel_12').update('')
		window.Element('Textlabel_13').update('')
		window.Element('Textlabel_14').update('')


	if event == 'Bootstick':
		window.Element('Textlabel_1').update('If your iBuntu runs directly on your')
		window.Element('Textlabel_2').update('Hardware you now have to create a')
		window.Element('Textlabel_3').update('bootable USB-Stick from which you can')
		window.Element('Textlabel_4').update('run the Installation')
		window.Element('Textlabel_5').update('')
		window.Element('Textlabel_6').update('We recommend Balena Etcher since this')
		window.Element('Textlabel_7').update('Tool ist totally Self-Explaining.')
		window.Element('Textlabel_8').update('')
		window.Element('Textlabel_9').update('Press \'OK \' to start the Tool')
		window.Element('Textlabel_10').update('or download it, if your iBuntu Version')
		window.Element('Textlabel_11').update('is below 1.3')
		window.Element('Textlabel_12').update('')
		window.Element('Textlabel_13').update('')
		window.Element('Textlabel_14').update('')


	if event == 'Update':
		window.Element('Textlabel_1').update('This is the most important Step!')
		window.Element('Textlabel_2').update('To make sure your Upgrade/Update will')
		window.Element('Textlabel_3').update('be a success and you won\'t need your')
		window.Element('Textlabel_4').update('Backup at all, follow the separate')
		window.Element('Textlabel_5').update('Tutorial we created especially for this')
		window.Element('Textlabel_6').update('case.')
		window.Element('Textlabel_7').update('')
		window.Element('Textlabel_8').update('Press \'OK \' to open it.')
		window.Element('Textlabel_9').update('')
		window.Element('Textlabel_10').update('You also can watch our video Tutorial')
		window.Element('Textlabel_11').update('The Link you find at the Top of the')
		window.Element('Textlabel_12').update('written Guide.')
		window.Element('Textlabel_13').update('Like this you won\'t loose your data')
		window.Element('Textlabel_14').update('in the process.')

	if event == 'Restore':
		window.Element('Textlabel_1').update('After the Upgrade/Update you manually')
		window.Element('Textlabel_2').update('installed programs are gone - but not')
		window.Element('Textlabel_3').update('your settings for them so don\'t worry.')
		window.Element('Textlabel_4').update('You only need to restore the packages')
		window.Element('Textlabel_5').update('Than all your programs and settings ')
		window.Element('Textlabel_6').update('will be back.')
		window.Element('Textlabel_7').update('')
		window.Element('Textlabel_8').update('just click \'OK \' and all' )
		window.Element('Textlabel_9').update('your manually installed programs')
		window.Element('Textlabel_10').update('will be restored by this tool.')
		window.Element('Textlabel_11').update('')
		window.Element('Textlabel_12').update('')
		window.Element('Textlabel_13').update('')
		window.Element('Textlabel_14').update('')



#Take Action after pressing OK according to choosen Radiobutton
	if event == 'OK':
		if values['Backup'] == True:
			os.system("timeshift-launcher")
			#browser.open('http://ibuntuos.com', new=2)
			#browser.open('https://www.balena.io/etcher/', new=2)

		if values['Save'] == True:
			if run ==1:
				codewindow = sg.Window('Packagerestore', layout2, font=("Helvetica", 12), finalize=True)

			else:
				run=1
				codewindow.UnHide()

			while True and run ==1:
				run=2
				packages=packagelist.packagelist()
				codewindow['textbox'].update('')
				codewindow['textbox'].print(WorkPath)
				codewindow['textbox'].print("A Backup of your manually installed packages is created.")
				codewindow['textbox'].print("--------------------------------------------------------")
				codewindow['textbox'].print("Following manually installed packages exist:")
				f=open(os.path.join(WorkPath, "packages.list.save"),'w')
				for ele in packages:
					f.write(ele+'\n')
					codewindow['textbox'].print(ele)
				f.close()
				codewindow['textbox'].print("--------------------------------------------------------")
				if os.path.exists(os.path.join(WorkPath, "packages.list.save")):
					codewindow['textbox'].print("Package List saved successfully.")
					codewindow['textbox'].print("Now we save your Snaps and Apps.")
					codewindow['textbox'].print("Follow the Instructions in the Popup-Terminal.")
					codewindow['textbox'].print("After you are done and the Terminal has closed again")
					codewindow['textbox'].print("the Saving is Completed. Than you can close this window.")
					os.system("gnome-terminal -- sh "+os.path.join(WorkPath, "backup.sh"))
					codewindow['textbox'].print("========================================================")
				else:
					codewindow['textbox'].print("[ERROR]: Package List was NOT created successfully!!")
					codewindow['textbox'].print("========================================================")

				ev2, vals2 = codewindow.Read()


				if ev2 == sg.WIN_CLOSED or ev2 == 'Close Window':
					codewindow.Hide()
				else:
					print("no way out!")


		if values['Download'] == True:
			browser.open('https://ibuntuos.com/get-it', new=2)

		if values['Bootstick'] == True:
			systemversion=(subprocess.check_output("lsb_release -d | cut -c 21-23" , shell=True, universal_newlines=True)).strip()
			systemversion = systemversion.replace(".", "")
			print(systemversion)
			if int(systemversion) < 13:
				browser.open('https://www.balena.io/etcher/', new=2)
			else:
				os.system("/etc/balena_etcher/balenaEtcher-1.5.101-x64.AppImage")

		if values['Update'] == True:
			browser.open_new(r'file://'+WorkPath+'/iBuntuUpdateTool_Guide.pdf')

		if values['Restore'] == True:
			if run ==1:
				codewindow = sg.Window('Packagerestore', layout2, font=("Helvetica", 12), finalize=True)

			else:
				run=1
				codewindow.UnHide()

			while True and run ==1:
				run=2
				codewindow['textbox'].update('')
				if not os.path.exists(os.path.join(WorkPath, "packages.list.save")):
					codewindow['textbox'].print("--------------------------------------------------------")
					codewindow['textbox'].print('Sorry: No previously saved Package-List found.')
					codewindow['textbox'].print("--------------------------------------------------------")
				else:
					codewindow['textbox'].print("--------------------------------------------------------")
					codewindow['textbox'].print("Packagelist found - Restoring started.")
					os.system("gnome-terminal -- sh "+os.path.join(WorkPath, "restore.sh"))
					#os.system("gnome-terminal -- xargs -a '"+os.path.join(WorkPath, "packages.list.save")+"' sudo apt install")
					codewindow['textbox'].print("Follow the Instructions in the Popup-Terminal.")
					codewindow['textbox'].print("After you are done and the Terminal has closed again")
					codewindow['textbox'].print("the Restore is Completed. Than you can close this window.")
					codewindow['textbox'].print("========================================================")
					os.remove(os.path.join(WorkPath, "packages.list.save"))

				ev2, vals2 = codewindow.Read()


				if ev2 == sg.WIN_CLOSED or ev2 == 'Close Window':
					codewindow.Hide()
				else:
					print("no way out!")
		else:
			print(event)



window.close()
