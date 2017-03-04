from xmpp import Client, protocol
from lib.config import load_config
from lib.utils import lf
from os import listdir
from lib.exceptions import JabberAuthException

class JabberJob:
	def __init__ (self, login, password, server):
		self.client = Client (server, debug=[])

		self.client.connect ()
		if not self.client.auth (login, password):
			self.client.disconnect ()
			raise JabberAuthException ()

	def send_message (self, to, message):
		self.client.send (protocol.Message (to, message))

	def disconnect (self):
		self.client.disconnect ()