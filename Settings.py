#! /usr/bin/python

import Configurer
import CloudStorage
import SyncDirectories
import Installation

#To check if the configuration file has the options present in their respective sections and create the options if they don't exist
if Configurer.config.has_section('CloudStorage') & Configurer.config.has_option('CloudStorage', 'dir_loc'):
	pass
else:
	CloudStorage.Add()

if Configurer.config.has_section('Installation') & Configurer.config.has_option('Installation', 'dir_loc'):
	pass
else:
	Installation.Add()

if Configurer.config.has_section('SyncDirectories') & Configurer.config.has_option('SyncDirectories', 'dir_loc1'):
	pass
else:
	SyncDirectories.Add()

# Functions
def CloudStorage_Main():
	return

def Status_Main():
	return

def Status_Logs():
	return
# End 

def main():
	print "List of operations:"

if __name__ == "__main__":
	#if opened directly (eg. double clicked) do nothing
	pass
