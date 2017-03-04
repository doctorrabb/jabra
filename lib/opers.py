from lib.utils import lf
from lib.config import load_config as lc
from lib.colors import *
from os import remove, system
from lib.db import get_databases

class CommandOperations:
	def __init__ (self, jabber):
		self.jabber = jabber


	def placedb (self):
		from shutil import move as mv

		try:
			mv (raw_input (INFO + 'Enter db file path: '), lc () ['databases_root'])
			print YES + 'Database placed!'
		except Exception as e:
			print ERR + 'Error placing database file! Details: ' + e
			exit (1)

	def getdbs (self):
		for database in get_databases():
			print database.replace (lc ()['default_dbfile_prefix'], "")

	def run (self):

		if len (get_databases ()) > 0:
			for db in get_databases ():
				with open (db) as database:
					for user in database.readlines ():
						usr = user.strip ('\r\n')
						print INFO + 'Sending spam to %s ...' % usr
						self.jabber.send_message (usr, lf (lc ()['content_file']))
					
				database.close ()
			self.jabber.disconnect ()
		else:
			print ERR + 'No databases files in db directory: %s' % lc () ['databases_root']

	def quit (self):
		print 'Good bye!'
		exit (0)

	def dbclear (self):
		for database in get_databases():
			print INFO + 'Removing database %s' % database
			remove (database)
		print YES + 'Databases were cleaned!'