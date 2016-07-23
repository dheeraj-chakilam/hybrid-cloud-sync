import Configurer

def Add():
	Configurer.config.add_section('Installation')
	dirloc = raw_input("Please enter the installation directory location:")
	with open('Settings.cfg', 'wb') as configfile:	
		Configurer.config.set('Installation', 'dir_loc', dirloc)
		Configurer.config.write(configfile)
	return

def main():
	#Show/Print Installation Location
	#Ask if user wants to change Installation location
	return

if __name__ == "__main__":
	#if opened directly (eg. double clicked) do nothing
	pass
