import time
from utils.py_utils import run_loop
from utils.light_utils import make_multi_grad
from PixelGroup.PixelGroupChain import PixelGroupChain
from consts import COLOR_FILE_PATH
from collections import namedtuple
import logging
import os

ColorFileData = namedtuple("ColorFileData", ["write_time", "colors"])

def watch_file():
	PIXEL_COUNT = 120
	chain = PixelGroupChain([PIXEL_COUNT])

	if (not os.path.exists(COLOR_FILE_PATH)): open(COLOR_FILE_PATH, "x").close()

	def read_colors():
		color_file = open(COLOR_FILE_PATH, "r")
		string = color_file.read() or "0,0,0"
		color_file.close()

		lines = string.splitlines()

		write_time = time.time()
		colors = [(0, 0, 0)]

		try:
			write_time = int(lines[0])
		except e:
			logging.warn("Could not read write_time, using default 0")
			logging.error(e)

		color_lines = lines[1:]
		colors = []

		for i, color_str in enumerate(color_lines):
			try:
				split = color_str.split(",")
				colors.append((int(split[0]), int(split[1]), int(split[2])))
			except e:
				logging.warn("Could not read line " + str(i) + " of color file, skipping")
				logging.error(e)

		if len(colors) == 0: colors = [(0, 0, 0)]

		return ColorFileData(write_time, colors)

	def render_pixels(colors):
		chain.fade_to_all(make_multi_grad(colors, PIXEL_COUNT), 0.5)

	initial_file_data = read_colors()
	render_pixels(initial_file_data.colors)
	last_write_time = initial_file_data.write_time

	def loop():
		nonlocal last_write_time

		file_data = read_colors()
		write_time = file_data.write_time
		colors = file_data.colors

		if write_time > last_write_time:
			render_pixels(colors)
			last_write_time = write_time

		time.sleep(1)

	run_loop(loop)
