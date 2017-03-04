from lib.config import load_config as lc
from os import listdir, path

def get_databases ():
	return [path.abspath (path.join (lc()['databases_root'], db)) for db in listdir (lc () ['databases_root']) if db.startswith (lc ()['default_dbfile_prefix'])]