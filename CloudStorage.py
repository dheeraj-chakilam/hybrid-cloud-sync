import Configurer

def Add():
	Configurer.config.add_section('CloudStorage')
	dirloc = raw_input("Please enter the cloud storage directory location:")
	with open('Settings.cfg', 'wb') as configfile:	
		Configurer.config.set('CloudStorage', 'dir_loc', dirloc)
		Configurer.config.write(configfile)
	return

def main():
	#Show/Print Cloud Storage Location
	#Ask if user wants to change cloud storage location
	return

if __name__ == "__main__":
	#if opened directly (eg. double clicked) do nothing
	pass
