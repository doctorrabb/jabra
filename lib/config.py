from json import loads
from lib.utils import lf
from lib.const import CONFIG_PATH

def load_config ():
	return loads (lf (CONFIG_PATH))

def load_creds ():
	return loads (lf (load_config () ['default_creds_file']))