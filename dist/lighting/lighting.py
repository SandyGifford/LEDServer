import sys
from utils.logging_utils import init_logging
init_logging()

from routines.from_db import from_db
from routines.pulse import pulse
from routines.swap import swap
from routines.static_rainbow import static_rainbow
from routines.noise import noise
from routines.rotate import rotate
from routines.off import off

routine = sys.argv[1] if len(sys.argv) >= 2 else None

print(routine)

if routine == None:
	print("No routine specified, turning off")
	off()
elif routine == "from_db": from_db()
elif routine == "pulse": pulse()
elif routine == "swap": swap()
elif routine == "static_rainbow": static_rainbow()
elif routine == "noise": noise()
elif routine == "rotate": rotate()
elif routine == "off": off()
else: print("No routine named " + "\"" + routine + "\"")
