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
	if routine_name not in routine_map: print("No routine named " + "\"" + routine_name + "\"")

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

def print_help(routine_name):
	if routine_name not in routine_map: print("No routine named \"%s\"" % routine_name)
	arg_str = ", ".join(get_arg_names(routine_map[routine_name]))
	if arg_str is "": arg_str = "** no arguments **"
	print("{routine_name:>20}: {arg_str}".format(routine_name=routine_name, arg_str=arg_str))

if routine_name == None:
	print("No routine specified, turning off")
	off()
elif routine_name == "help":
	if len(cli_args) >= 1: print_help(cli_args[0])
	else:
		for r in routines: print_help(r.__name__)
else: do_routine(routine_name)
