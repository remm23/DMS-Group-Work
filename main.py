import os, database

os.system('powershell.exe cls')

active = True
prompt = ':>'

def help():
	print()
	print('\t\t--- Database Management System Commands ---')
	print('delete <column> <data> <table>:\t\t\t\t\t\t\tDelete a row from a table')
	print('find <data> <column> <table>:\t\t\t\t\t\t\tFilter out rows to find user')
	print('help:\t\t\t\t\t\t\t\t\t\tShow help menu')
	print('quit:\t\t\t\t\t\t\t\t\t\tExit the system')
	print('update <column1> <data> <table> <column2> <data>:\t\t\t\tUpdate a row in a table')
	print('showall <table>:\t\t\t\t\t\t\t\tShow all rows in a table')
	print()

print('\t\t--- PARTSWORLD DMS ---')
print('\ttype \'help\' to show a list of commands')

while (active):
	line = input(prompt)
	if not line:
		pass
	elif line.lower() == 'quit':
		active = False
	elif 'delete' in line:
		args = line.split(' ')
		## delete the <id> <x> from <table>
		database.delete(args[1],args[2],args[3])
	elif 'find' in line:
		args = line.split(' ')
		try:
			database.find(args[1],args[2],args[3])
		except:
			print("Invalid query")
	elif line == 'help':
		help()
	elif 'showall' in line:
		try:
			database.showall(line[8:])
		except:
			print("Invalid query")
	elif 'update' in line:
		args = line.split(' ')
		try:
		 	## update <col> to <x> in <table> where <col2> = <y>
			database.update(args[1], args[2], args[3], args[4], args[5])
		except:
			print('Invalid query')
	else:
		print('invalid input: ' + line)