from lib.config import load_config as lc, load_creds as lcr
from lib.jabber import JabberJob
from lib.opers import CommandOperations
from lib.colors import *
from lib.utils import *

def get_operations ():
	from inspect import getmembers, ismethod

 	for operation in getmembers (CommandOperations, predicate=ismethod):
 		if operation [0] != "__init__":
 			print operation [0]

def main ():

	jabber = None

	print lf (lc () ['prompt_screen_file'])

	try:
		print INFO + 'Logging in ...'
		jabber = JabberJob (lcr ()['login'], lcr ()['password'], lcr ()['server'])
	except:
		print ERR + 'Error auth in account!'
		exit (1)
	
	print YES + 'Logged in successfully :3'

	while True:
		try:
			task = raw_input (INFO + "Enter task (\"?\" for listing tasks): ")
			if task == '?': get_operations ()
			else: getattr (CommandOperations (jabber), task) ()
		except KeyboardInterrupt:
			exit (0)
		except AttributeError:
			print ERR + 'Invalid command'


	




if __name__ == '__main__':
	main ()