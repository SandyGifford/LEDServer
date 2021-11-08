from utils.logging_utils import init_logging
init_logging()

from routines.watch_file import watch_file
from routines.pulse import pulse
from routines.swap import swap
from routines.static_rainbow import static_rainbow
from routines.noise import noise
from routines.rotate import rotate

rotate()
