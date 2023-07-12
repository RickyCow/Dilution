import subprocess
import sys

try:
  import pyvo as vo
except ImportError:
  subprocess.check_call([sys.executable, "-m", "pip", "install", 'pyvo'])
finally:
    import pyvo as vo

from io import BytesIO
from astropy.io import votable
import numpy as np
from astropy.table import Table
import matplotlib as plt



def SIMBAD():
    r = vo.regsearch(servicetype = 'tap', keywords = ['Simbad'])
    return r[0].service

def Vizier():
    r = vo.regsearch(servicetype = 'tap', keywords = ['Vizier'])
    k = int(np.nonzero(['obstap' not in rr['ivoid'] for rr in r])[0]) 
    return r[k].service

q = """
SELECT basic.OID,
       RA,
       DEC,
       main_id
FROM basic JOIN ident ON oidref = oid
WHERE id = 'omega Centauri'
"""