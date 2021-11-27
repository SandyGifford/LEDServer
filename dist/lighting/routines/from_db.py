import time
from utils.py_utils import run_loop
from utils.light_utils import make_multi_grad
from PixelGroup.PixelGroupChain import PixelGroupChain
from consts import REDIS_PORT, LED_CONFIG, LED_COUNT
from collections import namedtuple
import logging
import os
import redis
import json

db = redis.Redis(
	host="localhost",
	port=REDIS_PORT,
	decode_responses=True
)

def from_db():
	chain = PixelGroupChain(LED_CONFIG)

	def read_write_time():
		write_time = float(db.get("lastWrite") or 0)

		if not write_time:
			logging.warn("Could not read lastWrite, using default 0")
			write_time = 0

		return write_time

	def read_colors():
		color_data = json.loads(db.get("solidColor") or "{\"type\":\"solidColor\",\"color\":[0,0,0]}")

		return [color_data["color"]]

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
