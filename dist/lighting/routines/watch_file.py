import time
from utils.py_utils import run_loop
from PixelGroup.PixelGroupChain import PixelGroupChain
from consts import COLOR_FILE_PATH
from collections import namedtuple

ColorFileData = namedtuple("ColorFileData", ["write_time", "colors"])

def watch_file():
	chain = PixelGroupChain([120])

	open(COLOR_FILE_PATH, "w").close()

	def read_colors():
		color_file = open(COLOR_FILE_PATH, "r")
		string = color_file.read() or "0,0,0"
		color_file.close()

		lines = string.splitlines()
		write_time = int(lines[0])

		color_lines = lines[1:]
		colors = []

		for color_str in color_lines:
			split = color_str.split(",")
			colors.push((int(split[0]), int(split[1]), int(split[2])))

		return ColorFileData(write_time, colors)

	initial_file_data = read_colors()
	last_colors = initial_file_data.colors
	last_write_time = initial_file_data.write_time

	def loop():
		nonlocal last_colors, last_write_time

		file_data = read_colors()
		write_time = initial_file_data.write_time
		colors = initial_file_data.colors

		if write_time > last_write_time:
			chain.fade_to_all(colors, 0.5)
			last_colors = colors

		time.sleep(1)

	run_loop(loop)
