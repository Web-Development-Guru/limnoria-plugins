import os
import glob
from . import *

def handlers():
	lst = glob.glob(os.path.dirname(__file__)+"/*.py")
	return [ os.path.basename(f)[:-3] for f in lst if not name.startswith('_')]

#for p in __all__:
#	handles[p] = __import__(p)
#print(dir(handles))

#class HandlerMain:
	#from . import *
#	__all__ = [ os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__)+"/*.py")]
#	handles = [ __import__(p) for p in __all__ ]