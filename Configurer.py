import ConfigParser

#creates an object to read and store values from the Configuration file
#Also if there is no configuration file, create a blank cfg file (whereafter sections will be added by Add Methods of different modules.

config = ConfigParser.ConfigParser()
configfile = open('Settings.cfg', 'a+')
config.readfp(configfile)
