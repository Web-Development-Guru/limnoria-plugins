from os import path
import glob

modules = glob.glob(path.dirname(__file__)+"/*.py")
__all__ = [ path.basename(f)[:-3] for f in modules]