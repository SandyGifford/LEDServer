import time
from utils.py_utils import run_loop
from utils.light_utils import make_multi_grad
from PixelGroup.PixelGroupChain import PixelGroupChain
from consts import REDIS_PORT, LED_CONFIG, LED_COUNT
from collections import namedtuple
import logging
import os
import redis

db = redis.Redis(
	host="localhost",
	port=REDIS_PORT,
	decode_responses=True
)

def from_db():
	chain = PixelGroupChain(LED_CONFIG)


	def read_write_time():
		write_time = float(db.get("write_time") or 0)

		if not write_time:
			logging.warn("Could not read write_time, using default 0")
			write_time = 0

		return write_time

	def read_colors():
		colors_string = db.get("colors") or "0,0,0"

		lines = colors_string.splitlines()

		colors = []

		for i, color_str in enumerate(lines):
			try:
				split = color_str.split(",")
				colors.append((int(split[0]), int(split[1]), int(split[2])))
			except BaseException as e:
				logging.warn("Could not read line " + str(i) + " of color file, skipping")
				logging.error(e)

		if len(colors) == 0: colors = [(0, 0, 0)]

		return colors

	def render_pixels(colors):
		chain.fade_to_all(make_multi_grad(colors, LED_COUNT), 0.5)


	render_pixels(read_colors())
	last_write_time = read_write_time()

	def loop():
		nonlocal last_write_time

		write_time = read_write_time()

		if write_time > last_write_time:
			render_pixels(read_colors())
			last_write_time = write_time

		time.sleep(1)

	run_loop(loop)
