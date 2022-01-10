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

routine_name = sys.argv[1] if len(sys.argv) >= 2 else None
cli_args = sys.argv[2:]

routines = [from_db, pulse, swap, static_rainbow, noise, rotate, off]

routine_map = {}

for r in routines:
	routine_map[r.__name__] = r

def get_arg_names(fn):
	return fn.__code__.co_varnames[:fn.__code__.co_argcount]

def do_routine(routine_name):
	routine = routine_map[routine_name]
	routine_args = get_arg_names(routine)
	call_args = {}

	for a in range(0, len(cli_args)):
		arg_name = routine_args[a]
		split = cli_args[a].split(":")
		arg_val = split[0]

		if len(split) >= 2:
			arg_name = split[0]
			arg_val = split[1]

		if "," in arg_val: arg_val = tuple(map(int, arg_val.split(",")))
		else: arg_val = float(arg_val)

		call_args[arg_name] = arg_val

	routine(**call_args)

if routine_name == None:
	print("No routine specified, turning off")
	off()
elif routine_name not in routine_map: print("No routine named " + "\"" + routine_name + "\"")
else: do_routine(routine_name)
