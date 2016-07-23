import Configurer

def Add():
	Configurer.config.add_section('SyncDirectories')
	print "You can add more than one directory. To stop adding directories, type \"nomore\" (without the quotes)"
	i = 1
	dirloc = raw_input("Please enter the directory location:")
	while (dirloc != "nomore"):
		configfile = open('Settings.cfg', 'wb')
		dir_loc = "dir_loc" + str(i)
		Configurer.config.set('SyncDirectories', dir_loc, dirloc)
		Configurer.config.write(configfile)
		configfile.close()
		i = i+1

		dirloc = raw_input("Please enter the directory location:")
	return

def main():
	#Print List of Directories
	#Ask if user wants to add/edit list of directories
	return

if __name__ == "__main__":
	#if opened directly (eg. double clicked) do nothing
	pass
