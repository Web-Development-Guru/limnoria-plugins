import os
import glob

modules = glob.glob(os.path.dirname(__file__)+"/*.py")
__all__ = [ os.path.basename(f)[:-3] for f in modules]
handles = {}

for p in __all__:
	handles[p] = __import__(p)

print(dir(handles))

class HandlerMain:
	__all__ = [ os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__)+"/*.py")]
	for p in __all__:
		handles[p] = __import__(p)