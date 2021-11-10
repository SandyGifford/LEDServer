from utils.logging_utils import init_logging
init_logging()

from routines.from_db import from_db
from routines.pulse import pulse
from routines.swap import swap
from routines.static_rainbow import static_rainbow
from routines.noise import noise
from routines.rotate import rotate
from routines.off import off

from_db()
